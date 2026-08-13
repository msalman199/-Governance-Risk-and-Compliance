<div align="center">

# 🔐 Implement Technical Controls and Evidence Capture

![CGRC](https://img.shields.io/badge/CGRC-Domain%204%20%26%205-orange?style=for-the-badge)
![SP 800-53](https://img.shields.io/badge/NIST-SP%20800--53-0052CC?style=for-the-badge)
![OpenSCAP](https://img.shields.io/badge/OpenSCAP-Baseline%20Validation-2E8B57?style=for-the-badge)
![auditd](https://img.shields.io/badge/auditd-fail2ban-AIDE-C1272D?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Linux-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

**Deploying, validating, and evidencing technical security controls on a Linux workload**

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🛡️ Task 1: Deploy Hardened Workload Components](#️-task-1-deploy-hardened-workload-components)
- [👤 Task 2: Configure Access Control (AC-2, AC-3)](#-task-2-configure-access-control-ac-2-ac-3)
- [📝 Task 3: Configure Audit Logging (AU-2, AU-12)](#-task-3-configure-audit-logging-au-2-au-12)
- [✅ Task 4: Validate Baseline with OpenSCAP](#-task-4-validate-baseline-with-openscap)
- [🔏 Task 5: Capture Evidence Artifacts (Tamper-Evident Storage)](#-task-5-capture-evidence-artifacts-tamper-evident-storage)
- [📇 Task 6: Build the Evidence Index](#-task-6-build-the-evidence-index)
- [🔎 Verification](#-verification)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧠 Key Concepts](#-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Deploy and configure **auditd**, **fail2ban**, and **AIDE** as technical controls on Ubuntu |
| 2 | Implement access control (**AC-2, AC-3**) and audit logging (**AU-2, AU-12**) settings |
| 3 | Validate configuration baselines using **OpenSCAP** |
| 4 | Capture and hash evidence artifacts in a tamper-evident structure |
| 5 | Build an evidence index mapping artifacts to SP 800-53 control IDs |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 💻 Linux command line | Basic — users, permissions, systemd |
| 📘 SP 800-53 familiarity | Control families (AC, AU) |
| 🎓 CGRC context | Understanding of CGRC Domains 4 (Implementation) and 5 (Assessment) |
| ✏️ Config editing | Comfort with `nano` or `vim` |

## 🖥️ Environment Setup

> 🧪 **Al Nafi provides a single Ubuntu Linux machine via Start Lab.** Log in via the provided terminal/SSH access.

**1️⃣ Update the system before starting:**

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🛡️ Task 1: Deploy Hardened Workload Components

**1️⃣ Install the core control tools:**

```bash
sudo apt install -y auditd audispd-plugins fail2ban aide aide-common
```

**2️⃣ Verify each service:**

```bash
sudo systemctl status auditd --no-pager
sudo systemctl status fail2ban --no-pager
```

**3️⃣ Initialize AIDE** (file integrity baseline):

```bash
sudo aideinit
# TODO: locate the generated database (usually /var/lib/aide/aide.db.new.gz)
# TODO: promote it to the active database (aide.db.gz) so future checks work
```

> ✅ **Checkpoint:** Confirm `auditd` and `fail2ban` are active (running) before proceeding.

---

## 👤 Task 2: Configure Access Control (AC-2, AC-3)

**AC-2 (Account Management):** Create a restricted service account and a controls-admin group.

```bash
sudo groupadd controls-admins
sudo useradd -m -s /bin/bash svc-audit
# TODO: add svc-audit to controls-admins group
# TODO: set an account expiration policy using chage (e.g., 90 days)
```

**AC-3 (Access Enforcement):** Restrict access to sensitive directories.

```bash
sudo mkdir -p /opt/evidence
# TODO: set ownership to root:controls-admins
# TODO: set permissions so only owner/group can read/write (no world access)
```

> 📌 Document your choices — you will reference these settings when building the evidence index.

---

## 📝 Task 3: Configure Audit Logging (AU-2, AU-12)

**AU-2 (Event Logging):** Add audit rules for account and access changes.

Edit `/etc/audit/rules.d/audit.rules` and add:

```
-w /etc/passwd -p wa -k identity_changes
-w /etc/group -p wa -k identity_changes
-w /etc/sudoers -p wa -k privilege_escalation
-w /opt/evidence -p wa -k evidence_access
```

**AU-12 (Audit Generation):** Load rules and confirm generation.

```bash
sudo augenrules --load
sudo systemctl restart auditd
# TODO: trigger a test event (e.g., sudo touch /etc/passwd.test)
# TODO: verify it was logged using ausearch -k identity_changes
```

**Configure fail2ban for SSH monitoring** (supports AU-2 event capture):

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
# TODO: edit jail.local, enable the [sshd] section, set maxretry = 5
sudo systemctl restart fail2ban
```

---

## ✅ Task 4: Validate Baseline with OpenSCAP

**1️⃣ Install OpenSCAP and a SCAP content set:**

```bash
sudo apt install -y libopenscap8 ssg-debderived
```

**2️⃣ Locate available content:**

```bash
ls /usr/share/xml/scap/ssg/content/
```

**3️⃣ Run an evaluation** (adjust filename to your Ubuntu version's datastream):

```bash
sudo oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis_level1_server \
  --results /opt/evidence/scap-results.xml \
  --report /opt/evidence/scap-report.html \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
```

> ⚠️ **Troubleshooting:** If the datastream file name differs, use the `ls` output from above. If the profile ID errors out, list profiles with:
> ```bash
> oscap info /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
> ```

---

## 🔏 Task 5: Capture Evidence Artifacts (Tamper-Evident Storage)

**1️⃣ Collect artifacts into `/opt/evidence`:**

```bash
sudo auditctl -l > /opt/evidence/audit-rules.txt
sudo fail2ban-client status sshd > /opt/evidence/fail2ban-status.txt
sudo aide --check > /opt/evidence/aide-check.txt 2>&1
getent passwd > /opt/evidence/account-listing.txt
```

**2️⃣ Generate cryptographic hashes for tamper evidence:**

```python
# evidence_hash.py
import hashlib
import os
import json
from datetime import datetime

def hash_file(filepath: str) -> str:
    """
    Compute SHA-256 hash of a given file.

    Args:
        filepath: Path to the file to hash

    Returns:
        Hexadecimal SHA-256 digest as a string
    """
    # TODO: open file in binary mode
    # TODO: read in chunks and update hashlib.sha256()
    # TODO: return hex digest
    pass

def build_manifest(evidence_dir: str, output_file: str) -> dict:
    """
    Walk evidence_dir, hash each file, and write a JSON manifest.

    Args:
        evidence_dir: Directory containing evidence artifacts
        output_file: Path to write the manifest JSON

    Returns:
        Dictionary of {filename: {hash, timestamp}}
    """
    manifest = {}
    # TODO: iterate over files in evidence_dir (skip the manifest itself)
    # TODO: call hash_file() for each artifact
    # TODO: record hash + datetime.utcnow().isoformat() per file
    # TODO: write manifest dict to output_file as JSON
    return manifest

if __name__ == "__main__":
    build_manifest("/opt/evidence", "/opt/evidence/manifest.json")
```

**3️⃣ Run it and lock down permissions:**

```bash
python3 evidence_hash.py
sudo chmod 440 /opt/evidence/*
sudo chattr +i /opt/evidence/manifest.json   # optional: make immutable
```

---

## 📇 Task 6: Build the Evidence Index

Create `/opt/evidence/evidence-index.csv` mapping artifacts to controls:

```csv
control_id,control_name,artifact_file,description
AC-2,Account Management,account-listing.txt,List of system accounts
AC-3,Access Enforcement,# TODO,# TODO
AU-2,Event Logging,audit-rules.txt,Active audit rules
AU-12,Audit Generation,# TODO,# TODO
CM-6,Configuration Settings,scap-results.xml,OpenSCAP baseline results
SI-7,Software Integrity,aide-check.txt,AIDE file integrity check
```

**📝 Complete the `# TODO` rows** referencing the fail2ban status and manifest files.

---

## 🔎 Verification

Run these checks to confirm lab completion:

```bash
# Services running
systemctl is-active auditd fail2ban

# Audit rule triggered a log entry
sudo ausearch -k identity_changes | tail -5

# Evidence directory populated and permissions locked
ls -l /opt/evidence

# Manifest contains hashes
cat /opt/evidence/manifest.json

# Evidence index complete (no TODO markers remain)
grep -i "TODO" /opt/evidence/evidence-index.csv
```

**Expected outcome:** all services active, at least one audit event logged, `/opt/evidence` contains SCAP results, text artifacts, `manifest.json`, and a completed `evidence-index.csv` with no leftover TODOs.

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique Name | How This Lab Addresses It |
|---|---|---|
| T1098 | Account Manipulation | AC-2 restricted service account + group creation, with audit rules watching `/etc/passwd` and `/etc/group` for changes |
| T1548 | Abuse Elevation Control Mechanism | Audit rule watches `/etc/sudoers` for privilege-escalation attempts |
| T1110 | Brute Force | fail2ban SSH jail configuration detects and blocks repeated authentication failures |
| T1565.001 | Stored Data Manipulation | AIDE file integrity baseline detects unauthorized changes to monitored files |
| T1070 | Indicator Removal | Audit logging of `/opt/evidence` access plus tamper-evident SHA-256 manifest hashing deters and detects evidence tampering |

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| 🛡️ Technical Control | A control implemented through system configuration or software rather than policy alone |
| 📗 auditd | The Linux audit daemon that logs security-relevant system events |
| 🚫 fail2ban | Monitors logs and bans hosts showing malicious behavior (e.g., repeated SSH failures) |
| 🧬 AIDE | Advanced Intrusion Detection Environment — a file integrity checker |
| ✅ OpenSCAP | Validates a system's configuration against a SCAP benchmark (e.g., CIS) |
| 🔏 Tamper-Evident Evidence | Artifacts hashed and permission-locked so any later modification is detectable |

---

## 🏁 Conclusion

In this lab, you implemented technical controls on a Linux workload aligned to SP 800-53 (AC-2, AC-3, AU-2, AU-12), deployed auditd, fail2ban, and AIDE, and validated system configuration using OpenSCAP.

### 🎯 Key Accomplishments
- Captured evidence artifacts and generated tamper-evident SHA-256 hashes
- Mapped each artifact to its corresponding control in an evidence index

### 🌍 Real-World Applications
These skills directly support **CGRC Domain 4 (Implementation)** by demonstrating control deployment, and **Domain 5 (Assessment/Authorization)** by producing auditable, machine-readable evidence suitable for a security assessment package.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
