# 🔐 Internal Audit of ISMS Against ISO 27001:2022

### 🛡️ ISO 27001:2022 • ISMS Internal Audit • Evidence Collection • Nonconformities • CAP • CGRC Domain 5

[![ISO 27001](https://img.shields.io/badge/ISO%2FIEC-27001%3A2022-005B96?style=for-the-badge\&logo=iso\&logoColor=white)](https://www.iso.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge\&logo=git\&logoColor=white)](https://git-scm.com/)
[![Pandoc](https://img.shields.io/badge/Pandoc-Report%20Generation-283593?style=for-the-badge)](https://pandoc.org/)
[![Bash](https://img.shields.io/badge/Bash-Automation-4EAA25?style=for-the-badge\&logo=gnubash\&logoColor=white)](https://www.gnu.org/software/bash/)

> 🚀 **Hands-on ISMS Internal Audit Lab**
>
> Build a complete internal-audit workflow for an ISO/IEC 27001:2022-based ISMS — from audit planning and evidence collection through finding classification, corrective actions, and professional audit reporting.

---

# 🌟 Project Overview

This lab simulates an internal audit of a fictitious organization's Information Security Management System (**ISMS**) against **ISO/IEC 27001:2022**.

You will create a structured audit workspace, develop an audit plan, simulate interviews and technical walkthroughs, document audit evidence, identify nonconformities, and produce a final audit report with a **Corrective Action Plan (CAP)**.

The workflow follows:

```text id="g2zq9r"
                 🏢 ISMS
                   │
                   ▼
            📋 AUDIT PLANNING
                   │
          ┌────────┴────────┐
          ▼                 ▼
       🎯 Scope          📐 Criteria
          │                 │
          └────────┬────────┘
                   ▼
             🔎 AUDIT TESTING
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    📄 Documents  🗣️ Interviews  🖥️ Walkthroughs
        │          │          │
        └──────────┼──────────┘
                   ▼
             🧾 EVIDENCE
                   │
                   ▼
          ⚠️ FINDINGS / NCs
                   │
                   ▼
             🛠️ CORRECTIVE
                ACTION PLAN
                   │
                   ▼
             📊 AUDIT REPORT
                   │
                   ▼
             🛡️ CGRC DOMAIN 5
```

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 📁 Build an ISMS audit working environment.
* 📋 Develop an ISO 27001:2022 internal audit plan.
* 🎯 Define audit scope, objectives, and criteria.
* 🔎 Test selected Annex A controls.
* 🗣️ Conduct simulated audit interviews.
* 🖥️ Perform technical walkthroughs.
* 📂 Collect and reference audit evidence.
* ⚠️ Classify audit findings.
* 📝 Maintain a nonconformity register.
* 🛠️ Develop corrective actions.
* 📊 Generate an internal audit report.
* 📄 Convert the report to PDF.
* 🛡️ Apply practical CGRC Domain 5 audit concepts.

---

# 🧰 Technology Stack

## 💻 Core Technologies

| Technology            | Purpose                                |
| --------------------- | -------------------------------------- |
| 🐧 **Ubuntu Linux**   | Audit laboratory environment           |
| 🐍 **Python 3.10+**   | Audit automation and data processing   |
| 🐼 **Pandas**         | Checklist analysis                     |
| 🐚 **Bash**           | Evidence collection and CLI automation |
| 📝 **Markdown**       | Audit documentation                    |
| 🧩 **CSV**            | Control checklist and finding register |
| 🌳 **Tree**           | Workspace visualization                |
| 🔀 **Git**            | Optional audit-script version control  |
| 📄 **Pandoc**         | Audit report conversion                |
| 📕 **LaTeX/TeX Live** | Optional PDF rendering                 |

---

# 📚 ISO 27001:2022 Concepts

The audit should consider the ISO 27001:2022 ISMS requirements, including:

```text id="w8p1re"
CLAUSE 4  → Context of the Organization
CLAUSE 5  → Leadership
CLAUSE 6  → Planning
CLAUSE 7  → Support
CLAUSE 8  → Operation
CLAUSE 9  → Performance Evaluation
CLAUSE 10 → Improvement
```

Selected Annex A controls are used for practical testing.

Example controls:

```text id="3x8q2s"
A.5.1   Policies for information security
A.5.7   Threat intelligence
A.5.15  Access control
A.5.23  Information security for use of cloud services
A.6.3   Information security awareness, education and training
A.8.9   Configuration management
A.8.16  Monitoring activities
A.8.23  Web filtering
```

> ⚠️ The lab uses selected controls for demonstration. A real certification audit requires a complete, appropriately scoped audit program and consideration of the organization's Statement of Applicability.

---

# 📋 Prerequisites

You should have:

* 🟢 Basic Linux CLI knowledge.
* 🟢 Understanding of ISO 27001:2022.
* 🟢 Familiarity with ISMS concepts.
* 🟢 Basic understanding of Annex A.
* 🟢 Understanding of audit evidence.
* 🟢 Understanding of findings and nonconformities.
* 🟢 Basic CGRC Domain 5 knowledge.

No advanced programming experience is required.

---

# 🚀 STEP 0 — Prepare the Audit Environment

### 🟢 Objective

Verify the Linux environment and install the tools required for audit documentation and automation.

---

## 🔍 Verify Linux

```bash id="p4g7j8"
lsb_release -a
```

Verify Python:

```bash id="0wz6i2"
python3 --version
```

Verify tools:

```bash id="jqz1qf"
which git
which nano
```

---

## 📦 Install Helper Tools

```bash id="9ip3q4"
sudo apt update

sudo apt install -y \
    python3-pip \
    tree \
    pandoc \
    git
```

Install Python dependencies:

```bash id="4cq2cv"
pip3 install --user pandas tabulate
```

---

## 🎉 Success Indicator

```text id="7b8r7v"
╔══════════════════════════════════════════╗
║                                          ║
║       ✅ STEP 0 — AUDIT LAB READY        ║
║                                          ║
║  🐧 Linux       → READY                 ║
║  🐍 Python      → READY                 ║
║  🌳 Tree        → READY                 ║
║  🔀 Git         → READY                 ║
║  📄 Pandoc      → READY                 ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 📁 STEP 1 — Create the Audit Workspace

### 🔵 Objective

Create a structured repository for audit planning, evidence, findings, reports, and automation.

---

## 🗂️ Create Directories

```bash id="jv7p8e"
mkdir -p ~/isms_audit/{plan,evidence,findings,reports,scripts}

cd ~/isms_audit
```

Display the structure:

```bash id="5c7e1f"
tree
```

Expected:

```text id="v9fj2s"
isms_audit/
├── evidence/
├── findings/
├── plan/
├── reports/
└── scripts/
```

---

## 🧭 Directory Purpose

| Directory      | Purpose                          |
| -------------- | -------------------------------- |
| 📋 `plan/`     | Audit plan and control checklist |
| 📂 `evidence/` | Interview and technical evidence |
| ⚠️ `findings/` | Nonconformities and observations |
| 📊 `reports/`  | Final audit reports              |
| 🐍 `scripts/`  | Audit automation                 |

---

# 🧾 Create the Annex A Checklist

Create:

```text id="e0b5sq"
plan/annex_a_checklist.csv
```

Required columns:

```text id="8ypzbm"
Control_ID,Control_Name,Category,Status,Evidence_Ref
```

Example:

```csv id="k7f5xw"
Control_ID,Control_Name,Category,Status,Evidence_Ref
A.5.1,Policies for information security,Organizational,Not Tested,
A.5.7,Threat intelligence,Organizational,Not Tested,
A.5.15,Access control,Organizational,Not Tested,
A.5.23,Information security for use of cloud services,Organizational,Not Tested,
A.6.3,Information security awareness education and training,People,Not Tested,
A.8.9,Configuration management,Technological,Not Tested,
A.8.16,Monitoring activities,Technological,Not Tested,
A.8.23,Web filtering,Technological,Not Tested,
```

Add at least **15 sample controls**.

---

# 🐍 STEP 2 — Build the Checklist Analysis Tool

### 🟢 Objective

Automate checklist loading and status analysis using Python.

Create:

```text id="6o1o7n"
scripts/checklist_summary.py
```

Core structure:

```python id="6v8bub"
import pandas as pd


def load_checklist(csv_path: str) -> pd.DataFrame:
    """
    Load the Annex A checklist.
    """
    pass


def summarize_status(df: pd.DataFrame) -> dict:
    """
    Return control counts grouped by Status.
    """
    pass
```

---

## 📊 Expected Functionality

The script should:

1. Load the CSV.
2. Validate that `Status` exists.
3. Count each status.
4. Return a dictionary.

Example:

```text id="b1r7yz"
{
    'Not Tested': 15
}
```

---

## ▶️ Run the Script

```bash id="9i2z0r"
cd ~/isms_audit/scripts

python3 checklist_summary.py
```

---

### 🎉 Success Indicator

```text id="9of3z3"
╔══════════════════════════════════════════╗
║       ✅ STEP 2 — CHECKLIST TOOL         ║
║                                          ║
║  📋 CSV Loaded       → YES              ║
║  🔢 Status Count     → YES              ║
║  🐍 Python Script    → WORKING          ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 📋 STEP 3 — Develop the Internal Audit Plan

### 🔵 Objective

Define what will be audited, why it will be audited, and which criteria will be used.

Create:

```text id="oqj7fy"
plan/audit_plan.md
```

---

# 🎯 Required Audit Plan Sections

## 1️⃣ Audit Objective

Example:

> Verify whether the ISMS conforms to applicable ISO 27001:2022 requirements and selected Annex A controls, and evaluate whether implemented controls are operating effectively.

---

## 2️⃣ Audit Scope

Example organization:

> **AlNafi FinTech Ltd**

Example scope:

```text id="y3q4jr"
☑️ Cloud Infrastructure Team
☑️ HR onboarding process
☑️ Identity and access management
☑️ Security monitoring
☑️ Selected cloud services
```

---

## 3️⃣ Audit Criteria

Include:

```text id="x4w1cm"
ISO 27001:2022 Clauses 4–10
+
Selected Annex A controls
+
Organizational policies
+
Applicable procedures
```

---

## 4️⃣ Audit Team & Roles

Define:

```text id="g4nyo1"
👨‍💼 Lead Auditor
      │
      ├── 📋 Audit Planning
      ├── 🔎 Evidence Review
      └── 📊 Final Report

👩‍💻 Technical Auditor
      │
      └── 🖥️ Technical Walkthroughs

👤 Auditee Contacts
      │
      └── 📂 Evidence / Interviews
```

---

## 5️⃣ Audit Schedule

Example:

| Date  | Session               | Location |
| ----- | --------------------- | -------- |
| Day 1 | Opening meeting       | Virtual  |
| Day 1 | Document review       | Virtual  |
| Day 2 | IT interview          | Virtual  |
| Day 2 | HR interview          | Virtual  |
| Day 3 | Technical walkthrough | Virtual  |
| Day 3 | Findings review       | Virtual  |
| Day 4 | Closing meeting       | Virtual  |

---

## 6️⃣ Audit Resources

Include:

* 📋 Annex A checklist.
* 📂 Evidence repository.
* 🗣️ Interview templates.
* 🖥️ Technical walkthrough scripts.
* ⚠️ Finding register.
* 📊 Report template.

---

## 🔎 Validate the Plan

```bash id="bd3ntq"
wc -l plan/audit_plan.md
```

Search required sections:

```bash id="m4gk6n"
grep -E "Objective|Scope|Criteria" plan/audit_plan.md
```

Expected:

```text id="h5qgby"
Audit Objective
Audit Scope
Audit Criteria
```

---

### 🎉 Success Indicator

```text id="72c49f"
╔══════════════════════════════════════════╗
║       ✅ STEP 3 — AUDIT PLAN READY       ║
║                                          ║
║  🎯 Objective     → DEFINED             ║
║  📐 Scope         → DEFINED             ║
║  📏 Criteria      → DEFINED             ║
║  👥 Team          → DEFINED             ║
║  📅 Schedule      → DEFINED             ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 🗣️ STEP 4 — Simulate Audit Interviews

### 🟣 Objective

Collect qualitative audit evidence through structured interviews.

Create:

```text id="u1jby1"
evidence/interview_log_template.md
```

Template:

```markdown id="qv3wq7"
# Interview Log

- Auditee Name/Role:
- Date/Time:
- Control(s) Discussed:
- Questions Asked:
- Responses Summary:
- Evidence Collected:
```

---

# 👨‍💻 Interview 01 — IT Administrator

Create:

```text id="sw1jq6"
evidence/interview_01.md
```

Focus:

```text id="7dby6m"
A.8.9 — Configuration Management
```

Example evidence areas:

* Configuration standards.
* Password policies.
* Change management.
* System baselines.
* Configuration review frequency.

---

# 👩‍💼 Interview 02 — HR Representative

Create:

```text id="4m0z7q"
evidence/interview_02.md
```

Focus:

```text id="3w2v0a"
A.6.3 — Awareness, Education and Training
```

Evidence areas:

* Employee training.
* Security awareness.
* New-hire onboarding.
* Training completion records.
* Refresher training.

---

# 🖥️ STEP 5 — Perform a Technical Walkthrough

### 🟢 Objective

Collect technical evidence supporting an Annex A control.

For the lab, inspect password policy settings.

Run:

```bash id="8o9r0b"
cat /etc/login.defs | grep -i PASS_
```

---

## 💾 Save Evidence

```bash id="g8f4xu"
cat /etc/login.defs | grep -i PASS_ \
    > ~/isms_audit/evidence/A8_9_password_policy_evidence.txt
```

Review:

```bash id="syj2fc"
cat ~/isms_audit/evidence/A8_9_password_policy_evidence.txt
```

---

## 🔎 Audit Interpretation

Compare the observed configuration against the organization's documented policy.

For example:

```text id="d6z4t9"
Organization Policy
PASS_MAX_DAYS = 90

Observed System
PASS_MAX_DAYS = 180

Result
⚠️ Potential Nonconformity
```

> ⚠️ A technical setting by itself does not automatically establish an ISO 27001 nonconformity. The auditor should evaluate the applicable organizational requirement, implementation context, evidence reliability, and audit criteria before classifying the finding.

---

# 📝 STEP 6 — Update the Audit Checklist

Update:

```text id="j1v7r5"
plan/annex_a_checklist.csv
```

For `A.8.9`, change:

```text id="4q0j2c"
Status
```

from:

```text
Not Tested
```

to an appropriate result such as:

```text
Conforms
```

or:

```text
Nonconformity
```

Add:

```text id="a5f4jb"
Evidence_Ref
```

Example:

```text id="yq5w6j"
../evidence/A8_9_password_policy_evidence.txt
```

---

# ⚠️ STEP 7 — Create the Nonconformity Register

### 🔴 Objective

Create a structured register for audit findings.

Create:

```text id="hm5d7m"
findings/nonconformity_register.csv
```

Required columns:

```text id="k0n5xb"
Finding_ID,Control_ID,Description,Severity,Evidence_Ref,Recommendation
```

---

# 🏷️ Finding Classification

Use:

```text id="rjz0dl"
🔴 Major
🟠 Minor
🔵 Observation
```

### 🔴 Major

A significant failure or systemic issue that can affect ISMS conformity.

### 🟠 Minor

A limited deviation or isolated failure.

### 🔵 Observation

An improvement opportunity or condition worth management attention that is not necessarily a nonconformity.

> Classification should be based on the organization's audit criteria and the auditor's documented evidence and judgment.

---

# 🐍 STEP 8 — Automate Finding Registration

Create:

```text id="5f9c6b"
scripts/log_finding.py
```

Core function:

```python id="zqz9fs"
import csv
from datetime import date


def add_finding(
    csv_path: str,
    control_id: str,
    description: str,
    severity: str,
    evidence_ref: str,
    recommendation: str
) -> None:
    """
    Append an audit finding.
    """
    pass
```

The script should:

1. Read existing findings.
2. Generate the next finding ID.
3. Open the CSV in append mode.
4. Add the finding.
5. Preserve the existing records.

---

## 📝 Example Finding

```text id="h5f0bk"
Control: A.8.9

Description:
Password maximum age exceeds the organization's documented policy.

Severity:
Minor

Evidence:
../evidence/A8_9_password_policy_evidence.txt

Recommendation:
Align the system configuration with the approved organizational
password policy and verify implementation.
```

---

## ▶️ Run the Script

```bash id="7q4r2j"
cd ~/isms_audit/scripts

python3 log_finding.py
```

Verify:

```bash id="g3b8se"
cat ../findings/nonconformity_register.csv
```

Add at least one additional observation or improvement opportunity.

---

### 🎉 Success Indicator

```text id="w9b9cm"
╔══════════════════════════════════════════╗
║      ✅ STEP 8 — FINDINGS LOGGED         ║
║                                          ║
║  ⚠️ Findings       → RECORDED           ║
║  🏷️ Severity       → ASSIGNED           ║
║  📂 Evidence       → LINKED             ║
║  🛠️ Recommendation → DOCUMENTED         ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 📊 STEP 9 — Build the Internal Audit Report

### 🟠 Objective

Produce an executive-ready internal audit report.

Create:

```text id="4s0n0x"
reports/internal_audit_report.md
```

---

# 📑 Required Report Sections

## 1️⃣ Executive Summary

Include:

* Audit scope.
* Audit dates.
* Overall conclusion.
* Number of findings.
* Key risk areas.
* Recommended actions.

---

## 2️⃣ Audit Methodology

Document:

```text id="9qqt8s"
📄 Document Review
        +
🗣️ Interviews
        +
🖥️ Technical Walkthroughs
        +
🔎 Evidence Examination
        =
📊 Audit Conclusion
```

---

## 3️⃣ Findings Summary

Example:

| Finding | Control | Severity    | Evidence          | Status |
| ------- | ------- | ----------- | ----------------- | ------ |
| F001    | A.8.9   | Minor       | Password evidence | Open   |
| F002    | A.6.3   | Observation | HR interview      | Open   |

---

# 🛠️ STEP 10 — Create the Corrective Action Plan

### 🔵 Objective

Translate findings into actionable remediation.

Create a CAP table:

| Finding_ID | Corrective Action                        | Owner      | Target Date | Status |
| ---------- | ---------------------------------------- | ---------- | ----------- | ------ |
| F001       | Align password configuration with policy | IT Manager | TBD         | Open   |
| F002       | Improve awareness training tracking      | HR Manager | TBD         | Open   |

---

## 🔄 CAP Lifecycle

```text id="3e1x0k"
⚠️ Finding
    ↓
🔍 Root Cause
    ↓
🛠️ Corrective Action
    ↓
👤 Owner
    ↓
📅 Target Date
    ↓
🔎 Verification
    ↓
✅ Closure
```

---

# 📄 STEP 11 — Generate the PDF Report

### 🟢 Objective

Convert the Markdown report into a professional PDF.

From the reports directory:

```bash id="c1j9dq"
cd ~/isms_audit/reports

pandoc \
    internal_audit_report.md \
    -o internal_audit_report.pdf
```

Verify:

```bash id="x5t4f3"
ls -lh internal_audit_report.pdf
```

---

# 🧯 Troubleshooting PDF Generation

If Pandoc cannot generate a PDF because LaTeX is missing:

```bash id="n6a7b5"
sudo apt install -y texlive-latex-base
```

Then retry:

```bash id="p5x2j9"
pandoc internal_audit_report.md \
    -o internal_audit_report.pdf
```

If PDF generation remains unavailable, generate HTML:

```bash id="r2f9pz"
pandoc \
    internal_audit_report.md \
    -o internal_audit_report.html
```

---

### 🎉 Success Indicator

```text id="0v9r6b"
╔══════════════════════════════════════════╗
║      ✅ STEP 11 — REPORT GENERATED      ║
║                                          ║
║  📋 Audit Report    → READY             ║
║  🛠️ CAP             → INCLUDED          ║
║  📄 PDF             → GENERATED         ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 🔍 STEP 12 — Final Verification

### 🛡️ Objective

Confirm that the entire audit workflow has been completed.

---

## 🌳 Verify Directory Structure

```bash id="x4u4lm"
tree ~/isms_audit
```

---

## 📋 Check Completed Controls

```bash id="w1y1a0"
grep -c "Conforms\|Nonconformity" \
    ~/isms_audit/plan/annex_a_checklist.csv
```

---

## ⚠️ Review Findings

```bash id="kj9u6s"
cat ~/isms_audit/findings/nonconformity_register.csv
```

---

## 📄 Verify PDF

```bash id="kj0x4c"
ls -lh ~/isms_audit/reports/internal_audit_report.pdf
```

---

# ✅ Final Verification Checklist

```text id="m6w6m3"
☑️ Audit workspace created
☑️ Annex A checklist created
☑️ At least 15 controls documented
☑️ Checklist Python script completed
☑️ Audit objective defined
☑️ Audit scope defined
☑️ Audit criteria defined
☑️ Audit schedule documented
☑️ Interview template created
☑️ Two interviews simulated
☑️ Technical walkthrough completed
☑️ Evidence file created
☑️ Checklist statuses updated
☑️ Finding register created
☑️ At least 2 findings recorded
☑️ Severity assigned
☑️ Recommendations documented
☑️ CAP created
☑️ Internal audit report completed
☑️ PDF generated
```

---

# 🏆 FINAL SUCCESS SCREEN

```text id="q7x2r6"
╔════════════════════════════════════════════════════╗
║                                                    ║
║       🛡️ ISO 27001 INTERNAL AUDIT COMPLETE        ║
║                                                    ║
║   📋 Audit Plan          ✅                        ║
║   🎯 Scope & Criteria    ✅                        ║
║   📂 Evidence            ✅                        ║
║   🗣️ Interviews          ✅                        ║
║   🖥️ Walkthroughs        ✅                        ║
║   ⚠️ Findings            ✅                        ║
║   🛠️ Corrective Actions  ✅                        ║
║   📊 Audit Report        ✅                        ║
║   📄 PDF                 ✅                        ║
║                                                    ║
║              🏁 LAB SUCCESSFULLY COMPLETED         ║
║                                                    ║
╚════════════════════════════════════════════════════╝
```

---

# 🏗️ Complete Audit Architecture

```text id="n6e1g9"
                    🏢 ORGANIZATION
                          │
                          ▼
                    🔐 ISMS SCOPE
                          │
                          ▼
                  📋 AUDIT PLANNING
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
          🎯 OBJECTIVE              📐 CRITERIA
              │                       │
              └───────────┬───────────┘
                          ▼
                    🔎 AUDIT TESTING
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
   📄 DOCUMENTS       🗣️ INTERVIEWS      🖥️ WALKTHROUGHS
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
                    📂 AUDIT EVIDENCE
                          │
                          ▼
                    ⚠️ FINDINGS
                          │
                  ┌───────┴───────┐
                  ▼               ▼
              🔴 Major        🟠 Minor
                  │               │
                  └───────┬───────┘
                          ▼
                   🛠️ CORRECTIVE
                      ACTION PLAN
                          │
                          ▼
                     📊 REPORT
                          │
                          ▼
                    👔 MANAGEMENT
                          │
                          ▼
                     ✅ FOLLOW-UP
                          │
                          ▼
                   🛡️ CGRC DOMAIN 5
```





---

# 🔬 Advanced Extensions

Once the core lab is complete, you can extend it with:

* 🤖 Automated evidence collection.
* 📊 Audit dashboards.
* 🔗 Git-based evidence versioning.
* 🧾 Automated finding reports.
* 📈 Finding aging metrics.
* 🔄 Corrective-action tracking.
* 🔐 Evidence integrity hashes.
* 📋 Statement of Applicability integration.
* 🧠 Risk-based audit prioritization.
* 🛡️ Continuous control monitoring.
* 📧 Automated management notifications.
* 📊 Power BI/Tableau-compatible exports.
* 🗃️ PostgreSQL-backed audit repositories.

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

```text id="s6t6i9"
🐧 Linux
   ↓
📁 Audit Workspace Engineering
   ↓
📋 ISO 27001 Audit Planning
   ↓
🔎 Evidence Collection
   ↓
🗣️ Interview Techniques
   ↓
🖥️ Technical Walkthroughs
   ↓
⚠️ Nonconformity Management
   ↓
🛠️ Corrective Action Planning
   ↓
📊 Audit Reporting
   ↓
🛡️ CGRC Domain 5
```

---

# ⚠️ Audit Disclaimer

This laboratory is intended for **education, audit-practice exercises, and GRC skills development**.

The simulated evidence and findings are not substitutes for an actual independent audit. In a real engagement:

* Establish an appropriate audit scope.
* Use current and authoritative ISO requirements.
* Maintain auditor independence and objectivity.
* Preserve evidence securely.
* Document sampling and audit methodology.
* Base findings on sufficient, appropriate evidence.
* Distinguish observations from formal nonconformities.
* Validate corrective actions before closure.
* Protect confidential audit information.
* Ensure conclusions are supported by documented evidence.

---

# 🏁 Conclusion

This lab provides an end-to-end **ISO 27001:2022 ISMS internal audit workflow**.

You begin by establishing an audit environment and defining the audit scope and criteria. You then test selected Annex A controls through document review, interviews, and technical walkthroughs. Evidence is recorded, findings are classified, corrective actions are assigned, and the final results are transformed into a professional audit report.

The complete workflow is:

```text id="7f8z3h"
📋 PLAN
  ↓
🎯 SCOPE
  ↓
🔎 TEST
  ↓
📂 EVIDENCE
  ↓
⚠️ FINDINGS
  ↓
🛠️ CAP
  ↓
📊 REPORT
  ↓
🔍 FOLLOW-UP
  ↓
✅ CLOSURE
```

## 🛡️ Final Outcome

> **Plan the audit. Test the controls. Preserve the evidence. Report the findings. Drive corrective action.**

### 🔐 ISO 27001:2022 + Internal Audit + Evidence + CAP = Practical ISMS Audit Engineering
