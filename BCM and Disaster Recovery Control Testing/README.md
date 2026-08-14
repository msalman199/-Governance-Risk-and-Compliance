# BCM and Disaster Recovery Control Testing

## 📌 Overview

This lab demonstrates how to design, implement, and test **Business Continuity Management (BCM)** and **Disaster Recovery (DR)** controls for a containerized workload on Linux.

The lab focuses on creating a **Business Impact Analysis (BIA)**, defining **RTO/RPO targets**, implementing backups and replication, performing failover testing, and documenting results according to **NIST SP 800-53 CP-family controls** and **CGRC Domains 4 and 5**.

---

## 🎯 Objectives

By completing this lab, you will learn how to:

* Create a Business Impact Analysis (BIA).
* Define and justify RTO and RPO requirements.
* Implement backups using **Restic**.
* Implement data replication using **rsync**.
* Perform a containerized workload failover.
* Conduct a tabletop disaster recovery exercise.
* Measure actual RTO and RPO.
* Document DR testing results and deficiencies.
* Map activities to NIST 800-53 CP controls.
* Create CGRC-aligned assessment documentation.

---

## 🛠️ Prerequisites

* Linux command-line knowledge
* Basic Docker/Podman knowledge
* Git and shell scripting
* Basic networking knowledge
* Understanding of:

  * BIA
  * RTO
  * RPO
  * MTD
  * Failover
  * Disaster Recovery
  * Business Continuity
* Basic knowledge of NIST SP 800-34 and NIST SP 800-53

---

## 💻 Environment

**Operating System:** Ubuntu 22.04+

### Install Required Tools

```bash
sudo apt update
sudo apt install -y docker.io restic rsync sqlite3 jq cron

sudo systemctl enable --now docker

docker --version
restic version
rsync --version
```

### Create Lab Directories

```bash
mkdir -p ~/dr-lab/{workload,backups-primary,backups-secondary,docs,scripts}

cd ~/dr-lab
```

---

## 🏗️ Lab Architecture

```text
                 Linux Host
                     |
          +----------+----------+
          |                     |
     Primary Site           Secondary Site
          |                     |
   Docker Workload       DR Data Directory
          |                     |
   workload/data       backups-secondary/
          |
     +----+----+
     |         |
  Restic     rsync
  Backup    Replication
     |         |
backups-   backups-
primary    secondary
```

The primary and secondary environments are simulated on the same Linux machine.

---

## 📋 Task 1: Business Impact Analysis

Deploy a stateful containerized workload that represents a critical business application.

The workload should:

* Store persistent data.
* Generate sample transactional data.
* Write data periodically.
* Use a mounted directory for persistent storage.

Create:

```text
docs/bia.md
```

The BIA should document:

* Critical business process
* Application dependencies
* Financial impact
* Operational impact
* Reputational impact
* Regulatory impact
* Maximum Tolerable Downtime (MTD)
* Recovery Time Objective (RTO)
* Recovery Point Objective (RPO)
* Required staff and resources

Example targets:

```text
RTO = 15 minutes
RPO = 5 minutes
```

The selected values must be justified based on the business impact analysis.

---

## 💾 Task 2: Backup and Replication

### Restic Backup

Create:

```text
scripts/backup.sh
```

The script should:

* Initialize a Restic repository if required.
* Use a protected password file.
* Back up workload data.
* Create timestamped snapshots.
* Add workload tags.
* Record success and failure information.

Example:

```bash
restic -r <repository> snapshots
```

### Rsync Replication

Create:

```text
scripts/replicate.sh
```

The script should:

* Replicate workload data to the secondary location.
* Use archive mode.
* Use checksums.
* Remove deleted data from the destination.
* Record exit codes.
* Write structured logs.

Example destination:

```text
~/dr-lab/backups-secondary/
```

### Schedule Jobs

Configure cron according to the RPO defined in the BIA.

```bash
crontab -e
```

Verify:

```bash
crontab -l
```

---

## 🔄 Task 3: Failover

Create:

```text
scripts/failover.sh
```

The failover script should:

1. Stop the primary workload.
2. Start a new workload using secondary data.
3. Check application health.
4. Record start and end timestamps.
5. Calculate the actual recovery time.

