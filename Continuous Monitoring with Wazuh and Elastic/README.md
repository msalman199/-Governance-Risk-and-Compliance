<div align="center">

# 📡 Continuous Monitoring with Wazuh and Elastic

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04%2F24.04-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Wazuh](https://img.shields.io/badge/Wazuh-4.x-3AB6E3?style=for-the-badge&logo=wazuh&logoColor=white)
![OpenSearch](https://img.shields.io/badge/OpenSearch-Dashboards-005EB8?style=for-the-badge&logo=opensearch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NIST RMF](https://img.shields.io/badge/NIST-RMF%20Domain%207-002F6C?style=for-the-badge&logo=nist&logoColor=white)

*Deploy a self-contained SIEM and operationalize it as an ongoing-authorization ConMon program*

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🧩 Task 1: Deploy Wazuh Manager and Agent (All-in-One)](#-task-1-deploy-wazuh-manager-and-agent-all-in-one)
- [🔍 Task 2: Configure FIM and SCA Policy Checks](#-task-2-configure-fim-and-sca-policy-checks)
- [📐 Task 3: Define ConMon Metrics, Frequencies, and Reporting Cadence](#-task-3-define-conmon-metrics-frequencies-and-reporting-cadence)
- [📊 Task 4: Build Dashboards for Control Effectiveness and Drift](#-task-4-build-dashboards-for-control-effectiveness-and-drift)
- [📄 Task 5: Generate a Monthly ConMon Report for the AO](#-task-5-generate-a-monthly-conmon-report-for-the-ao)
- [🛡️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [✅ Verification](#-verification)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By completing this lab, you will:

| # | Objective |
|---|---|
| 1 | Deploy Wazuh manager/agent as a self-contained SIEM for continuous monitoring (ConMon) |
| 2 | Configure File Integrity Monitoring (FIM) and Security Configuration Assessment (SCA) policies |
| 3 | Design a ConMon program (metrics, frequencies, reporting cadence) aligned to CGRC Domain 7 |
| 4 | Build Wazuh dashboard visualizations tracking control effectiveness and configuration drift |
| 5 | Produce a monthly ConMon report artifact suitable for Authorizing Official (AO) review |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🐧 Linux Administration | Strong skills (systemd, package managers, firewall/networking basics) |
| 📊 SIEM Concepts | Working knowledge of log pipelines and JSON/YAML configuration |
| 🏛️ CGRC Domain 7 | Familiarity with POA&Ms, control effectiveness, ongoing authorization |
| 📖 Vendor Docs | Comfort reading vendor documentation independently (Wazuh docs are your primary reference) |
| 💻 Hardware | Minimum 4 vCPU / 8GB RAM Linux machine (Ubuntu 22.04/24.04 recommended) |

## 🖥️ Environment Setup

> **Lab Environment:** Single Linux machine provided via Al Nafi Start Lab (Ubuntu 22.04+ assumed). No external cloud dependencies — Wazuh indexer, server, and dashboard all run locally. You will install the Wazuh all-in-one stack (manager + indexer + dashboard, Elastic-based) using the official installation script, then register a local agent against itself (or a second local container/process if available). **Root/sudo access required.**

---

## 🧩 Task 1: Deploy Wazuh Manager and Agent (All-in-One)

> **🏗️ Architecture note:** Wazuh 4.x replaced the raw ELK stack with the Wazuh indexer (OpenSearch-based fork) and Wazuh dashboard, but the underlying data model and query experience remain Elastic-compatible. Use the official all-in-one installer for a single-node deployment.

### 📌 Requirements

- Download and run the Wazuh installation assistant script for a single-node all-in-one install
- Confirm all three components (indexer, manager, dashboard) report healthy status
- Register the local host as a monitored agent (self-monitoring is acceptable for this lab)
- Validate agent connectivity via the manager's agent control utility

```bash
# Reference only — consult current Wazuh docs for exact script name/version
curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
# TODO: run with appropriate flags for all-in-one, non-interactive or interactive install
# TODO: capture generated dashboard admin credentials from script output
# TODO: verify service status for wazuh-manager, wazuh-indexer, wazuh-dashboard
# TODO: use /var/ossec/bin/agent_control or manage_agents to confirm agent registration
```

**📦 Deliverable:** screenshot or CLI output showing manager, indexer, dashboard active and agent listed as "Active."

---

## 🔍 Task 2: Configure FIM and SCA Policy Checks

### 📌 Requirements

- Edit the agent's `ossec.conf` `<syslog_output>`/`<syscheck>` (FIM) block to monitor at least two sensitive paths (e.g., `/etc`, `/root/.ssh`, or a custom app config directory)
- Set an appropriate scan frequency (justify your choice — real-time vs. scheduled) considering performance trade-offs
- Enable and run a Security Configuration Assessment (SCA) policy (e.g., CIS benchmark for the OS) via the built-in `wodle` SCA module
- Trigger a manual file change and confirm an alert is generated and visible in the dashboard
- Review SCA scan results and identify at least 3 failed checks; document remediation feasibility

```xml
<!-- /var/ossec/etc/ossec.conf (agent) — partial reference -->
<syscheck>
  <!-- TODO: define <directories> entries, real_time attribute, frequency -->
</syscheck>
<wodle name="sca">
  <!-- TODO: enable, set scan_on_start, interval, policy file reference -->
</wodle>
```

**📦 Deliverable:** dashboard screenshot of a FIM alert + SCA scan summary with pass/fail counts.

---

## 📐 Task 3: Define ConMon Metrics, Frequencies, and Reporting Cadence

> This is a **design task** — no single correct answer. Produce a written ConMon plan (markdown or table) covering:

### 📌 Requirements

- **Metrics** (minimum 5): e.g., % assets with active agent, FIM alert volume/severity, SCA compliance score trend, mean time to detect (MTTD) configuration drift, critical vulnerability count
- **Frequency per metric:** continuous, daily, weekly, monthly — justify based on control criticality and CGRC ongoing authorization expectations
- **Reporting cadence:** define what rolls up daily to a SOC analyst dashboard vs. monthly to the AO
- **Control mapping:** map each metric to a NIST 800-53 control family (e.g., CM-6, SI-4, RA-5) relevant to Domain 7

**📦 Deliverable:** `conmon_plan.md` with a metrics table (`Metric | Frequency | Data Source | Control Mapping | Threshold/Trigger`).

---

## 📊 Task 4: Build Dashboards for Control Effectiveness and Drift

### 📌 Requirements

Using Wazuh dashboard (OpenSearch Dashboards interface), create a custom index-pattern-based visualization set including:

- SCA compliance score over time (line chart)
- FIM alerts by rule severity (bar/heat map)
- Top 10 hosts/paths with most configuration changes (drift indicator)
- Combine visualizations into a single custom dashboard named `ConMon-Domain7`
- Apply a saved search/filter to exclude noise (e.g., known benign change patterns)

```bash
# Design guidance — no fixed steps:
# TODO: identify correct index pattern (wazuh-alerts-*)
# TODO: choose aggregation type per visualization (avg, terms, date histogram)
# TODO: justify chart type selection per metric from Task 3
```

**📦 Deliverable:** exported dashboard (NDJSON via Saved Objects) or screenshot set.

---

## 📄 Task 5: Generate a Monthly ConMon Report for the AO

### 📌 Requirements

- Query Wazuh (via dashboard export, curl against the indexer API, or Wazuh API) to pull the prior 30 days of alert and SCA data
- Synthesize findings into an AO-ready report including: executive summary, control effectiveness trend, open risks/POA&M candidates, recommended actions
- Automate at least the data-pull step with a script (language of your choice) rather than manual export

```python
def generate_conmon_report(days_back: int = 30, output_path: str = "conmon_report.md") -> str:
    """
    Query Wazuh indexer/API for the reporting window and produce
    an AO-facing ConMon report.

    Args:
        days_back: Reporting window in days
        output_path: Destination file for the generated report

    Returns:
        Path to the generated report file
    """
    # TODO: authenticate against Wazuh API or indexer (OpenSearch query DSL)
    # TODO: aggregate SCA scores, FIM alert counts by severity
    # TODO: identify trend (improving/degrading) vs. prior period
    # TODO: render markdown/PDF report with executive summary section
    pass
```

**📦 Deliverable:** `conmon_report.md` (or PDF) containing at minimum: summary, metrics table, trend commentary, open findings.

---

## 🛡️ MITRE ATT&CK Mapping

| Technique ID | Name | Relevance |
|---|---|---|
| T1565.001 | Data Manipulation: Stored Data Manipulation | FIM detects unauthorized modification of monitored files |
| T1070 | Indicator Removal on Host | FIM/log alerting surfaces tampering with logs or evidence |
| T1562.001 | Impair Defenses: Disable or Modify Tools | SCA and agent-status checks detect disabled/misconfigured security tooling |
| T1098 | Account Manipulation | SCA configuration drift checks catch unauthorized account/permission changes |

---

## ✅ Verification

- [ ] `systemctl status wazuh-manager wazuh-indexer wazuh-dashboard` all show active (running)
- [ ] Agent status shows Active via `/var/ossec/bin/agent_control -l`
- [ ] A test file change under a monitored path produces a searchable FIM alert in the dashboard within the configured scan window
- [ ] SCA scan results are queryable and show a numeric compliance percentage
- [ ] `ConMon-Domain7` dashboard renders all three visualizations without errors
- [ ] `conmon_plan.md` and `conmon_report.md` exist and map metrics to control families

---

## 🏁 Conclusion

You deployed a self-contained Wazuh/Elastic-based SIEM stack and operationalized it as a continuous monitoring capability supporting CGRC Domain 7. You configured FIM and SCA to detect unauthorized change and configuration drift, designed a metrics-driven ConMon program with defined cadences mapped to NIST control families, built an executive dashboard for control effectiveness, and automated generation of an AO-facing monthly report — mirroring real-world GRC Analyst and SOC Analyst responsibilities in an ongoing authorization environment.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
