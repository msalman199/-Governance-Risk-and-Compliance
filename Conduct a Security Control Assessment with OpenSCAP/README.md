<div align="center">

# 🕵️ Conduct a Security Control Assessment with OpenSCAP

![CGRC](https://img.shields.io/badge/CGRC-Domain%205-orange?style=for-the-badge)
![OpenSCAP](https://img.shields.io/badge/OpenSCAP-Compliance%20Scanning-2E8B57?style=for-the-badge)
![DISA STIG](https://img.shields.io/badge/DISA-STIG-C1272D?style=for-the-badge)
![SAR](https://img.shields.io/badge/Security%20Assessment%20Report-SAR-4B0082?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Terminal-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**An end-to-end STIG compliance assessment: scan, triage, remediate, report**

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [📥 Task 1: Install OpenSCAP, SCAP Security Guide, and STIG Content](#-task-1-install-openscap-scap-security-guide-and-stig-content)
- [📝 Task 2: Develop a Security Assessment Plan (SAP) and Independence Statement](#-task-2-develop-a-security-assessment-plan-sap-and-independence-statement)
- [🔎 Task 3: Run Automated Scans Against the Target Baseline](#-task-3-run-automated-scans-against-the-target-baseline)
- [🩺 Task 4: Triage Findings and Document Remediation Actions](#-task-4-triage-findings-and-document-remediation-actions)
- [📄 Task 5: Produce a Security Assessment Report (SAR)](#-task-5-produce-a-security-assessment-report-sar)
- [✅ Verification](#-verification)
- [🧠 Key Concepts](#-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Install and configure **OpenSCAP**, SCAP Security Guide, and STIG content on a Linux system |
| 2 | Draft a security assessment plan and assessor independence statement per **CGRC Domain 5** practices |
| 3 | Execute automated compliance scans against a STIG baseline |
| 4 | Triage scan findings and document remediation actions |
| 5 | Compile results into a formal **Security Assessment Report (SAR)** |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 💻 Linux command line | Package management, file editing, redirecting output |
| 📘 Compliance concepts | Controls, baselines, findings |
| 🎓 STIG terminology | NIST/DISA STIG severity categories (CAT I/II/III) |
| 🧩 OpenSCAP experience | None required — comfort reading XML/HTML reports is helpful |

## 🖥️ Environment Setup

> 🧪 **Al Nafi provides a single Linux machine (RHEL/CentOS/Fedora or Ubuntu) via Start Lab.** All work is performed locally — no external cloud services required.

**1️⃣ Confirm root or sudo access before starting:**

```bash
sudo whoami
```

---

## 📥 Task 1: Install OpenSCAP, SCAP Security Guide, and STIG Content

**RHEL/CentOS/Fedora:**

```bash
sudo dnf install -y openscap openscap-scanner scap-security-guide
```

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install -y libopenscap8 ssg-debderived ssg-nondebian
```

**Verify installation:**

```bash
oscap --version
```

**Locate available STIG/benchmark content:**

```bash
ls /usr/share/xml/scap/ssg/content/
```

**📝 TODO:** Identify the datastream file matching your OS (e.g., `ssg-rhel9-ds.xml` or `ssg-ubuntu2204-ds.xml`)

**📝 TODO:** List available profiles within that datastream using:

```bash
oscap info /usr/share/xml/scap/ssg/content/<your-datastream-file>.xml
```

Record the profile ID that references "STIG" (e.g., `xccdf_org.ssgproject.content_profile_stig`)

---

## 📝 Task 2: Develop a Security Assessment Plan (SAP) and Independence Statement

**1️⃣ Create a working directory:**

```bash
mkdir -p ~/scap-assessment/{plans,results,reports}
cd ~/scap-assessment
```

**2️⃣ Create `plans/assessment_plan.md`** and complete the template below:

```markdown
# Security Assessment Plan

## Scope
- Target system: <hostname / IP>
- Baseline: <STIG profile ID selected in Task 1>
- Assessment type: Automated technical control testing

## Objectives
- TODO: State the purpose (e.g., verify implementation of DISA STIG hardening controls)

## Methodology
- TODO: Describe scan tool (OpenSCAP), scan type (compliance), and evidence collection method

## Roles and Responsibilities
- Assessor: <your name>
- System Owner: <role, not the assessor>

## Assessor Independence Statement
- TODO: Write a 2-3 sentence statement confirming the assessor has no operational
  responsibility for the target system and no conflict of interest, per CGRC
  Domain 5 independence requirements

## Schedule
- TODO: Add planned start/end date and time for the scan
```

> 📌 This plan must be finalized before running scans (reflects real-world assessment governance)

---

## 🔎 Task 3: Run Automated Scans Against the Target Baseline

**1️⃣ Run an XCCDF evaluation using your chosen STIG profile:**

```bash
sudo oscap xccdf eval \
  --profile <profile_id_from_task1> \
  --results results/scan-results.xml \
  --report results/scan-report.html \
  /usr/share/xml/scap/ssg/content/<datastream-file>.xml
```

**📝 TODO:** Replace `<profile_id_from_task1>` and `<datastream-file>` with your actual values

**📝 TODO:** Open `results/scan-report.html` in a browser (or `less` for a text overview) and identify:
- Total rules evaluated
- Pass / Fail / Not Applicable counts
- At least 5 failed rules with their severity (CAT I/II/III equivalent)

**2️⃣ Generate a plain-text summary for quick reference:**

```bash
oscap xccdf generate report results/scan-results.xml > results/scan-summary.html
```

> ⚠️ **Troubleshooting:**
> - If `oscap` reports "no profile found," re-run `oscap info` to confirm exact profile ID spelling
> - If scan exits with permission errors, confirm you used `sudo`

---

## 🩺 Task 4: Triage Findings and Document Remediation Actions

**1️⃣ Create `results/findings_triage.csv`** and complete entries for your failed rules:

```csv
Rule ID,Title,Severity,Risk Rating,Remediation Action,Owner,Target Date
xccdf_org.ssgproject...,<rule title>,<CAT I/II/III>,<High/Med/Low>,<TODO: describe fix>,<TODO>,<TODO>
```

**📝 TODO:** Populate at least 5 rows from your `scan-report.html` failed rules

**📝 TODO:** For 2 findings, attempt an actual remediation (e.g., adjust a config file, disable a service) and re-scan to confirm the rule now passes:

```bash
sudo oscap xccdf eval \
  --profile <profile_id> \
  --results results/rescan-results.xml \
  --report results/rescan-report.html \
  /usr/share/xml/scap/ssg/content/<datastream-file>.xml
```

Compare `scan-report.html` vs `rescan-report.html` to confirm improvement

---

## 📄 Task 5: Produce a Security Assessment Report (SAR)

Create `reports/SAR.md` using this structure:

```markdown
# Security Assessment Report (SAR)

## 1. Executive Summary
- TODO: Summarize overall security posture in 3-5 sentences

## 2. Assessment Scope and Methodology
- TODO: Reference the assessment plan (Task 2) and tool used (OpenSCAP + profile ID)

## 3. Results Summary
- TODO: Insert pass/fail counts and percentage compliance from scan-report.html

## 4. Detailed Findings
- TODO: Insert your triage table from Task 4

## 5. Remediation Status
- TODO: Note which findings were remediated and verified via rescan

## 6. Assessor Conclusion
- TODO: State whether controls are "implemented correctly and operating effectively"
  or require a Plan of Action and Milestones (POA&M)

## 7. Appendices
- Attach: scan-report.html, rescan-report.html, assessment_plan.md
```

---

## ✅ Verification

Confirm lab completion on the same machine:

```bash
ls ~/scap-assessment/plans/assessment_plan.md
ls ~/scap-assessment/results/scan-report.html
ls ~/scap-assessment/results/findings_triage.csv
ls ~/scap-assessment/reports/SAR.md
oscap xccdf eval --profile <profile_id> --results /tmp/verify.xml \
  /usr/share/xml/scap/ssg/content/<datastream-file>.xml && echo "Scan re-runs successfully"
```

**Checklist:**

- [ ] OpenSCAP and SCAP content installed and version confirmed
- [ ] Assessment plan includes completed independence statement
- [ ] Initial scan report generated with pass/fail counts
- [ ] At least 5 findings triaged with remediation actions
- [ ] At least 2 findings remediated and re-scanned successfully
- [ ] SAR completed referencing all prior artifacts

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| ✅ OpenSCAP / STIG | Automated compliance scanning against a DISA Security Technical Implementation Guide baseline |
| 🚦 CAT I/II/III | STIG severity categories ranking finding risk from most (I) to least (III) critical |
| 📝 Assessment Plan (SAP) | The scope, methodology, and schedule agreed before scanning begins |
| ⚖️ Assessor Independence | Confirmation the assessor has no operational responsibility for or conflict of interest in the target system |
| 🩺 Findings Triage | Documenting each failed rule's severity, risk, and remediation owner |
| 📄 Security Assessment Report (SAR) | The formal deliverable summarizing results, remediation status, and the assessor's conclusion |
| 📌 POA&M | Plan of Action and Milestones — the remediation roadmap for findings not yet resolved |

---

## 🏁 Conclusion

In this lab, you performed an end-to-end security control assessment aligned to CGRC Domain 5 practices.

### 🎯 Key Accomplishments
- Installed OpenSCAP and STIG-based SCAP content
- Authored an assessment plan with an assessor independence statement
- Executed automated compliance scans
- Triaged and remediated real findings
- Consolidated everything into a formal Security Assessment Report

### 🌍 Real-World Applications
This workflow mirrors real-world compliance auditing tasks performed by **Cybersecurity Auditors** validating whether technical controls are implemented correctly and operating as intended.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
