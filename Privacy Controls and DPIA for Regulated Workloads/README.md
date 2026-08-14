<div align="center">

# 🔏 Privacy Controls and DPIA for Regulated Workloads

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Data%20Model-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![GPG](https://img.shields.io/badge/GPG-Integrity%20Signing-4B0082?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)
![GDPR](https://img.shields.io/badge/GDPR-PDPL-003399?style=for-the-badge&logo=europeanunion&logoColor=white)
![NIST RMF](https://img.shields.io/badge/NIST%20800--53-PT%2FPM-002F6C?style=for-the-badge&logo=nist&logoColor=white)

*Classify PII, run a DPIA, map privacy controls, and produce a signed report*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🗂️ Task 1: Build the Privacy Assessment Workbook](#️-task-1-build-the-privacy-assessment-workbook)
- [🏷️ Task 2: Identify PII Categories and Lawful Bases](#️-task-2-identify-pii-categories-and-lawful-bases)
- [⚠️ Task 3: Execute DPIA Workflow](#️-task-3-execute-dpia-workflow)
- [🗺️ Task 4: Map Mitigations to NIST SP 800-53 PT and PM Controls](#️-task-4-map-mitigations-to-nist-sp-800-53-pt-and-pm-controls)
- [✍️ Task 5: Produce a Signed DPIA Report](#️-task-5-produce-a-signed-dpia-report)
- [✅ Verification](#-verification)
- [🗝️ Key Concepts](#️-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|---|
| 1 | Set up a local privacy assessment workbook using open-source tools |
| 2 | Classify PII categories and determine lawful bases for processing under GDPR/PDPL |
| 3 | Execute a DPIA workflow and document residual privacy risks |
| 4 | Map mitigations to NIST SP 800-53 PT (Privacy) and PM (Program Management) control families |
| 5 | Generate and digitally sign a DPIA report |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🐧 Linux CLI | Basic command-line familiarity (file navigation, text editors) |
| ⚖️ GDPR/PDPL & NIST 800-53 | Understanding of fundamentals and control structure |
| 🏛️ CGRC Domains | Familiarity with Domain 3 (Risk Response) and Domain 4 (Controls) concepts |
| 📝 YAML/Markdown | No prior scripting expertise required, but comfort editing YAML/Markdown is helpful |

## 🖥️ Environment Setup

> **Lab Environment:** Al Nafi provides a single Linux machine (Ubuntu 22.04+) via **Start Lab**.

```bash
# Update system and install required tools
sudo apt update && sudo apt install -y python3-pip gnupg python3-venv git  # 📦 core toolchain

# Create working directory
mkdir -p ~/dpia-lab/{data,reports,evidence}  # 📁 workbook layout
cd ~/dpia-lab

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pandas pyyaml jinja2  # 🐍 Python libs
```

---

## 🗂️ Task 1: Build the Privacy Assessment Workbook

Create a structured YAML workbook to track PII inventory and processing activities.

```bash
cat > data/pii_inventory.yaml << 'EOF'
workload_name: "Patient Neural Signal Analytics Platform"
data_controller: "TODO: Enter organization name"
assessment_date: "TODO: YYYY-MM-DD"
data_elements:
  - field: "patient_id"
    category: "TODO: direct identifier / indirect / special category"
    sensitivity: "high"
    lawful_basis: "TODO: consent / contract / legal obligation / vital interest"
  - field: "eeg_signal_data"
    category: "special category (biometric/health)"
    sensitivity: "high"
    lawful_basis: "TODO"
  - field: "device_ip_address"
    category: "indirect identifier"
    sensitivity: "medium"
    lawful_basis: "TODO"
EOF
```

**📌 Your task:** Add 3 more realistic data elements relevant to a Brain-Computer Interface (BCI) workload (e.g., session timestamps, consent records, clinician notes). Fill in all `TODO` fields using GDPR Art. 6/9 and PDPL equivalents as reference.

---

## 🏷️ Task 2: Identify PII Categories and Lawful Bases

Write a Python script to classify records and flag special category data requiring extra safeguards.

```python
# classify_pii.py
import yaml

def load_inventory(filepath: str) -> dict:
    """
    Load the PII inventory YAML file.

    Args:
        filepath: Path to pii_inventory.yaml

    Returns:
        Parsed dictionary of inventory data
    """
    # TODO: open and parse the YAML file
    pass

def classify_records(inventory: dict) -> list:
    """
    Classify each data element by risk tier based on category and sensitivity.

    Args:
        inventory: Parsed inventory dictionary

    Returns:
        List of dicts with added 'risk_tier' key (Low/Medium/High/Critical)
    """
    # TODO: iterate data_elements
    # TODO: assign risk_tier = "Critical" if category contains "special category"
    # TODO: assign risk_tier = "High" if sensitivity == "high"
    # TODO: else assign "Medium" or "Low"
    pass

if __name__ == "__main__":
    inventory = load_inventory("data/pii_inventory.yaml")
    results = classify_records(inventory)
    for r in results:
        print(r)
```

**Run and validate:**

```bash
python3 classify_pii.py  # ▶️ run classifier
```

**Expected outcome:** Console output listing each field with an assigned risk tier. At least one field must be `Critical`.

---

## ⚠️ Task 3: Execute DPIA Workflow

Create a DPIA risk register documenting threats, likelihood, impact, and residual risk after mitigation.

```bash
cat > data/dpia_risk_register.yaml << 'EOF'
risks:
  - id: R1
    description: "Unauthorized access to raw EEG biometric data"
    likelihood: "TODO: Low/Medium/High"
    impact: "TODO: Low/Medium/High"
    inherent_risk: "TODO: calculate qualitatively"
    mitigation: "TODO: e.g., encryption at rest, RBAC"
    residual_risk: "TODO"
  - id: R2
    description: "Re-identification via device metadata correlation"
    likelihood: "TODO"
    impact: "TODO"
    inherent_risk: "TODO"
    mitigation: "TODO"
    residual_risk: "TODO"
EOF
```

**📌 Your task:**

- Add 2 additional risks specific to BCI data (e.g., third-party cloud analytics vendor, cross-border transfer to non-adequate jurisdiction)
- Complete all `TODO` fields using a qualitative 3x3 risk matrix (Low/Medium/High)
- Ensure residual risk is lower than inherent risk for each entry, reflecting applied mitigation

---

## 🗺️ Task 4: Map Mitigations to NIST SP 800-53 PT and PM Controls

Complete the control mapping table linking each mitigation to a specific control ID.

```bash
cat > data/control_mapping.yaml << 'EOF'
mappings:
  - risk_id: R1
    mitigation: "Encryption at rest and in transit"
    control_family: "PT"
    control_id: "TODO: e.g., PT-4 (Consent) or reference correct control"
  - risk_id: R2
    mitigation: "Data minimization and pseudonymization"
    control_family: "PT"
    control_id: "TODO"
EOF
```

**📌 Your task:**

- Reference NIST SP 800-53 Rev 5 Privacy control catalog (PT family: PT-1 to PT-8) and Program Management (PM-18 to PM-27 for privacy)
- Complete `control_id` for R1 and R2
- Add mappings for your R3 and R4 risks from Task 3
- Verify each mapping is logically justified (e.g., PT-6 for Data Quality, PM-25 for Minimization)

---

## ✍️ Task 5: Produce a Signed DPIA Report

Generate a consolidated Markdown report and sign it using GPG for integrity/non-repudiation.

```python
# generate_report.py
import yaml
from datetime import date

def build_report(inventory_path: str, risk_path: str, mapping_path: str, output_path: str) -> None:
    """
    Consolidate inventory, risk register, and control mappings into a DPIA report.

    Args:
        inventory_path: Path to pii_inventory.yaml
        risk_path: Path to dpia_risk_register.yaml
        mapping_path: Path to control_mapping.yaml
        output_path: Path to write the final Markdown report
    """
    # TODO: load all three YAML files
    # TODO: build a Markdown string with sections:
    #   - Workload Overview
    #   - PII Inventory Table
    #   - Risk Register Table
    #   - Control Mapping Table
    #   - Conclusion / DPO Recommendation
    # TODO: write the Markdown string to output_path
    pass

if __name__ == "__main__":
    build_report(
        "data/pii_inventory.yaml",
        "data/dpia_risk_register.yaml",
        "data/control_mapping.yaml",
        "reports/DPIA_Report.md"
    )
    print("Report generated at reports/DPIA_Report.md")
```

```bash
python3 generate_report.py  # ▶️ build the report
cat reports/DPIA_Report.md  # 👀 inspect output
```

**Now digitally sign the report:**

```bash
# Generate a local GPG key (if not already present)
gpg --batch --gen-key <<EOF
%no-protection
Key-Type: RSA
Key-Length: 2048
Name-Real: Privacy Officer
Name-Email: privacy@lab.local
Expire-Date: 0
%commit
EOF

# Sign the DPIA report
gpg --local-user privacy@lab.local --output reports/DPIA_Report.md.sig --detach-sign reports/DPIA_Report.md  # ✍️ detached signature

# Verify the signature
gpg --verify reports/DPIA_Report.md.sig reports/DPIA_Report.md  # 🔍 confirm integrity
```

---

## ✅ Verification

Confirm lab completion by running these checks on the same machine:

```bash
# 1. Confirm inventory has at least 5 data elements with no TODO remaining
grep -c "TODO" data/pii_inventory.yaml   # should return 0

# 2. Confirm risk register has 4+ risks with residual risk lower than inherent
grep -c "id:" data/dpia_risk_register.yaml   # should return 4 or more

# 3. Confirm control mappings exist for all risks
grep -c "control_id" data/control_mapping.yaml

# 4. Confirm report file exists and is non-empty
ls -lh reports/DPIA_Report.md

# 5. Confirm GPG signature is valid
gpg --verify reports/DPIA_Report.md.sig reports/DPIA_Report.md
# Expected output: "Good signature from Privacy Officer <privacy@lab.local>"
```

<details>
<summary>🛠️ Troubleshooting</summary>

- If GPG signing fails with "no default secret key," re-run key generation and confirm with `gpg --list-secret-keys`
- If YAML parsing errors occur in Python, validate syntax with `python3 -c "import yaml; yaml.safe_load(open('data/pii_inventory.yaml'))"`

</details>

---

## 🗝️ Key Concepts

| Concept | Description |
|---|---|
| 🔏 PII Classification | Categorizing data elements (direct/indirect identifier, special category) by sensitivity |
| ⚖️ Lawful Basis | The GDPR Art. 6/9 or PDPL justification for processing a given data element |
| ⚠️ DPIA | Data Protection Impact Assessment — a structured process for identifying and mitigating privacy risk |
| 📊 Inherent vs. Residual Risk | Risk before vs. after mitigation is applied |
| 🗺️ NIST 800-53 PT/PM | Privacy and Program Management control families used to formally map mitigations |
| ✍️ Non-Repudiation | GPG-signing a report so its authorship and integrity can be independently verified |

---

## 🏁 Conclusion

In this lab, you built a complete DPIA workflow on a single Linux machine using open-source tools. You classified PII categories for a regulated BCI-adjacent workload, assigned lawful bases aligned to GDPR and PDPL, and documented inherent versus residual risks in a structured risk register. You mapped mitigations to NIST SP 800-53 PT and PM privacy control families, satisfying CGRC Domain 3 and 4 requirements, and produced a GPG-signed DPIA report demonstrating integrity and accountability. These skills directly support the responsibilities of a Privacy Officer or GRC Analyst conducting privacy impact assessments for regulated data processing systems.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
