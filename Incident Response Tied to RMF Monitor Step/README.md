Incident Response Lab Tied to RMF Monitor Step
Lab Title: Deploying TheHive/Cortex for IR Case Management and Integrating with RMF Monitor
Author: [Your Name]
Date: [YYYY-MM-DD]
Version: 1.0

🎯 Objectives
By the end of this lab, you will be able to:

✅ Deploy TheHive/Cortex as an IR case management platform on a single Linux host

✅ Design NIST SP 800-61-aligned playbooks that map incident phases to RMF Monitor activities

✅ Establish traceability between incident artifacts, SSP controls, and POA&M entries

✅ Automate POA&M lifecycle updates using API-driven workflows

✅ Produce a CGRC Domain 7-compliant after-action report

🧠 Prerequisites
💻 Strong Linux administration (systemd, Docker/Podman, networking, JSON/YAML)

📚 Working knowledge of NIST RMF steps (Categorize through Monitor) and SP 800-61 IR lifecycle

🔌 Familiarity with REST APIs, curl/Python scripting

📋 Prior exposure to SSP/POA&M structure (NIST SP 800-18, SP 800-137)

🐳 Comfort with Docker Compose and reverse-proxy concepts

🖥️ Environment Setup
OS: Single Linux machine (Ubuntu 22.04 LTS) provided via Al Nafi Start Lab

Resources: Minimum 4 vCPU / 8GB RAM recommended

Tools: Docker Engine + Docker Compose plugin required (install if not present)

Network: No external cloud dependencies — all services run locally in containers

