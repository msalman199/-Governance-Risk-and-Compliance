<div align="center">

# 🌐 Map ISO 27001, NIST CSF, and SAMA CSF Crosswalk

![CGRC](https://img.shields.io/badge/CGRC-Domain%201-orange?style=for-the-badge)
![ISO 27001](https://img.shields.io/badge/ISO-27001%20Annex%20A-0052CC?style=for-the-badge)
![NIST CSF](https://img.shields.io/badge/NIST-CSF%202.0-0052CC?style=for-the-badge)
![SAMA CSF](https://img.shields.io/badge/SAMA-CSF-006C35?style=for-the-badge)
![OpenRefine](https://img.shields.io/badge/OpenRefine-Data%20Cleaning-CC3333?style=for-the-badge)

**A multi-framework compliance crosswalk pipeline for GCC-region GRC teams**

</div>

> 🎓 **Skill Domain 11: Governance, Risk, and Compliance**

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [📑 Task 1: Prepare Control Catalog CSVs](#-task-1-prepare-control-catalog-csvs)
- [🧹 Task 2: Normalize Data in OpenRefine](#-task-2-normalize-data-in-openrefine)
- [🔗 Task 3: Build Mapping Logic](#-task-3-build-mapping-logic)
- [📎 Task 4: Validate Mappings with Evidence Requirements](#-task-4-validate-mappings-with-evidence-requirements)
- [📈 Task 5: Generate Stakeholder Report](#-task-5-generate-stakeholder-report)
- [✅ Verification](#-verification)
- [🧠 Key Concepts](#-key-concepts)
- [🔧 Troubleshooting Tips](#-troubleshooting-tips)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Normalize control catalogs from **ISO 27001 Annex A**, **NIST CSF 2.0**, and **SAMA CSF** into structured CSV format |
| 2 | Use **OpenRefine** to clean and reconcile control data across frameworks |
| 3 | Build a crosswalk mapping logic identifying equivalent controls and coverage gaps |
| 4 | Validate mappings against sample evidence requirements |
| 5 | Generate a stakeholder-ready crosswalk report |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 📘 Framework familiarity | Basic understanding of ISO 27001 Annex A structure, NIST CSF Functions/Categories, and SAMA CSF domains |
| 💻 Technical comfort | Linux terminal, CSV files, and basic Python |
| 🎓 GRC concepts | Controls, evidence, gap analysis |

## 🖥️ Environment Setup

> 🧪 **Al Nafi provides a single Linux machine via Start Lab.** Use it directly — no cloud account needed.

**1️⃣ Update system and install required tools:**

```bash
sudo apt update
sudo apt install -y python3 python3-pip default-jre wget unzip
```

**2️⃣ Create working directory:**

```bash
mkdir -p ~/crosswalk-lab/{data,scripts,output}
cd ~/crosswalk-lab
```

**3️⃣ Install Python libraries for data processing:**

```bash
pip3 install pandas openpyxl
```

**4️⃣ Install OpenRefine** (local, open-source data cleaning tool):

```bash
cd ~/crosswalk-lab
wget https://github.com/OpenRefine/OpenRefine/releases/download/3.8.0/openrefine-linux-3.8.0.tar.gz
tar -xzf openrefine-linux-3.8.0.tar.gz
cd openrefine-3.8.0
./refine -p 3333 &
```

- 🌐 Access OpenRefine in the lab machine's browser at `http://localhost:3333`
- 🔄 Keep this terminal session running in background

---

## 📑 Task 1: Prepare Control Catalog CSVs

Create three seed CSV files representing simplified extracts of each framework.

```bash
cd ~/crosswalk-lab/data
```

**1️⃣ Create `iso27001.csv`:**

```csv
control_id,control_title,domain
A.5.1,Policies for information security,Organizational
A.8.8,Management of technical vulnerabilities,Technological
A.5.24,Incident management planning,Organizational
A.8.16,Monitoring activities,Technological
```

**2️⃣ Create `nist_csf.csv`:**

```csv
control_id,control_title,function
GV.PO-01,Policy is established and communicated,Govern
ID.RA-01,Vulnerabilities are identified and recorded,Identify
DE.CM-01,Networks are monitored,Detect
RS.MA-01,Incident response plan is executed,Respond
```

**3️⃣ Create `sama_csf.csv`:**

```csv
control_id,control_title,principle
3.1.1,Information security policy,Leadership and Governance
3.3.4,Vulnerability management,Threat Management
3.3.9,Security event monitoring,Threat Management
3.3.12,Incident management,Threat Management
```

**📝 TODO:** Expand each CSV with at least 4 more rows using real control references from official framework documentation.

---

## 🧹 Task 2: Normalize Data in OpenRefine

**1️⃣ In OpenRefine, click `Create Project` > import each CSV separately**

**2️⃣ For each project:**
- ✂️ Use `Edit cells > Common transforms > Trim leading/trailing whitespace` on `control_title`
- 🔍 Use `Facet > Text facet` on the `domain`/`function`/`principle` column to verify consistent naming

**3️⃣ Export each cleaned project as CSV** into `~/crosswalk-lab/data/normalized_*.csv`

> ⚠️ **Troubleshooting:** If OpenRefine won't load in browser, confirm the process is running (`jobs` command) and port 3333 is not blocked.

---

## 🔗 Task 3: Build Mapping Logic

Create `~/crosswalk-lab/scripts/build_crosswalk.py`:

```python
import pandas as pd

def load_catalog(filepath: str, source_name: str) -> pd.DataFrame:
    """
    Load a normalized control catalog CSV and tag it with source framework.

    Args:
        filepath: path to normalized CSV
        source_name: label like 'ISO27001', 'NIST_CSF', 'SAMA_CSF'

    Returns:
        DataFrame with columns: control_id, control_title, category, source
    """
    # TODO: Read CSV with pandas
    # TODO: Rename domain/function/principle column to 'category'
    # TODO: Add a 'source' column with source_name
    # TODO: Return standardized DataFrame
    pass


def build_mapping(iso_df: pd.DataFrame, nist_df: pd.DataFrame,
                   sama_df: pd.DataFrame, mapping_rules: list) -> pd.DataFrame:
    """
    Build crosswalk rows from manual mapping rules.

    Args:
        iso_df, nist_df, sama_df: standardized DataFrames
        mapping_rules: list of dicts, e.g.
            {"iso": "A.5.1", "nist": "GV.PO-01", "sama": "3.1.1", "status": "Equivalent"}

    Returns:
        DataFrame with resolved titles per framework and mapping status
    """
    # TODO: For each rule, look up control_title in each DataFrame by control_id
    # TODO: Handle missing mappings (status = "Gap") when a rule leaves a field blank
    # TODO: Assemble into a single crosswalk DataFrame
    pass


def find_gaps(crosswalk_df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify controls present in one framework but unmapped in others.

    Returns:
        DataFrame filtered to rows where status == 'Gap'
    """
    # TODO: Filter crosswalk_df for gap rows
    pass


if __name__ == "__main__":
    # TODO: Call load_catalog() for each normalized CSV
    # TODO: Define mapping_rules list covering policy, vulnerability mgmt,
    #       monitoring, and incident management controls
    # TODO: Call build_mapping() and find_gaps()
    # TODO: Save results to ~/crosswalk-lab/output/crosswalk.csv
    print("Crosswalk build script - complete the TODOs")
```

**Run it once implemented:**

```bash
cd ~/crosswalk-lab/scripts
python3 build_crosswalk.py
```

---

## 📎 Task 4: Validate Mappings with Evidence Requirements

Create `~/crosswalk-lab/data/evidence_requirements.csv`:

```csv
mapping_status,control_theme,required_evidence
Equivalent,Policy,Approved policy document with review date
Equivalent,Vulnerability Management,Scan reports and remediation tickets
Equivalent,Monitoring,SIEM logs or monitoring dashboard screenshots
Gap,Incident Management,Manual process documentation pending automation
```

**📝 TODO:** Write a short Python snippet (append to `build_crosswalk.py` or new script `validate_evidence.py`) that merges `crosswalk.csv` with `evidence_requirements.csv` on `control_theme`, flagging any mapped control missing a corresponding evidence entry.

---

## 📈 Task 5: Generate Stakeholder Report

Create `~/crosswalk-lab/scripts/generate_report.py`:

```python
import pandas as pd

def generate_report(crosswalk_csv: str, output_path: str) -> None:
    """
    Generate a summary report (Markdown or HTML) from the crosswalk CSV.

    Args:
        crosswalk_csv: path to crosswalk.csv
        output_path: path to write report (e.g., output/crosswalk_report.md)
    """
    # TODO: Load crosswalk CSV
    # TODO: Compute summary counts: total mapped, equivalent, gaps
    # TODO: Group by category/theme for a breakdown table
    # TODO: Write Markdown report with summary + full table
    pass


if __name__ == "__main__":
    generate_report(
        "../output/crosswalk.csv",
        "../output/crosswalk_report.md"
    )
```

**Run:**

```bash
cd ~/crosswalk-lab/scripts
python3 generate_report.py
cat ../output/crosswalk_report.md
```

---

## ✅ Verification

Confirm lab completion on the same machine:

```bash
# Check normalized data exists
ls ~/crosswalk-lab/data/normalized_*.csv

# Check crosswalk output was generated
test -f ~/crosswalk-lab/output/crosswalk.csv && echo "Crosswalk PASS" || echo "Crosswalk FAIL"

# Check report exists and has content
wc -l ~/crosswalk-lab/output/crosswalk_report.md
```

**Expected outcomes:**

- `crosswalk.csv` contains rows linking ISO, NIST, and SAMA controls with a status column
- At least one row has status `Gap`
- `crosswalk_report.md` displays summary statistics and a mapping table

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| 📘 ISO 27001 Annex A | The reference set of information security controls organized by domain |
| 📗 NIST CSF 2.0 | The Cybersecurity Framework's Functions (Govern, Identify, Detect, Respond, etc.) and Categories |
| 🟩 SAMA CSF | The Saudi Central Bank's Cyber Security Framework, organized by principle |
| 🔗 Crosswalk Mapping | Linking equivalent controls across frameworks to show where requirements overlap |
| 🕳️ Coverage Gap | A control present in one framework with no equivalent mapped in another |
| 🧹 OpenRefine | An open-source tool for cleaning and reconciling messy tabular data |

---

## 🔧 Troubleshooting Tips

<details>
<summary>Click to expand common issues and fixes</summary>

- **OpenRefine not accessible:** verify with `ps aux | grep refine` and restart with `./refine -p 3333 &`
- **pandas `KeyError` on column names:** confirm normalized CSV headers match exactly (`control_id`, `control_title`, `category`)
- **Empty crosswalk output:** check `mapping_rules` list is populated before calling `build_mapping()`

</details>

---

## 🏁 Conclusion

In this lab, you built a working multi-framework crosswalk pipeline on a single Linux machine.

### 🎯 Key Accomplishments
- Normalized ISO 27001, NIST CSF 2.0, and SAMA CSF control catalogs using OpenRefine
- Implemented Python-based mapping logic to identify equivalent controls and gaps
- Validated mappings against evidence requirements
- Produced a stakeholder-facing crosswalk report

### 🌍 Real-World Applications
These skills directly support **CGRC Domain 1** competencies for compliance officers and GRC managers operating across multi-jurisdictional regulatory environments in the GCC region.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
