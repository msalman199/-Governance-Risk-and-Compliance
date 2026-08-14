<div align="center">

# 🏛️ Authorize the System: Build an ATO Package

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-YAML-000000?style=for-the-badge&logo=markdown&logoColor=white)
![GPG](https://img.shields.io/badge/GPG-Integrity%20Signing-4B0082?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)
![NIST RMF](https://img.shields.io/badge/NIST-RMF%20Domain%206-002F6C?style=for-the-badge&logo=nist&logoColor=white)
![Pandoc](https://img.shields.io/badge/Pandoc-Reveal.js-1A1A1A?style=for-the-badge&logo=pandoc&logoColor=white)

*Assemble, hash, brief, and formally authorize a complete ATO package*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🗂️ Task 1: Organize Core ATO Artifacts](#️-task-1-organize-core-ato-artifacts)
- [📝 Task 2: Draft Executive Risk Summary](#-task-2-draft-executive-risk-summary)
- [🔐 Task 3: Compile Evidence Index with Integrity Hashing](#-task-3-compile-evidence-index-with-integrity-hashing)
- [🎤 Task 4: Prepare AO Briefing Slides and Decision Memo](#-task-4-prepare-ao-briefing-slides-and-decision-memo)
- [🗝️ Key Concepts](#️-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By completing this lab, you will be able to:

| # | Objective |
|---|---|
| 1 | Assemble a structured ATO package (SSP, SAR, POA&M, risk assessment) on Linux |
| 2 | Generate a cryptographically verifiable evidence index |
| 3 | Draft an executive risk summary and AO decision memo |
| 4 | Simulate a formal authorization decision with recorded sign-off |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🏛️ NIST RMF | Working knowledge of NIST RMF / CGRC Domain 6 (Authorize) concepts |
| 🐧 Linux CLI | Familiarity with bash scripting and text-based document formats (Markdown/YAML) |
| 📄 ATO Artifacts | Understanding of SSP, SAR, POA&M artifact purposes |
| 🐍 Python | Basic Python 3 scripting ability |

## 🖥️ Environment Setup

> **Lab Environment:** Al Nafi-provided single Linux machine (Ubuntu 22.04+ assumed).

```bash
sudo apt update
sudo apt install -y python3 python3-pip pandoc tree gnupg jq  # 📦 core toolchain
pip3 install pyyaml python-docx                                 # 🐍 Python libs
```

**Create the working directory structure:**

```bash
mkdir -p ~/ato-package/{ssp,sar,poam,risk-assessment,evidence,briefing,decision}  # 📁 package layout
cd ~/ato-package
```

---

## 🗂️ Task 1: Organize Core ATO Artifacts

Design and populate the four core artifacts as structured Markdown/YAML files. **You determine schema and content depth** appropriate to a fictitious "example workload" (e.g., a mid-tier web application processing sensitive data).

### 📌 Requirements

| Artifact | Path | Must Contain |
|---|---|---|
| 📘 SSP | `ssp/system-security-plan.md` | System boundary, control implementation summary (pick 8–10 NIST 800-53 controls minimum), data flow |
| 📗 SAR | `sar/security-assessment-report.md` | Findings mapped to controls, pass/fail/partial status, risk ratings |
| 📙 POA&M | `poam/poam.csv` | Weaknesses, milestones, resource estimates, target completion dates (columns: `id,weakness,control,severity,status,milestone,due_date`) |
| 📕 Risk Assessment | `risk-assessment/risk-assessment.md` | Threat sources, likelihood/impact matrix, residual risk determination |

### ✅ Write a validation script

Checks all four artifacts exist and are non-empty, and that the POA&M CSV has the required columns:

```python
# validate_artifacts.py
import csv, os
from pathlib import Path

REQUIRED_POAM_COLUMNS = ["id", "weakness", "control", "severity", "status", "milestone", "due_date"]

def validate_package(base_dir: str) -> dict:
    """
    Validate presence and structure of SSP, SAR, POA&M, and risk assessment.

    Args:
        base_dir: root of ato-package directory

    Returns:
        dict with keys: artifact_name -> bool (valid/invalid), plus 'errors' list
    """
    # TODO: check file existence for ssp, sar, risk-assessment (non-empty .md)
    # TODO: parse poam.csv and verify REQUIRED_POAM_COLUMNS present
    # TODO: return structured result dict
    pass

if __name__ == "__main__":
    result = validate_package(".")
    print(result)
```

---

## 📝 Task 2: Draft Executive Risk Summary

### 📌 Requirements

- Create `briefing/executive-risk-summary.md`
- Must synthesize SAR findings + POA&M status into a **1-page summary** for a non-technical Authorizing Official (AO)
- Include: overall risk posture (High/Moderate/Low), top 3 residual risks, POA&M closure timeline, recommendation (`Authorize` / `Authorize with Conditions` / `Deny`)

> ⚠️ **Constraint:** no more than 400 words, no raw control IDs — translate technical findings into business risk language.

---

## 🔐 Task 3: Compile Evidence Index with Integrity Hashing

Build a script that indexes every file in the package and computes SHA-256 hashes for tamper evidence, mirroring evidence chain-of-custody practices.

```python
# build_evidence_index.py
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

def compute_sha256(filepath: str) -> str:
    """Return hex SHA-256 digest of a file."""
    # TODO: implement chunked file read + hashlib.sha256 update
    pass

def build_index(base_dir: str, output_path: str) -> None:
    """
    Walk base_dir, hash every artifact, and write a JSON evidence index.

    Each entry should include: relative_path, sha256, size_bytes, indexed_at (UTC ISO8601)
    Exclude the output index file and any .git directories.
    """
    # TODO: walk directory tree with pathlib
    # TODO: build list of entries using compute_sha256
    # TODO: write JSON to output_path
    pass

if __name__ == "__main__":
    build_index(".", "evidence/evidence-index.json")
```

### 🔁 Verify integrity later

Build a companion `verify_evidence_index.py` that re-hashes files and flags mismatches — **design this yourself** (same CLI pattern).

### ✍️ Sign the final index for non-repudiation

```bash
gpg --generate-key   # 🔑 if no key exists; use lab defaults
gpg --output evidence/evidence-index.json.sig --detach-sign evidence/evidence-index.json  # ✍️ detached signature
```

---

## 🎤 Task 4: Prepare AO Briefing Slides and Decision Memo

### 1️⃣ Convert the executive summary into slides using Pandoc (no GUI tools required)

```bash
pandoc briefing/executive-risk-summary.md -t revealjs -s -o briefing/ao-briefing.html \
  -V revealjs-url=https://unpkg.com/reveal.js@4/  # 🎬 build reveal.js deck
```

### 2️⃣ Draft `decision/decision-memo.md`

Must contain:

- System name
- Authorization boundary
- Risk summary reference
- POA&M reference
- Recommended authorization type (`Full ATO` / `Interim ATO` / `Denial`)
- A signature block placeholder for the AO

---

## 🗝️ Key Concepts

| Concept | Description |
|---|---|
| 🏛️ ATO | Authority to Operate — the formal risk decision issued by an Authorizing Official |
| 📘 SSP | System Security Plan — documents the system boundary and control implementation |
| 📗 SAR | Security Assessment Report — findings mapped to controls with risk ratings |
| 📙 POA&M | Plan of Action and Milestones — tracks weaknesses through to remediation |
| 📝 Executive Risk Summary | Translates technical findings into business risk language for non-technical decision-makers |
| 🔐 Evidence Integrity | SHA-256 hashing + GPG signing to establish a tamper-evident chain of custody |
| 👤 Authorizing Official (AO) | The individual who formally accepts risk and issues the authorization decision |

---

## 🏁 Conclusion

In this lab, you assembled a complete ATO package from the ground up: structuring the SSP, SAR, POA&M, and risk assessment as validated artifacts; distilling technical findings into a business-facing executive risk summary; building a SHA-256 evidence index with a GPG-signed integrity seal; and packaging the results into an AO-ready briefing deck and decision memo. This end-to-end workflow mirrors how a real system moves through **CGRC Domain 6 (Authorize)** — from assembled evidence to a recorded, non-repudiable authorization decision.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
