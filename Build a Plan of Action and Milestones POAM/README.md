<div align="center">

# 📋 Build a Plan of Action and Milestones (POA&M)

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Redmine](https://img.shields.io/badge/Redmine-5.1.1-B32024?style=for-the-badge&logo=redmine&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![OSCAL](https://img.shields.io/badge/OSCAL-JSON-1E3A8A?style=for-the-badge&logo=json&logoColor=white)
![NIST RMF](https://img.shields.io/badge/NIST-RMF-002F6C?style=for-the-badge&logo=nist&logoColor=white)

*Convert Security Assessment Report findings into a fully tracked, exportable POA&M*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🧩 Task 1: Install and Configure Redmine](#-task-1-install-and-configure-redmine-lightweight-ticketing)
- [📥 Task 2: Import SAR Findings as Structured Tickets](#-task-2-import-sar-findings-as-structured-tickets)
- [🗂️ Task 3: Assign Owners, Milestones, Severity, and Target Dates](#️-task-3-assign-owners-milestones-severity-and-target-dates)
- [⚖️ Task 4: Track Risk Acceptance and Residual Risk](#️-task-4-track-risk-acceptance-and-residual-risk)
- [📤 Task 5: Export POA&M in OSCAL Format](#-task-5-export-poam-in-oscal-format)
- [✅ Verification](#-verification)
- [🗝️ Key Concepts](#️-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|---|
| 1 | Deploy a lightweight ticketing system to track remediation findings |
| 2 | Convert Security Assessment Report (SAR) findings into structured, trackable tickets |
| 3 | Assign ownership, severity, milestones, and target close dates to findings |
| 4 | Document risk acceptance decisions and residual risk levels |
| 5 | Export a POA&M report in OSCAL-compliant JSON format |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🐧 Linux CLI | Basic command-line familiarity (package management, file editing) |
| 📊 Severity Ratings | Understanding of vulnerability/finding severity ratings (Critical/High/Medium/Low) |
| 🏛️ NIST RMF | Conceptual knowledge of NIST RMF (Domain 5: Authorization, Domain 7: Continuous Monitoring) |
| 🎫 Redmine/OSCAL | No prior experience required |

## 🖥️ Environment Setup

> **Lab Environment:** Al Nafi provides a single Linux machine (Ubuntu 22.04) via **Start Lab**. All work is done locally — no external cloud accounts needed.

```bash
sudo apt update
sudo apt install -y ruby-full ruby-dev build-essential libmysqlclient-dev \
    sqlite3 libsqlite3-dev python3 python3-pip jq  # 📦 core toolchain

sudo gem install bundler  # 💎 Ruby dependency manager
```

---

## 🧩 Task 1: Install and Configure Redmine (Lightweight Ticketing)

### 1️⃣ Download and extract Redmine

```bash
cd /opt
sudo wget https://www.redmine.org/releases/redmine-5.1.1.tar.gz  # ⬇️ fetch release
sudo tar -xzf redmine-5.1.1.tar.gz                                 # 📦 extract
sudo mv redmine-5.1.1 redmine
cd redmine
```

### 2️⃣ Configure SQLite database (simplest option for single-machine lab)

```bash
sudo tee config/database.yml <<EOF
production:
  adapter: sqlite3
  database: db/redmine.sqlite3
EOF
```

### 3️⃣ Install dependencies and initialize

```bash
sudo bundle install --without development test    # 📥 install gems
sudo bundle exec rake generate_secret_token        # 🔐 secret token
RAILS_ENV=production sudo bundle exec rake db:migrate  # 🗄️ migrate schema
```

### 4️⃣ Start Redmine on port 3000

```bash
sudo bundle exec rails server webrick -e production -p 3000 -d  # 🚀 start server
```

**Verify:** Open a browser to `http://<lab-machine-ip>:3000`. Login with default `admin`/`admin`.

<details>
<summary>🛠️ Troubleshooting</summary>

If `bundle install` fails on gem versions, run `sudo gem update --system` first.

</details>

---

## 📥 Task 2: Import SAR Findings as Structured Tickets

### 1️⃣ Create a sample SAR findings file (simulating assessor output)

```bash
mkdir -p ~/poam-lab && cd ~/poam-lab
cat > sar_findings.json <<'EOF'
[
  {"id": "F-001", "title": "Unpatched OpenSSL vulnerability", "severity": "High", "control": "SI-2"},
  {"id": "F-002", "title": "Weak password policy enforcement", "severity": "Medium", "control": "IA-5"},
  {"id": "F-003", "title": "Missing audit log review", "severity": "Low", "control": "AU-6"}
]
EOF
```

### 2️⃣ Push findings into Redmine via its REST API

First, generate an API key in Redmine (**My Account > API access key**).

Complete the script template below:

```python
import json
import requests

REDMINE_URL = "http://localhost:3000"
API_KEY = "YOUR_API_KEY_HERE"
PROJECT_ID = "poam-project"  # 📁 create this project in Redmine UI first

def load_findings(filepath: str) -> list:
    """
    Load SAR findings from a JSON file.

    Args:
        filepath: Path to sar_findings.json

    Returns:
        List of finding dictionaries
    """
    # TODO: Open file, parse JSON, return list
    pass

def create_ticket(finding: dict) -> dict:
    """
    Create a Redmine issue from a single finding.

    Args:
        finding: dict with keys id, title, severity, control

    Returns:
        JSON response from Redmine API
    """
    headers = {"X-Redmine-API-Key": API_KEY, "Content-Type": "application/json"}
    payload = {
        "issue": {
            "project_id": PROJECT_ID,
            "subject": f"{finding['id']}: {finding['title']}",
            "description": f"Control: {finding['control']}\nSeverity: {finding['severity']}",
            # TODO: Map severity to Redmine priority_id (e.g., 1=Low, 2=Normal, 3=High, 4=Urgent)
        }
    }
    # TODO: POST to f"{REDMINE_URL}/issues.json", return response.json()
    pass

if __name__ == "__main__":
    findings = load_findings("sar_findings.json")
    for f in findings:
        result = create_ticket(f)
        print(f"Created ticket for {f['id']}")
```

### 3️⃣ Run the script and verify

```bash
python3 import_findings.py  # ▶️ push findings into Redmine
```

Confirm the tickets appear in the Redmine project UI.

---

## 🗂️ Task 3: Assign Owners, Milestones, Severity, and Target Dates

### 1️⃣ In the Redmine UI, open each imported ticket and set:

| Field | Value |
|---|---|
| 👤 Assignee | A designated owner (create sample users under **Administration > Users**) |
| 🏁 Target version/Milestone | Create milestones like `Q1-Remediation`, `Q2-Remediation` |
| 🔺 Priority | Already mapped from severity in Task 2 |
| 📅 Due date | Set based on severity (suggested SLA: High = 30 days, Medium = 60 days, Low = 90 days) |

### 2️⃣ Bulk-update due dates via the Redmine REST API

Complete this snippet:

```python
def update_ticket_dates(issue_id: int, due_date: str, assigned_to_id: int) -> None:
    """
    Update an existing Redmine issue with due date and assignee.

    Args:
        issue_id: Redmine issue ID
        due_date: Date string in YYYY-MM-DD format
        assigned_to_id: Redmine user ID
    """
    # TODO: Build PUT request to f"{REDMINE_URL}/issues/{issue_id}.json"
    # TODO: Include due_date and assigned_to_id in the issue payload
    # TODO: Send request with requests.put()
    pass
```

---

## ⚖️ Task 4: Track Risk Acceptance and Residual Risk

### 1️⃣ Add a custom field for risk decisions

**Administration > Custom Fields > Issues** → name it `Risk_Decision` with values: `Remediate`, `Risk Accepted`, `Transferred`.

### 2️⃣ Add a second custom field for residual risk

`Residual_Risk` (text field) — records the risk level remaining after mitigation.

### 3️⃣ Apply to finding F-003 (Low severity)

| Field | Value |
|---|---|
| Risk_Decision | `Risk Accepted` |
| Residual_Risk | `Low - accepted by ISSO, review in 12 months` |

### 4️⃣ Document the decision rationale in the ticket's notes/journal field

<details>
<summary>🛠️ Troubleshooting</summary>

Custom fields must be enabled per-tracker (**Administration > Trackers > Bug** → check `Risk_Decision`/`Residual_Risk`).

</details>

---

## 📤 Task 5: Export POA&M in OSCAL Format

### 1️⃣ Fetch all tickets via the API and transform into OSCAL structure

Complete the script:

```python
def fetch_all_issues(project_id: str) -> list:
    """
    Fetch all issues for the POA&M project from Redmine.

    Args:
        project_id: Redmine project identifier

    Returns:
        List of issue dictionaries from API response
    """
    # TODO: GET f"{REDMINE_URL}/issues.json?project_id={project_id}"
    # TODO: Return the 'issues' list from response JSON
    pass

def build_oscal_poam(issues: list) -> dict:
    """
    Convert Redmine issues into a minimal OSCAL POA&M JSON structure.

    Args:
        issues: List of issue dicts from Redmine

    Returns:
        Dictionary matching OSCAL plan-of-action-and-milestones schema (simplified)
    """
    poam_items = []
    for issue in issues:
        # TODO: Map each issue to an OSCAL poam-item:
        #   uuid, title, description, status (open/closed),
        #   remediation-tracking (due date), risk (severity)
        pass

    oscal_doc = {
        "plan-of-action-and-milestones": {
            "uuid": "GENERATE-A-UUID-HERE",
            "metadata": {"title": "Sample POA&M", "version": "1.0"},
            "poam-items": poam_items
        }
    }
    return oscal_doc

if __name__ == "__main__":
    issues = fetch_all_issues("poam-project")
    oscal_output = build_oscal_poam(issues)
    with open("poam_export.json", "w") as f:
        json.dump(oscal_output, f, indent=2)
    print("OSCAL POA&M exported to poam_export.json")
```

### 2️⃣ Validate the JSON structure

```bash
jq . poam_export.json | head -30  # 🔍 pretty-print + inspect
```

---

## ✅ Verification

Confirm lab completion by checking:

```bash
# 1. Redmine is running
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000

# 2. All 3 findings exist as tickets
curl -s -H "X-Redmine-API-Key: $API_KEY" \
  "http://localhost:3000/issues.json?project_id=poam-project" | jq '.issues | length'

# 3. OSCAL export file exists and is valid JSON
jq empty poam_export.json && echo "Valid JSON"

# 4. Confirm risk acceptance field is present
jq '.["plan-of-action-and-milestones"].["poam-items"][] | select(.title | contains("F-003"))' poam_export.json
```

**Expected results:** HTTP 200, 3 issues returned, valid JSON confirmation, and F-003 entry showing risk acceptance data.

---

## 🗝️ Key Concepts

| Concept | Description |
|---|---|
| 📋 POA&M | Plan of Action and Milestones — tracks identified findings through to remediation or formal risk acceptance |
| 📄 SAR | Security Assessment Report — the source of findings converted into trackable tickets |
| 🎫 Ticketing Automation | Using a REST API (Redmine) to programmatically create and update remediation tickets |
| ⚖️ Risk Acceptance | A formal decision to accept residual risk rather than remediate, with documented rationale |
| 📦 OSCAL | Open Security Controls Assessment Language — a standardized JSON/XML format for exchanging compliance artifacts |

---

## 🏁 Conclusion

In this lab, you built an end-to-end POA&M tracking workflow using open-source tools on a single Linux machine. You deployed Redmine as a lightweight ticketing system, imported SAR findings as structured tickets via the REST API, assigned ownership/milestones/severity/due dates, documented risk acceptance and residual risk using custom fields, and exported the tracked findings into an OSCAL-compliant POA&M JSON file.

### 🏆 Key Accomplishments

- Deployed and configured a Redmine ticketing instance from source
- Automated SAR-finding-to-ticket conversion via the Redmine REST API
- Assigned ownership, severity, milestones, and SLA-based due dates
- Documented a formal risk acceptance decision with residual risk rationale
- Exported a tracked POA&M into OSCAL-compliant JSON

### 🌍 Real-World Applications

This workflow directly supports **CGRC Domain 5 (Authorization)** and **Domain 7 (Continuous Monitoring)** by demonstrating how assessed findings are operationally tracked from identification through remediation or formal risk acceptance — the same lifecycle GRC teams run when preparing for ATO renewal and continuous monitoring reporting.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