The goal is to determine whether the implemented solution meets the defined RTO.

---

## 🧪 Task 4: Tabletop Exercise

Create:

```text
docs/tabletop-scenario.md
```

Example scenario:

> Primary storage becomes corrupted and the incident is discovered at 14:20.

Discuss:

* Incident detection
* Escalation
* Roles and responsibilities
* Disaster declaration
* Failover authorization
* Communication
* Recovery decisions

Record the results in:

```text
docs/tabletop-results.md
```

Document:

* Decisions
* Identified gaps
* Timing
* RTO/RPO comparison
* Corrective actions

---

## 🚨 Task 5: Technical Failover Test

Simulate a disaster by removing the primary workload data:

```bash
rm -rf ~/dr-lab/workload/data/*
```

Run:

```bash
./scripts/failover.sh
```

Validate:

* Data recovery
* Data integrity
* Application availability
* Actual RTO
* Actual RPO

Also test Restic recovery:

```bash
restic -r <repo-path> restore latest --target <restore-path>
```

Store supporting evidence in:

```text
docs/evidence/
```

Evidence can include:

* Command output
* Logs
* Screenshots
* Recovery timestamps
* Validation results

---

## 📑 Task 6: Documentation

Create the following documents:

```text
docs/
├── bia.md
├── tabletop-scenario.md
├── tabletop-results.md
├── test-plan.md
├── test-results.md
├── deficiency-log.md
├── bcp-updates.md
└── control-mapping.md
```

### Test Plan

Document:

* Test scope
* Test objectives
* Tabletop exercise
* Technical failover test
* Success criteria
* RTO/RPO requirements

### Test Results

Record:

* Target RTO
* Actual RTO
* Target RPO
* Actual RPO
* Pass/Fail results
* Evidence

### Deficiency Log

Document:

* Identified gap
* Risk
* Root cause
* Remediation
* Responsible owner
* Target completion date

### BCP Updates

Document improvements made to the Business Continuity Plan and Disaster Recovery Plan.

### Control Mapping

Map the lab activities to:

* NIST SP 800-53 CP-2
* NIST SP 800-53 CP-4
* NIST SP 800-53 CP-9
* NIST SP 800-53 CP-10
* CGRC Domain 4
* CGRC Domain 5

---

## 🔍 Verification

Check the documentation:

```bash
ls docs/
```

Check Restic backups:

```bash
restic -r <repo-path> snapshots
```

Check replication logs:

```bash
cat scripts/replicate.log | tail -5
```

Check RTO documentation:

```bash
cat docs/test-results.md | grep -i rto
```

Check cron:

```bash
crontab -l
```

Verify that:

* Backup snapshots exist.
* Replication runs successfully.
* Failover starts the recovery workload.
* Recovered data is available.
* Actual RTO is documented.
* Actual RPO is documented.
* BIA and test results use consistent RTO/RPO values.



---

## 🛡️ Controls Covered

| Control   | Purpose                  |
| --------- | ------------------------ |
| **CP-2**  | Contingency Planning     |
| **CP-4**  | Contingency Plan Testing |
| **CP-9**  | System Backup            |
| **CP-10** | System Recovery          |

---

## 🎓 Skills Demonstrated

This lab demonstrates practical experience with:

* 🏢 Business Continuity Management
* 🔄 Disaster Recovery
* 📊 Business Impact Analysis
* ⏱️ RTO/RPO Management
* 💾 Restic Backups
* 🔁 Rsync Replication
* 🐳 Container Recovery
* 🧪 Disaster Recovery Testing
* 📋 Control Assessment
* 📝 POA&M-Style Deficiency Tracking
* 🔐 NIST 800-53 CP Controls
* 🎯 CGRC Domains 4 & 5

---

## ✅ Conclusion

This lab provides a practical BCM and Disaster Recovery control-testing exercise for a containerized workload.

It combines **BIA development, backup, replication, failover, tabletop testing, technical recovery testing, evidence collection, and control mapping** into a complete DR testing lifecycle.

The final documentation demonstrates how recovery capabilities can be measured against defined **RTO/RPO objectives** and how identified deficiencies can be tracked for continuous improvement.