✅ Verify/Install Docker
bash
docker --version || (curl -fsSL https://get.docker.com | sh)
sudo systemctl enable --now docker
docker compose version
🧩 Task 1: Deploy TheHive + Cortex for Case Management
🏗️ Architecture Requirement
TheHive (case mgmt) + Cortex (analyzers) + Elasticsearch/Cassandra backend

Networked via Docker Compose, exposed on localhost only

Research current TheHive 5.x deployment method (official Docker images vs. package repo — package repo is deprecated; use Docker)

📄 docker-compose.yml (Skeleton)
text
version: "3.8"
services:
  cassandra:
    image: cassandra:4.1
    # TODO: environment, volumes, healthcheck

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.x
    # TODO: single-node discovery, memory limits

  cortex:
    image: thehiveproject/cortex:latest
    # TODO: depends_on, config volume mount

  thehive:
    image: strangebee/thehive:5.x
    # TODO: depends_on cassandra + elasticsearch, config mount, port mapping
⚙️ Configuration Steps
Configure persistent volumes and a shared Docker network

Set initial admin credentials via TheHive's org/user bootstrap API or UI

Design decision: Determine whether to run Cortex analyzers in Docker-in-Docker or install analyzer dependencies directly — justify your choice in your notes

✅ Validation
TheHive UI reachable on https://localhost:9000

Cortex on https://localhost:9001, linked via API key

📘 Task 2: Define IR Playbooks Aligned to NIST SP 800-61 → RMF Monitor Mapping
🧭 Create Case Templates in TheHive
Representing the four SP 800-61 phases:

Preparation

Detection & Analysis

Containment/Eradication/Recovery

Post-Incident Activity

Each phase must map to an RMF Monitor activity (e.g., Detection → Ongoing Assessment trigger; Post-Incident → POA&M update trigger)

🧩 Define Custom Fields in TheHive Case Templates
affected_controls

poam_id

ao_notified

reassessment_required

📄 Deliverable: Playbook Document (Markdown/YAML)
SP 800-61 Phase	RMF Monitor Trigger	TheHive Case Field
Detection & Analysis	Control effectiveness reassessment	affected_controls
Containment	Interim POA&M entry	poam_id
Post-Incident	AO notification + final POA&M closure	ao_notified
Import this structure as a TheHive case template via API or UI JSON import

🔗 Task 3: Link Incident Artifacts to SSP Controls
📁 Simulate an SSP as a Local JSON/YAML File
ssp_controls.yaml containing NIST 800-53 control IDs (e.g., IR-4, IR-6, CA-7, CM-3)

🧠 Build a Script
python
def link_case_to_controls(case_id: str, ssp_path: str) -> dict:
    """
    Fetch a TheHive case, extract affected_controls field,
    validate against SSP control catalog, and return mapping.

    Args:
        case_id: TheHive case identifier
        ssp_path: path to local SSP control YAML

    Returns:
        dict mapping control_id -> {status, case_id, evidence_link}
    """
    # TODO: Authenticate to TheHive API (API key from env var)
    # TODO: GET /api/v1/case/{case_id}
    # TODO: Parse affected_controls custom field
    # TODO: Load and validate against ssp_path
    # TODO: Flag controls requiring reassessment (status = "monitor-triggered")
    pass
📤 Store Output
control_impact_report.json — this becomes evidence for the Monitor step

🤖 Task 4: Automate POA&M Update on Incident Closure
🏗️ Architecture Requirement
Use TheHive webhooks (or polling via cron) to detect case closure, then trigger a POA&M update script

Configure a TheHive webhook (or a scheduled poller if webhooks unavailable in your version) firing on case status = Resolved

🗃️ Maintain POA&M as a Local CSV/SQLite Table
poam.db with fields: poam_id, control_id, weakness, status, remediation_date, source_case_id

🧠 Automation Script
python
def update_poam_on_closure(case_id: str, poam_db: str) -> bool:
    """
    Triggered when a TheHive case is closed. Updates or creates
    POA&M entries and marks reassessment status.

    Args:
        case_id: closed TheHive case ID
        poam_db: path to POA&M SQLite/CSV store

    Returns:
        True if POA&M successfully updated
    """
    # TODO: Retrieve closed case details + control_impact_report.json
    # TODO: For each affected control, upsert POA&M record
    # TODO: Set remediation_date = case close date
    # TODO: Write AO notification log entry (see Task 5)
    pass
⚠️ Edge Case to Handle
Partial remediation — case closed but control still requires compensating measures (status = "Risk Accepted" vs "Closed")

⚙️ Automation Wiring
Wire this function to run automatically (webhook receiver script using Flask/FastAPI, or cron polling every N minutes) — design choice is yours; justify latency trade-offs

📝 Task 5: After-Action Report and AO Notification
📄 Generate an After-Action Report
Summarizing: incident timeline, controls impacted, POA&M changes, lessons learned, AO notification status

Simulate AO notification as a logged/emailed artifact (use local sendmail/msmtp or simply append to ao_notifications.log)

🧠 Report Generation Script
python
def generate_after_action_report(case_id: str, output_path: str) -> str:
    """
    Compile case data, control impact report, and POA&M diffs
    into a CGRC Domain 7-aligned after-action report.

    Args:
        case_id: resolved TheHive case ID
        output_path: destination file path (.md)

    Returns:
        Path to generated report
    """
    # TODO: Pull case summary, timeline, and observables from TheHive
    # TODO: Merge control_impact_report.json + poam.db diff
    # TODO: Add "Lessons Learned" and "AO Notification" sections
    # TODO: Write formatted Markdown to output_path
    pass
✅ Verification Checklist
TheHive and Cortex UIs accessible; Cortex successfully linked as analyzer engine in TheHive

At least one test case created using your custom SP 800-61/RMF-mapped template

control_impact_report.json exists and correctly lists affected controls with reassessment flags

POA&M store (poam.db) reflects an updated/new entry after simulating case closure

after_action_report.md generated containing all required sections, including explicit AO notification evidence

Spot-check: manually close a second test case and confirm automation re-triggers POA&M update without manual intervention

🏁 Conclusion
In this lab, you architected an end-to-end integration between incident response operations and the RMF Monitor step, using TheHive and Cortex as the operational backbone. You designed SP 800-61-aligned playbooks with explicit RMF triggers, built traceability from incident artifacts to SSP controls, automated POA&M lifecycle updates on case closure, and produced a CGRC Domain 7-compliant after-action report. This exercise reflects real-world GRC/IR convergence responsibilities expected of Incident Response Managers and GRC Analysts operating continuous monitoring programs.

📌 Tip: Replace all TODO placeholders with real values, API keys, and environment-specific configurations before deployment.

