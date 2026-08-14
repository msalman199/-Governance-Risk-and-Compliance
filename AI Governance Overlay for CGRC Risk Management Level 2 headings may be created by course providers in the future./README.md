<div align="center">

# 🤖 AI Governance Overlay for CGRC Risk Management

![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NIST AI RMF](https://img.shields.io/badge/NIST%20AI-RMF%20600--1-002F6C?style=for-the-badge&logo=nist&logoColor=white)
![OSCAL](https://img.shields.io/badge/OSCAL-SP%20800--53-1E3A8A?style=for-the-badge&logo=json&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-JSON-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

*Build an AI-specific risk register, map it to the NIST AI RMF, and cross-walk it into a CGRC RMF package*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🩺 Scenario](#-scenario)
- [🗂️ Task 1: Build the AI Risk Register](#️-task-1-build-the-ai-risk-register)
- [🧭 Task 2: Map Use Case to NIST AI RMF Profiles](#-task-2-map-use-case-to-nist-ai-rmf-profiles)
- [🔍 Task 3: Identify AI-Specific Harms and Data Lineage Risks](#-task-3-identify-ai-specific-harms-and-data-lineage-risks)
- [🗺️ Task 4: Select and Cross-Map Controls (AI 600-1 + SP 800-53)](#️-task-4-select-and-cross-map-controls-ai-600-1--sp-800-53)
- [📄 Task 5: Produce AI Risk Treatment Plan and AO Briefing](#-task-5-produce-ai-risk-treatment-plan-and-ao-briefing)
- [✅ Verification](#-verification)
- [🗝️ Key Concepts](#️-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By completing this lab, you will:

| # | Objective |
|---|---|
| 1 | Configure a Python-based AI risk register on a Linux system |
| 2 | Map an AI use case to NIST AI RMF profiles (Govern, Map, Measure, Manage) |
| 3 | Identify algorithmic harms, bias vectors, and data lineage gaps for a black-box ML system |
| 4 | Cross-map NIST AI 600-1 controls to SP 800-53 control families within a CGRC RMF package |
| 5 | Produce an AI risk treatment plan and AO briefing artifact |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🏛️ NIST RMF | Working knowledge of Categorize, Select, Implement, Assess, Authorize, Monitor |
| 📖 SP 800-53 | Familiarity with control families and CGRC authorization packages |
| 🐍 Python | 3.10+ scripting proficiency (JSON/YAML handling, CLI tools) |
| 🧠 ML Risk Concepts | Conceptual understanding of model risk (bias, drift, explainability) |
| 🐙 Git/Linux CLI | Basic competency |

## 🖥️ Environment Setup

> **Lab Environment:** Single Linux machine (provided via Al Nafi **Start Lab**). No cloud dependencies required.

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv git jq  # 📦 core toolchain
mkdir -p ~/ai-governance-lab/{register,profiles,evidence,artifacts}      # 📁 workspace layout
cd ~/ai-governance-lab
python3 -m venv venv && source venv/bin/activate
pip install pandas pyyaml jsonschema tabulate                            # 🐍 Python libs
```

**Clone reference control catalogs** (mirrors are acceptable if the NIST source is unreachable):

```bash
# SP 800-53 Rev 5 OSCAL catalog (JSON)
git clone --depth 1 https://github.com/usnistgov/oscal-content.git
ls oscal-content/nist.gov/SP800-53/rev5/json/
```

> Retrieve or manually transcribe the NIST AI RMF Playbook and AI 600-1 (Generative AI Profile) control text into `profiles/ai_600-1_controls.yaml` — no official machine-readable OSCAL exists yet, so **you must structure this yourself**.

---

## 🩺 Scenario

Your organization is deploying an AI-enabled clinical decision-support tool derived from a BCI signal-classification model (black-box neural network) that flags anomalous neural activity for physician review. **You are the AI Governance Lead** building the CGRC authorization package overlay.

---

## 🗂️ Task 1: Build the AI Risk Register

Design a structured risk register that extends a standard CGRC risk register with AI-specific fields.

**Required fields:** `risk_id`, `ai_lifecycle_stage`, `harm_category`, `affected_rmf_function` (Govern/Map/Measure/Manage), `likelihood`, `impact`, `data_lineage_source`, `bias_vector`, `mapped_controls` (AI 600-1 + 800-53), `treatment_status`

Build `register/risk_register.py`:

```python
import pandas as pd
from typing import List, Dict

SCHEMA_COLUMNS = [
    "risk_id", "ai_lifecycle_stage", "harm_category",
    "affected_rmf_function", "likelihood", "impact",
    "data_lineage_source", "bias_vector",
    "mapped_controls", "treatment_status"
]

def load_register(path: str) -> pd.DataFrame:
    """Load existing risk register CSV or initialize empty schema."""
    # TODO: handle file-not-found by creating empty DataFrame with SCHEMA_COLUMNS
    pass

def add_risk_entry(df: pd.DataFrame, entry: Dict) -> pd.DataFrame:
    """Validate entry against SCHEMA_COLUMNS and append."""
    # TODO: validate required keys, compute risk_score = likelihood * impact
    pass

def export_register(df: pd.DataFrame, path: str) -> None:
    """Persist register to CSV for evidence artifact."""
    pass
```

**📌 Populate at least 8 risk entries** covering: training data drift, label bias from underrepresented patient cohorts, lack of model explainability for clinician trust, adversarial input manipulation, third-party model provenance gaps, PII leakage via model inversion, automation bias by end users, and lifecycle retraining without re-validation.

---

## 🧭 Task 2: Map Use Case to NIST AI RMF Profiles

Create `profiles/use_case_profile.yaml` mapping your clinical BCI model to the four AI RMF functions.

- **Govern:** Define roles (AI Governance Lead, Data Steward, Clinical SME), policy references, accountability structure
- **Map:** Document context of use, intended vs. foreseeable misuse, stakeholder impact (patients, clinicians, regulators)
- **Measure:** Define metrics for bias (e.g., demographic parity), explainability (e.g., SHAP coverage threshold), and performance drift
- **Manage:** Define risk prioritization criteria and response triggers (retrain, rollback, human-in-loop override)

**Write a Python validator:**

```python
import yaml
from jsonschema import validate

def load_profile(path: str) -> dict:
    """Load YAML profile mapping."""
    pass

def validate_profile_completeness(profile: dict) -> List[str]:
    """
    Check that Govern, Map, Measure, Manage sections exist
    and each has at least 3 populated sub-fields.
    Return list of missing/incomplete sections.
    """
    pass
```

Run validation and resolve all gaps before proceeding.

---

## 🔍 Task 3: Identify AI-Specific Harms and Data Lineage Risks

Build a data lineage trace and harm taxonomy.

- Trace the model's data pipeline: source datasets → preprocessing → feature engineering → training → deployment. Document any unverifiable provenance links.
- Classify harms using categories from NIST AI 600-1: representational harm, allocative harm, quality-of-service harm, informational harm
- For each harm, identify the responsible lifecycle stage and whether it maps to a Govern, Map, Measure, or Manage gap

**📦 Deliverable:** `evidence/harm_lineage_report.md` containing a lineage diagram (ASCII or Mermaid) and a harm-to-lifecycle mapping table.

---

## 🗺️ Task 4: Select and Cross-Map Controls (AI 600-1 + SP 800-53)

Query the OSCAL catalog for candidate 800-53 controls addressing AI risk surfaces (e.g., SI-4, SI-7, RA-3, RA-9, PT-2, AC-4, SR-3, SR-11):

```bash
jq '.catalog.groups[] | select(.title=="System and Information Integrity") .controls[] | {id, title}' \
  oscal-content/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json
```

For each risk register entry, assign at least one 800-53 control and one corresponding AI 600-1 practice. Justify the pairing in `artifacts/control_crosswalk.csv` with columns: `risk_id, ai_600_1_practice, sp800_53_control, justification, residual_risk_after_control`

> **⚠️ Critically evaluate:** which risks (e.g., black-box explainability) have **no adequate 800-53 mapping** and require compensating AI-specific controls — document these gaps explicitly.

---

## 📄 Task 5: Produce AI Risk Treatment Plan and AO Briefing

- Generate `artifacts/risk_treatment_plan.md`: for each unmitigated/high-residual risk, define treatment (accept/mitigate/transfer/avoid), owner, target date, and monitoring cadence
- Generate `artifacts/ao_briefing.md`: a 1-page executive summary for the Authorizing Official covering:
  - Overall AI system risk posture (aggregate score from register)
  - Top 3 unresolved risks and business impact
  - Explainability/black-box limitations and residual risk acceptance rationale
  - Recommendation: `Authorize`, `Authorize with conditions`, or `Deny`

**Automate the aggregate score:**

```python
def compute_risk_posture(register_path: str) -> Dict[str, float]:
    """
    Load register, compute average and max risk_score,
    count of unmitigated risks, and return summary dict
    for embedding into the AO briefing.
    """
    pass
```

---

## ✅ Verification

Run the following on your Linux machine to confirm completion:

```bash
test -f register/risk_register.py && python3 -c "import ast; ast.parse(open('register/risk_register.py').read())" && echo "risk_register.py syntax OK"
test -f profiles/use_case_profile.yaml && python3 -c "import yaml; yaml.safe_load(open('profiles/use_case_profile.yaml'))" && echo "profile YAML valid"
wc -l register/risk_register.csv        # expect >= 9 lines (header + 8 entries)
test -f artifacts/control_crosswalk.csv && echo "crosswalk present"
test -f artifacts/risk_treatment_plan.md && test -f artifacts/ao_briefing.md && echo "briefing artifacts present"
```

- Confirm the harm-to-lifecycle mapping table has no unmapped harm categories.
- Confirm at least one risk in the crosswalk is flagged with "no adequate 800-53 mapping."

---

## 🗝️ Key Concepts

| Concept | Description |
|---|---|
| 🧭 NIST AI RMF | Govern/Map/Measure/Manage — the four functions used to profile AI system risk |
| 🎭 Algorithmic Harm Taxonomy | Representational, allocative, quality-of-service, and informational harms (NIST AI 600-1) |
| 🔗 Data Lineage | Tracing a model's data pipeline to expose unverifiable provenance links |
| 🗺️ AI 600-1 ↔ 800-53 Crosswalk | Pairing AI-specific practices with traditional SP 800-53 controls, and flagging gaps neither covers |
| 📄 AO Briefing | A concise, risk-posture-driven summary supporting an Authorizing Official's decision |

---

## 🏁 Conclusion

In this lab, you built an AI governance overlay on top of a standard CGRC RMF package by constructing an AI-specific risk register, mapping a clinical AI use case against the NIST AI RMF's Govern/Map/Measure/Manage functions, and tracing data lineage to expose black-box and bias-related harms. You cross-mapped NIST AI 600-1 practices to SP 800-53 controls using the OSCAL catalog, identified control gaps unique to algorithmic transparency risk, and produced a risk treatment plan and AO briefing suitable for an authorization decision. These artifacts reflect the real-world deliverables expected of an AI Governance Lead or GRC Manager preparing an AI-enabled system for CGRC authorization.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
