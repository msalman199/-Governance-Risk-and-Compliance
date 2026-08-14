# 🛡️ GCC Regulatory Mapping 

### NCA ECC • SAMA CSF • NESA/SIA • Qatar NIA → NIST 800-53 • ISO 27001

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)](https://www.postgresql.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM%2FDB-FCA121?style=for-the-badge)](https://www.sqlalchemy.org/)
[![NIST](https://img.shields.io/badge/NIST-SP%20800--53-003B71?style=for-the-badge)](https://www.nist.gov/)
[![ISO 27001](https://img.shields.io/badge/ISO-27001-005B96?style=for-the-badge)](https://www.iso.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)](https://ubuntu.com/)

> 🚀 **Hands-on GRC Engineering Lab**
> Build a normalized GCC regulatory control database, engineer NIST/ISO crosswalks, detect GCC-specific overlays, and generate a regional applicability matrix for continuous compliance monitoring.

---

## 🌟 Project Overview

This lab teaches you how to engineer a **multi-framework regulatory mapping platform** for GCC cybersecurity and compliance requirements.

### 🌍 Regulatory Frameworks

| 🇸🇦 Framework     | 🌍 Jurisdiction | 🎯 Purpose                          |
| ------------------ | --------------- | ----------------------------------- |
| **NCA ECC 2-2024** | Saudi Arabia    | Essential Cybersecurity Controls    |
| **SAMA CSF v2.0**  | Saudi Arabia    | Cybersecurity Framework             |
| **NESA/SIA**       | UAE             | National cybersecurity requirements |
| **Qatar NIA v2.0** | Qatar           | National Information Assurance      |

### 🔗 Reference Frameworks

```text
GCC Regulatory Controls
          │
          ▼
 ┌──────────────────────┐
 │   Crosswalk Engine   │
 └──────────┬───────────┘
            │
      ┌─────┴─────┐
      ▼           ▼
 NIST 800-53   ISO 27001
```

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 🗄️ Design a normalized relational GRC database.
* 📥 Build a regulatory-control ETL pipeline.
* 🔗 Create many-to-many cross-framework mappings.
* 🤖 Generate automated mapping candidates.
* 👨‍💼 Implement analyst validation of mappings.
* 🏷️ Detect GCC-specific regulatory overlays.
* 📊 Build a regional applicability matrix.
* 🔍 Perform compliance data-quality checks.
* 📈 Support CGRC Domain 6 continuous monitoring.
* 🛡️ Identify controls that have no direct NIST/ISO equivalent.

---

# 🧰 Technology Stack

## 💻 Core Technologies

| Technology          | Role                                 |
| ------------------- | ------------------------------------ |
| 🐍 **Python 3.10+** | ETL, automation, similarity analysis |
| 🐘 **PostgreSQL**   | Primary GRC database                 |
| 🐼 **Pandas**       | Data transformation and reporting    |
| 🔌 **SQLAlchemy**   | Python database abstraction          |
| 🧩 **psycopg2**     | PostgreSQL connectivity              |
| 📗 **openpyxl**     | Excel report generation              |
| 🐧 **Linux**        | Lab environment                      |
| 🗃️ **SQLite**      | Optional lightweight testing         |

---

# 📋 Prerequisites

Before starting, make sure you have:

* 🟢 Strong SQL knowledge.
* 🟢 Python 3.10+ experience.
* 🟢 Knowledge of NIST SP 800-53.
* 🟢 Knowledge of ISO/IEC 27001.
* 🟢 Understanding of GRC concepts.
* 🟢 Understanding of control inheritance.
* 🟢 Understanding of overlays and compensating controls.
* 🟢 Familiarity with CSV data.
* 🟢 Basic understanding of CGRC Domain 6.

---



---

# 🚀 STEP 0 — Environment Setup

### 🟢 Objective

Prepare the Linux environment and install all required dependencies.

### 🔧 Install Packages

```bash
sudo apt update

sudo apt install -y \
    postgresql \
    postgresql-contrib \
    python3-pip \
    sqlite3
```

### 🐍 Install Python Dependencies

```bash
pip3 install \
    pandas \
    psycopg2-binary \
    sqlalchemy \
    openpyxl
```

### 🐘 Start PostgreSQL

```bash
sudo systemctl enable --now postgresql
```

### 🗄️ Create Database

```bash
sudo -u postgres createdb gcc_grc_map
```

### 📁 Create Project

```bash
mkdir -p ~/gcc-lab/{data,scripts,sql,output}

cd ~/gcc-lab
```

### ✅ Verification

```bash
psql -d gcc_grc_map -c "SELECT version();"
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 0 COMPLETE                  ║
║  PostgreSQL + Python environment OK  ║
╚══════════════════════════════════════╝
```

---

# 🗄️ STEP 1 — Build the GRC Database

### 🔵 Objective

Create a normalized database capable of storing multiple regulatory frameworks and versions.

---

## 🧱 Required Tables

### 1️⃣ `frameworks`

```text
id
name
version
jurisdiction
authority
```

### 2️⃣ `controls`

```text
id
framework_id
control_ref
domain
title
description
control_type
```

### 3️⃣ `crosswalks`

```text
id
source_control_id
target_control_id
mapping_strength
rationale
```

### 4️⃣ `overlays`

```text
id
name
description
trigger_condition
```

### 5️⃣ `control_overlays`

```text
control_id
overlay_id
```

---

## 🔐 Database Design Rules

### 🔗 Many-to-Many Mapping

A single GCC control can map to:

```text
GCC Control A
     │
     ├──── NIST AC-2
     ├──── NIST AC-3
     └──── ISO A.5.15
```

Therefore, mappings belong in a junction table.

Prevent duplicate relationships:

```sql
UNIQUE (source_control_id, target_control_id)
```

---

## 🕐 Framework Versioning

Never overwrite an old framework version.

Example:

```text
NCA ECC 1-2018
       │
       └── Historical version

NCA ECC 2-2024
       │
       └── Current version
```

This allows historical assessments and mapping comparisons.

---

## 🟡 Orphan Controls

If no NIST or ISO equivalent exists:

```text
GCC Control
     │
     └── ❌ No equivalent
```

Do **not** create a fake mapping.

An unmapped control is valuable information because it may represent a GCC-specific regulatory requirement.

---

## ⚡ Database Performance

Add indexes to:

```text
controls.framework_id
controls.control_ref
crosswalks.source_control_id
crosswalks.target_control_id
control_overlays.control_id
control_overlays.overlay_id
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 1 COMPLETE                  ║
║  Normalized GRC schema created       ║
╚══════════════════════════════════════╝
```

---

# 📥 STEP 2 — Load Regulatory Catalogs

### 🟢 Objective

Import heterogeneous CSV catalogs into PostgreSQL.

Each CSV should contain:

```text
control_id,domain,title,description,control_type
```

Example:

```csv
control_id,domain,title,description,control_type
LOG-01,Logging and Monitoring,Security Logging,Organizations shall maintain security event logs,Preventive
```

---

## 🐍 Create ETL Script

Create:

```text
scripts/load_controls.py
```

Core function:

```python
def load_framework_csv(
    csv_path: str,
    framework_name: str,
    engine
) -> int:
    """
    Load and validate one regulatory catalog.
    """
    pass
```

Validation should detect:

* ❌ Missing control IDs.
* ❌ Missing titles.
* ❌ Missing descriptions.
* ❌ Missing domains.
* ❌ Duplicate control IDs.
* ❌ Invalid framework names.

---

## 🔍 Integrity Function

```python
def validate_catalog_integrity(engine) -> dict:
    """
    Return data-quality statistics.
    """
    pass
```

---

## 📊 Expected Catalogs

```text
🇸🇦 NCA ECC
🇸🇦 SAMA CSF
🇦🇪 NESA/SIA
🇶🇦 Qatar NIA
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 2 COMPLETE                  ║
║  Regulatory catalogs successfully    ║
║  loaded into PostgreSQL              ║
╚══════════════════════════════════════╝
```

---

# 🔗 STEP 3 — Build the Crosswalk Engine

### 🔵 Objective

Map GCC regulatory controls to:

* 🟦 NIST SP 800-53 Rev. 5
* 🟩 ISO/IEC 27001:2022

---

## 🧠 Mapping Philosophy

**Never assume 1:1 equivalence.**

One GCC control may map to multiple reference controls.

```text
             GCC CONTROL
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      NIST      NIST       ISO
      AC-2      AU-2       A.5.15
```

---

## 🏷️ Mapping Strength

Use:

```text
🟢 EXACT
🟡 PARTIAL
🔵 RELATED
```

### 🟢 Exact

Essentially the same objective and requirement.

### 🟡 Partial

Significant overlap, but one control has additional requirements.

### 🔵 Related

Similar security objective but not equivalent.

---

# 🤖 STEP 4 — Generate Mapping Candidates

Create:

```text
scripts/crosswalk_engine.py
```

Example:

```python
from typing import Literal

MappingStrength = Literal[
    "exact",
    "partial",
    "related"
]

def generate_crosswalk_candidates(
    gcc_control_id: int,
    reference_framework: str,
    engine
) -> list[dict]:
    """
    Generate candidate mappings.
    """
    pass
```

---

## 🧮 Recommended Similarity Model

Use a hybrid approach:

```text
Domain Similarity
       +
Keyword Similarity
       +
TF-IDF
       +
Analyst Review
       =
Final Mapping
```

### Why?

Regulatory controls are often short and jargon-heavy.

Pure fuzzy matching can produce misleading matches.

TF-IDF provides useful lexical similarity, while domain and keyword matching add regulatory context.

---

## 👨‍💼 Analyst Approval

Automated matching should only generate candidates.

Final mappings require human review:

```text
🤖 Candidate
      ↓
📊 Similarity Score
      ↓
👨‍💼 Analyst Review
      ↓
🟢 Exact
🟡 Partial
🔵 Related
❌ Rejected
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 4 COMPLETE                  ║
║  Crosswalk candidates generated     ║
╚══════════════════════════════════════╝
```

---

# 🏷️ STEP 5 — GCC Regulatory Overlay Detection

### 🟣 Objective

Identify GCC-specific requirements that may not have a direct NIST/ISO equivalent.

---

## Required Overlays

### 🗺️ 1. Data Residency

Tag controls mentioning:

```text
data residency
in-country storage
local data
within the Kingdom
domestic storage
```

---

### 🕌 2. Arabic Logging

Tag requirements involving:

```text
Arabic-language logs
Arabic audit records
local-language logging
Arabic-readable records
```

---

### 🚨 3. National CERT Reporting

Detect:

```text
national CERT
government notification
cybersecurity authority
incident notification
mandatory reporting
```

---

### 🏢 4. Local Hosting

Detect:

```text
local hosting
in-country hosting
domestic infrastructure
local cloud
locally hosted systems
```

---

# 🔎 STEP 6 — Implement Overlay Detection

Create:

```text
scripts/overlay_detection.py
```

Function:

```python
def detect_overlay_requirements(
    control_description: str
) -> list[str]:
    """
    Detect GCC-specific overlay requirements.
    """
    pass
```

Then:

```python
def tag_controls_with_overlays(engine) -> int:
    """
    Apply overlay detection to all controls.
    """
    pass
```

---

## 🧠 Detection Pipeline

```text
Raw Control
     │
     ▼
Normalize Text
     │
     ▼
Regex / Keyword Detection
     │
     ▼
Overlay Classification
     │
     ▼
control_overlays
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 6 COMPLETE                  ║
║  GCC overlays detected and tagged   ║
╚══════════════════════════════════════╝
```

---

# 📊 STEP 7 — Generate Regional Applicability Matrix

### 🟢 Objective

Create a consolidated compliance matrix across all frameworks.

Create:

```text
scripts/generate_matrix.py
```

---

## 📋 Matrix Example

| Domain               | 🇸🇦 NCA | 🇸🇦 SAMA | 🇦🇪 NESA | 🇶🇦 NIA | 🟦 NIST | 🟩 ISO | 🗺️ Residency | 🕌 Arabic Logs | 🚨 CERT | 🏢 Hosting |
| -------------------- | -------- | --------- | --------- | -------- | ------- | ------ | ------------- | -------------- | ------- | ---------- |
| Logging & Monitoring | ✅        | ✅         | ✅         | ✅        | ✅       | ✅      | ❌             | ✅              | ✅       | ❌          |
| Access Control       | ✅        | ✅         | ✅         | ✅        | ✅       | ✅      | ❌             | ❌              | ❌       | ❌          |
| Incident Response    | ✅        | ✅         | ✅         | ✅        | 🟡      | ✅      | ❌             | ❌              | ✅       | ❌          |

---

## 📤 Excel Export

The report should be generated as:

```text
~/gcc-lab/output/applicability_matrix.xlsx
```

Function:

```python
def build_applicability_matrix(
    engine,
    output_path: str
) -> None:
    """
    Build and export the regional matrix.
    """
    pass
```

### 🎉 Success Indicator

```text
╔══════════════════════════════════════╗
║  ✅ STEP 7 COMPLETE                  ║
║  Regional matrix exported to Excel  ║
╚══════════════════════════════════════╝
```

---

# 🔍 STEP 8 — Verification & Quality Assurance

### 🛡️ Objective

Confirm that the database, mappings, overlays, and report are working correctly.

---

## 1️⃣ Framework Counts

```bash
psql -d gcc_grc_map -c \
"SELECT name, COUNT(*)
 FROM frameworks f
 JOIN controls c ON f.id=c.framework_id
 GROUP BY name;"
```

### Expected

```text
NCA ECC       → > 0
SAMA CSF      → > 0
NESA/SIA      → > 0
Qatar NIA     → > 0
```

---

## 2️⃣ Mapping Strengths

```bash
psql -d gcc_grc_map -c \
"SELECT mapping_strength, COUNT(*)
 FROM crosswalks
 GROUP BY mapping_strength;"
```

Expected:

```text
🟢 exact
🟡 partial
🔵 related
```

---

## 3️⃣ Overlay Coverage

```bash
psql -d gcc_grc_map -c \
"SELECT o.name, COUNT(*)
 FROM control_overlays co
 JOIN overlays o ON co.overlay_id=o.id
 GROUP BY o.name;"
```

Expected:

```text
🗺️ data_residency          → > 0
🕌 arabic_logging          → > 0
🚨 national_cert_reporting → > 0
🏢 local_hosting_mandate   → > 0
```

---

## 4️⃣ Verify Excel Report

```bash
ls -la ~/gcc-lab/output/applicability_matrix.xlsx
```

### 🎉 Final Success Indicator

```text
╔════════════════════════════════════════════════════╗
║                                                    ║
║       🏆 GCC REGULATORY MAPPING LAB COMPLETE       ║
║                                                    ║
║  🗄️ Database       → READY                         ║
║  📥 ETL Pipeline   → READY                         ║
║  🔗 Crosswalk      → READY                         ║
║  🏷️ Overlays       → READY                         ║
║  📊 Matrix         → READY                         ║
║  🛡️ CGRC Domain 6  → SUPPORTED                     ║
║                                                    ║
╚════════════════════════════════════════════════════╝
```

---

# 🧪 Advanced Quality Checks

## 🔍 Find Orphan Controls

```sql
SELECT
    c.control_ref,
    f.name
FROM controls c
JOIN frameworks f
    ON f.id = c.framework_id
LEFT JOIN crosswalks cw
    ON cw.source_control_id = c.id
WHERE cw.id IS NULL;
```

---

## 🔍 Find Duplicate Controls

```sql
SELECT
    framework_id,
    control_ref,
    COUNT(*)
FROM controls
GROUP BY framework_id, control_ref
HAVING COUNT(*) > 1;
```

---

## 🔍 Find Missing Domains

```sql
SELECT *
FROM controls
WHERE domain IS NULL
   OR TRIM(domain) = '';
```

---

# 🏗️ Final Architecture

```text
                    🌍 GCC REGULATORS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       🇸🇦 NCA           🇸🇦 SAMA         🇦🇪 NESA
          │                │                │
          └────────────────┼────────────────┘
                           │
                       🇶🇦 Qatar NIA
                           │
                           ▼
                  📥 ETL PIPELINE
                           │
                           ▼
                  🐘 PostgreSQL
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        🔗 Crosswalk Engine       🏷️ Overlay Engine
              │                         │
       ┌──────┴──────┐          ┌───────┼────────┐
       ▼             ▼          ▼       ▼        ▼
   🟦 NIST       🟩 ISO       🗺️ Data  🕌 Arabic 🚨 CERT
   800-53       27001        Residency Logging Reporting
              │
              ▼
       📊 Applicability Matrix
              │
              ▼
       🛡️ CGRC DOMAIN 6
       Continuous Monitoring
```

---

# 🎓 Skills Demonstrated

By completing this project, you demonstrate practical experience in:

```text
🗄️ Database Engineering
        ↓
📥 Regulatory ETL
        ↓
🔗 Control Crosswalking
        ↓
🤖 Similarity Analysis
        ↓
🏷️ Regulatory Overlay Detection
        ↓
📊 Compliance Reporting
        ↓
🛡️ Continuous Monitoring
```

---

# ⚠️ Compliance Disclaimer

This lab is designed for **education, GRC engineering practice, and technical demonstration**.

The sample mappings and overlay detection logic must **not** be treated as authoritative regulatory interpretations.

For production compliance work:

* Verify requirements against official regulator publications.
* Preserve framework versions.
* Record effective and retirement dates.
* Maintain mapping rationale.
* Require analyst approval for regulatory mappings.
* Maintain an audit trail.
* Periodically review regulatory changes.
* Consider sector-specific applicability.
* Validate jurisdiction-specific requirements with qualified compliance professionals.

---

# 🏆 Conclusion

You have built the foundation of a **GCC-focused regulatory intelligence and compliance mapping platform**.

The completed solution demonstrates:

> **Regulatory Data → Normalization → Crosswalk → Overlay Detection → Applicability Matrix → Continuous Monitoring**

This architecture can be extended into a production GRC platform with:

* 🔄 Regulatory change monitoring
* 🤖 AI-assisted control mapping
* 📑 Evidence management
* 👨‍💼 Analyst approval workflows
* 📈 Compliance dashboards
* 🔐 Control inheritance
* 🧩 Compensating controls
* 🌐 REST APIs
* 🏢 Multi-tenant GRC architecture
* 📊 Automated compliance-gap reporting

## 🚀 Final Project Status

```text
╔════════════════════════════════════════════════════╗
║                                                    ║
║           🛡️ GCC GRC MAPPING PLATFORM              ║
║                                                    ║
║              ██████████████████████                ║
║              █   LAB COMPLETE   █                  ║
║              ██████████████████████                ║
║                                                    ║
║   🇸🇦 NCA ECC     ✅                               ║
║   🇸🇦 SAMA CSF    ✅                               ║
║   🇦🇪 NESA/SIA    ✅                               ║
║   🇶🇦 Qatar NIA   ✅                               ║
║   🟦 NIST 800-53  ✅                               ║
║   🟩 ISO 27001    ✅                               ║
║   🏷️ Overlays     ✅                               ║
║   📊 Matrix       ✅                               ║
║                                                    ║
╚════════════════════════════════════════════════════╝
```

**🎯 Outcome:** A practical GCC regulatory mapping lab aligned with **GRC engineering, regulatory crosswalking, and CGRC Domain 6 continuous monitoring**.
