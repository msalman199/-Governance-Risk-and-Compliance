<div align="center">

# 🤝 Third-Party Risk Management Program Build

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![LimeSurvey](https://img.shields.io/badge/LimeSurvey-PHP-1D3557?style=for-the-badge&logo=php&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-Database-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Dashboard-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NIST SP 800-161](https://img.shields.io/badge/NIST%20800--161-ISO%2027036-002F6C?style=for-the-badge&logo=nist&logoColor=white)

*Deploy a vendor questionnaire, score inherent risk, and stand up an ongoing TPRM oversight program*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🧩 Task 1: Install LimeSurvey (Vendor Questionnaire Platform)](#-task-1-install-limesurvey-vendor-questionnaire-platform)
- [📝 Task 2: Build the Vendor Due Diligence Questionnaire](#-task-2-build-the-vendor-due-diligence-questionnaire)
- [📊 Task 3: Score Responses and Tier Vendors](#-task-3-score-responses-and-tier-vendors)
- [📅 Task 4: Define Monitoring Cadence and KRIs](#-task-4-define-monitoring-cadence-and-kris)
- [📈 Task 5: Build TPRM Dashboard and Exception Register](#-task-5-build-tprm-dashboard-and-exception-register)
- [✅ Verification](#-verification)
- [🗝️ Key Concepts](#️-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By completing this lab, you will:

| # | Objective |
|---|---|
| 1 | Deploy a self-hosted survey platform to support vendor risk assessments |
| 2 | Build a vendor due diligence questionnaire mapped to ISO 27036 and NIST SP 800-161 |
| 3 | Score vendor responses and assign inherent risk tiers |
| 4 | Define a monitoring cadence and Key Risk Indicators (KRIs) for ongoing oversight |
| 5 | Produce a TPRM dashboard and exception register using open-source tools |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🐧 Linux CLI | Basic command-line familiarity (`apt`, `systemctl`, file editing) |
| 🗄️ SQL/Spreadsheets | Basic understanding of SQL and spreadsheet formulas |
| 🔄 TPRM Lifecycle | Conceptual knowledge of onboarding, due diligence, monitoring, offboarding |
| 📖 Frameworks | Familiarity with SP 800-161 (supply chain risk, tiering) and ISO 27036 (supplier relationship security) |

## 🖥️ Environment Setup

> **Lab Environment:** A single Linux machine (Ubuntu 22.04 LTS) provided via **Start Lab**. Root or sudo access and internet access for package installation required.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y apache2 mariadb-server php php-mysql php-gd php-curl php-mbstring php-xml php-zip unzip wget  # 📦 core stack
sudo systemctl enable --now apache2 mariadb  # 🚀 start services
```

---

## 🧩 Task 1: Install LimeSurvey (Vendor Questionnaire Platform)

### 1️⃣ Secure MariaDB and create the LimeSurvey database

```bash
sudo mysql_secure_installation  # 🔐 harden MariaDB
sudo mysql -u root -p <<'EOF'
CREATE DATABASE limesurvey CHARACTER SET utf8mb4;
CREATE USER 'lsuser'@'localhost' IDENTIFIED BY 'ChangeMe123!';
GRANT ALL PRIVILEGES ON limesurvey.* TO 'lsuser'@'localhost';
FLUSH PRIVILEGES;
EOF
```

### 2️⃣ Download and extract LimeSurvey into the web root

```bash
cd /tmp
wget https://download.limesurvey.org/latest-stable-release/limesurvey5xx.tar.gz -O limesurvey.tar.gz  # ⬇️ fetch release
sudo tar -xzf limesurvey.tar.gz -C /var/www/html/                                                        # 📦 extract
sudo chown -R www-data:www-data /var/www/html/limesurvey                                                 # 👤 ownership
```

### 3️⃣ Configure Apache to serve LimeSurvey

```bash
sudo bash -c 'cat > /etc/apache2/sites-available/limesurvey.conf' <<'EOF'
<VirtualHost *:80>
    DocumentRoot /var/www/html/limesurvey
    <Directory /var/www/html/limesurvey>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOF
sudo a2ensite limesurvey.conf
sudo a2enmod rewrite
sudo systemctl reload apache2  # 🔄 apply config
```

Open `http://<lab-machine-ip>/` in a browser and complete the installation wizard using the database credentials above.

> **✅ Checkpoint:** Log into the LimeSurvey admin panel before proceeding.

---

## 📝 Task 2: Build the Vendor Due Diligence Questionnaire

Map questionnaire sections to control domains. Create a new survey named **Vendor Due Diligence Assessment** and add question groups:

| Group | Framework Mapping | Sample Question |
|---|---|---|
| Governance | SP 800-161 (Risk Mgmt) | Does the vendor have a documented supply chain risk policy? |
| Access & Data Handling | ISO 27036-3 | Does the vendor encrypt data at rest and in transit? |
| Incident Response | SP 800-161 (C-SCRM) | Does the vendor have a tested IR plan with notification SLAs? |
| Subcontractor Management | ISO 27036-2 | Does the vendor disclose and vet fourth parties? |
| Business Continuity | SP 800-161 | Is there a tested BCP/DR plan reviewed annually? |

For each question, configure a 5-point Likert or Yes/No/Partial answer type, and assign a numeric equivalent (0-4) for scoring.

**📌 Task:** Add at least 3 questions per group (15 total minimum). Export the survey structure as an `.lss` file for version control.

```bash
# TODO: Locate exported .lss file and move it to a working directory
mkdir -p ~/tprm-lab/questionnaires
# TODO: mv <exported_file>.lss ~/tprm-lab/questionnaires/
```

---

## 📊 Task 3: Score Responses and Tier Vendors

Export survey responses as CSV from LimeSurvey (**Responses > Export > CSV**), then complete the scoring script.

```python
import csv

def load_responses(csv_file: str) -> list:
    """
    Load vendor survey responses from a CSV export.

    Args:
        csv_file: Path to the LimeSurvey CSV export

    Returns:
        List of dictionaries, one per vendor response row
    """
    # TODO: Open file with csv.DictReader
    # TODO: Return list of row dicts
    pass

def score_vendor(response: dict, weight_map: dict) -> float:
    """
    Calculate a weighted inherent risk score for one vendor.

    Args:
        response: Dict of question_code -> numeric answer (0-4)
        weight_map: Dict of question_code -> weight (e.g. 1.0-3.0)

    Returns:
        Weighted average score (0-4 scale)
    """
    # TODO: Multiply each answer by its weight
    # TODO: Sum weighted scores and divide by sum of weights
    pass

def tier_vendor(score: float) -> str:
    """
    Assign a risk tier based on score.

    Args:
        score: Weighted vendor score (0-4)

    Returns:
        One of "Critical", "High", "Medium", "Low"
    """
    # TODO: Define thresholds, e.g.
    # score < 1.0 -> Critical (inverted: low control maturity = high risk)
    # 1.0-2.0 -> High
    # 2.0-3.0 -> Medium
    # >3.0 -> Low
    pass
```

- Define your own `weight_map` reflecting criticality (e.g., Incident Response weighted higher than Governance)
- Run the script against the exported CSV and output a `vendor_scores.csv` with columns: `vendor_name, score, tier`

---

## 📅 Task 4: Define Monitoring Cadence and KRIs

Create a file `~/tprm-lab/monitoring_plan.md` defining cadence by tier:

| Tier | Reassessment Cadence | Sample KRIs |
|---|---|---|
| Critical | Quarterly | Open critical findings, SLA breach count, security incidents involving vendor |
| High | Semi-annual | Days since last pen test, contract renewal risk flags |
| Medium | Annual | Certification expiry (ISO 27001/SOC 2), overdue questionnaire renewals |
| Low | Biennial | Self-attestation completion rate |

**📌 Task:** Add at least 2 KRIs per tier with a defined data source (e.g., "pulled from vendor's SOC 2 report" or "tracked in exception register").

---

## 📈 Task 5: Build TPRM Dashboard and Exception Register

Use SQLite for a lightweight local dashboard backend.

```bash
sudo apt install -y sqlite3  # 📦 install SQLite
sqlite3 ~/tprm-lab/tprm.db <<'EOF'
CREATE TABLE vendors (
  id INTEGER PRIMARY KEY,
  name TEXT,
  tier TEXT,
  score REAL,
  last_assessed DATE,
  next_review DATE
);
CREATE TABLE exceptions (
  id INTEGER PRIMARY KEY,
  vendor_id INTEGER,
  control_gap TEXT,
  risk_rating TEXT,
  compensating_control TEXT,
  approved_by TEXT,
  expiry_date DATE,
  FOREIGN KEY(vendor_id) REFERENCES vendors(id)
);
EOF
```

**Complete the import script to load `vendor_scores.csv` into the `vendors` table:**

```python
import sqlite3
import csv

def import_vendors(db_path: str, csv_path: str) -> int:
    """
    Load scored vendors into the SQLite dashboard database.

    Args:
        db_path: Path to tprm.db
        csv_path: Path to vendor_scores.csv

    Returns:
        Count of rows inserted
    """
    # TODO: Connect to SQLite database
    # TODO: Read CSV rows and INSERT into vendors table
    # TODO: Commit and close connection
    # TODO: Return number of rows inserted
    pass
```

- Populate the `exceptions` table manually with at least 2 sample entries (e.g., a Critical vendor lacking MFA, with a compensating control noted)
- Query a summary view:

```sql
SELECT tier, COUNT(*) AS vendor_count, AVG(score) AS avg_score
FROM vendors
GROUP BY tier;
```

---

## ✅ Verification

Confirm the following on your lab machine:

```bash
systemctl is-active apache2 mariadb
curl -I http://localhost/limesurvey | head -n 1
sqlite3 ~/tprm-lab/tprm.db "SELECT COUNT(*) FROM vendors;"
sqlite3 ~/tprm-lab/tprm.db "SELECT COUNT(*) FROM exceptions;"
ls ~/tprm-lab/questionnaires/*.lss
```

**Expected results:**

- Apache and MariaDB report active
- LimeSurvey returns HTTP 200
- `vendors` table contains rows matching your questionnaire respondents
- `exceptions` table contains at least 2 entries
- `.lss` questionnaire file exists

<details>
<summary>🛠️ Troubleshooting</summary>

- **LimeSurvey install wizard fails to connect to DB:** verify `lsuser` credentials and that `mysql.sock` is accessible
- **Apache shows default page instead of LimeSurvey:** confirm `a2ensite limesurvey.conf` ran and `a2dissite 000-default` if needed
- **CSV import script fails on encoding:** open LimeSurvey export settings and select UTF-8 CSV format

</details>

---

## 🗝️ Key Concepts

| Concept | Description |
|---|---|
| 🤝 TPRM | Third-Party Risk Management — the lifecycle of onboarding, assessing, monitoring, and offboarding vendors |
| 📝 Due Diligence Questionnaire | A structured survey mapped to control frameworks used to assess vendor security posture |
| 📊 Inherent Risk Tiering | Scoring vendor responses to assign a risk tier (Critical/High/Medium/Low) |
| 📅 KRI | Key Risk Indicator — a measurable signal used to monitor risk between full reassessments |
| 📋 Exception Register | A tracked log of accepted control gaps with compensating controls and approval/expiry |

---

## 🏁 Conclusion

In this lab, you built a functional third-party risk management workflow on a single Linux machine. You deployed LimeSurvey as a self-hosted vendor questionnaire platform, designed due diligence questions mapped to ISO 27036 and SP 800-161 control domains, and implemented Python scoring logic to tier vendors by inherent risk. You then defined a monitoring cadence with tier-based KRIs and built a lightweight SQLite-backed dashboard and exception register to track ongoing oversight. These artifacts mirror real-world CGRC Domain 1 practices for establishing and operating a defensible TPRM program.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
