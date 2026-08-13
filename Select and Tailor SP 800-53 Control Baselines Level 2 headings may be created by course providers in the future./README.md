<div align="center">

# 🧩 Select and Tailor SP 800-53 Control Baselines

![CGRC](https://img.shields.io/badge/CGRC-Domain%203-orange?style=for-the-badge)
![SP 800-53](https://img.shields.io/badge/NIST-SP%20800--53%20Rev5-0052CC?style=for-the-badge)
![OSCAL](https://img.shields.io/badge/OSCAL-CLI-2E8B57?style=for-the-badge)
![GRC](https://img.shields.io/badge/GRC-Governance%20Risk%20Compliance-4B0082?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Terminal-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**Baseline selection, privacy tailoring, and control inheritance for a moderate-impact HR system**

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [📥 Task 1: Install OSCAL CLI and Download SP 800-53B Baselines](#-task-1-install-oscal-cli-and-download-sp-800-53b-baselines)
- [🎯 Task 2: Select the Moderate Baseline for the Example Workload](#-task-2-select-the-moderate-baseline-for-the-example-workload)
- [🔐 Task 3: Tailor Controls Using a Privacy Overlay](#-task-3-tailor-controls-using-a-privacy-overlay)
- [🏷️ Task 4: Designate System-Specific, Hybrid, and Common Controls](#️-task-4-designate-system-specific-hybrid-and-common-controls)
- [📤 Task 5: Export Tailored Control Set in OSCAL JSON](#-task-5-export-tailored-control-set-in-oscal-json)
- [✅ Verification](#-verification)
- [🧠 Key Concepts](#-key-concepts)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Install and use the **NIST OSCAL CLI** on Linux |
| 2 | Select the **SP 800-53 moderate control baseline** for a sample workload |
| 3 | Tailor controls using a **privacy overlay** with documented rationale |
| 4 | Classify controls as **system-specific, hybrid, or common** |
| 5 | Export a tailored control baseline in **OSCAL JSON** format |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 📘 SP 800-53 familiarity | Control families and baseline concepts (low/moderate/high) |
| 💻 Linux command line | Basic — navigating directories, editing files |
| 🎓 CGRC context | Understanding of CGRC Domain 3 (Selecting and Approving Security/Privacy Controls) |
| 🧩 OSCAL experience | None required |

## 🖥️ Environment Setup

> 🧪 **Al Nafi provides a single Linux machine via Start Lab.** Use the terminal for all steps.

```bash
# 📦 Update system and install Java (required for OSCAL CLI)
sudo apt update
sudo apt install -y openjdk-17-jre-headless unzip wget jq

# ☕ Verify Java
java -version
```

---

## 📥 Task 1: Install OSCAL CLI and Download SP 800-53B Baselines

**1️⃣ Download and extract the OSCAL CLI:**

```bash
cd ~
wget https://github.com/usnistgov/oscal-cli/releases/latest/download/oscal-cli-distribution.zip
unzip oscal-cli-distribution.zip -d oscal-cli
export PATH=$PATH:~/oscal-cli/bin
oscal-cli --version
```

**2️⃣ Add the PATH export to `~/.bashrc` so it persists:**

```bash
echo 'export PATH=$PATH:~/oscal-cli/bin' >> ~/.bashrc
```

**3️⃣ Create a working directory and download the SP 800-53 Rev 5 catalog and baselines** (OSCAL content repo):

```bash
mkdir -p ~/oscal-lab/content && cd ~/oscal-lab/content

# TODO: Download the SP 800-53 catalog JSON
wget https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json

# TODO: Download the moderate baseline profile JSON
wget https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_MODERATE-baseline_profile.json
```

**4️⃣ Validate the downloaded files:**

```bash
oscal-cli profile validate NIST_SP-800-53_rev5_MODERATE-baseline_profile.json
```

> ⚠️ **Troubleshooting:** If validation fails with a schema error, confirm the file downloaded completely (`ls -lh`) and re-download if size is 0 or truncated.

---

## 🎯 Task 2: Select the Moderate Baseline for the Example Workload

> 👤 **Scenario:** You are the GRC Architect for a moderate-impact HR records system (`HR-Sys`) processing employee PII.

**1️⃣ Resolve the moderate profile into a flattened catalog** to see all included controls:

```bash
cd ~/oscal-lab/content
oscal-cli profile resolve NIST_SP-800-53_rev5_MODERATE-baseline_profile.json \
  -o ~/oscal-lab/hr-sys-resolved-catalog.json
```

**2️⃣ Inspect the resolved catalog control count:**

```bash
jq '[.catalog.groups[].controls[]?.id] | length' ~/oscal-lab/hr-sys-resolved-catalog.json
```

**📝 TODO:** List all controls belonging to the Access Control (AC) family using `jq`. Reference the OSCAL catalog schema for the correct path (hint: filter by id prefix `ac-`).

---

## 🔐 Task 3: Tailor Controls Using a Privacy Overlay

Since HR-Sys processes PII, apply a privacy-focused tailoring by creating a custom profile that imports the moderate baseline and adds/modifies controls (e.g., emphasizing PT family and SC-9-equivalent protections).

**1️⃣ Create a tailoring profile file `hr-sys-privacy-profile.json`:**

```bash
cd ~/oscal-lab
touch hr-sys-privacy-profile.json
```

**2️⃣ Use this starter template — complete the TODOs:**

```json
{
  "profile": {
    "uuid": "GENERATE-A-UUID-HERE",
    "metadata": {
      "title": "HR-Sys Moderate Baseline with Privacy Overlay",
      "last-modified": "2024-01-01T00:00:00Z",
      "version": "1.0",
      "oscal-version": "1.1.2"
    },
    "imports": [
      {
        "href": "content/NIST_SP-800-53_rev5_MODERATE-baseline_profile.json"
      }
    ],
    "modify": {
      "set-parameters": [
        {
          "param-id": "ac-2_prm_1",
          "values": ["TODO: define account types applicable to HR-Sys"]
        }
      ],
      "alters": [
        {
          "control-id": "pt-2",
          "adds": [
            {
              "props": [
                {
                  "name": "rationale",
                  "value": "TODO: Explain why PT-2 (Authority to Process PII) is emphasized for HR-Sys"
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

**3️⃣ Generate a UUID for the profile:**

```bash
python3 -c "import uuid; print(uuid.uuid4())"
```

**4️⃣ Validate your tailored profile:**

```bash
oscal-cli profile validate hr-sys-privacy-profile.json
```

**5️⃣ Document your rationale** in a separate markdown file `tailoring-rationale.md`:

```bash
cat > tailoring-rationale.md << 'EOF'
# Tailoring Rationale - HR-Sys

## Control: PT-2 (Authority to Process PII)
Rationale: TODO

## Control: AC-2 (Account Management)
Rationale: TODO

## Compensating Control (if any control cannot be fully implemented)
Control Not Implemented: TODO
Compensating Control Applied: TODO
Justification: TODO
EOF
```

---

## 🏷️ Task 4: Designate System-Specific, Hybrid, and Common Controls

**1️⃣ Create a control designation worksheet `control-designations.csv`:**

```bash
cat > control-designations.csv << 'EOF'
control-id,designation,justification
ac-2,hybrid,TODO
au-2,common,TODO
pt-2,system-specific,TODO
cp-9,common,TODO
EOF
```

**📝 TODO:** Add at least 6 more controls from the moderate baseline (from families AC, AU, CM, IR, SC, PT) and classify each as:

| Designation | Meaning |
|---|---|
| 🌐 common | Inherited from a shared service (e.g., managed by a central IT/security team) |
| 🏢 system-specific | Implemented uniquely by HR-Sys |
| 🔀 hybrid | Partially inherited, partially implemented locally |

Justify each designation in one sentence, referencing how HR-Sys's architecture (e.g., shared logging service, dedicated PII database) supports the classification.

---

## 📤 Task 5: Export Tailored Control Set in OSCAL JSON

**1️⃣ Resolve your tailored privacy profile into a final catalog for handoff:**

```bash
cd ~/oscal-lab
oscal-cli profile resolve hr-sys-privacy-profile.json \
  -o hr-sys-final-tailored-catalog.json
```

**2️⃣ Validate the final export:**

```bash
oscal-cli catalog validate hr-sys-final-tailored-catalog.json
```

**3️⃣ Confirm the file is well-formed JSON:**

```bash
jq . hr-sys-final-tailored-catalog.json > /dev/null && echo "Valid JSON"
```

> ⚠️ **Troubleshooting:** If `oscal-cli profile resolve` fails due to a broken href, ensure the `imports.href` path in your profile is relative to your current working directory or use an absolute path.

---

## ✅ Verification

Run these checks to confirm lab completion:

```bash
# 1. Confirm OSCAL CLI is installed
oscal-cli --version

# 2. Confirm baseline files exist
ls -lh ~/oscal-lab/content/*.json

# 3. Confirm tailored profile validates
oscal-cli profile validate ~/oscal-lab/hr-sys-privacy-profile.json

# 4. Confirm final export exists and is valid JSON
jq '.catalog.metadata.title' ~/oscal-lab/hr-sys-final-tailored-catalog.json

# 5. Confirm rationale and designation files exist
ls ~/oscal-lab/tailoring-rationale.md ~/oscal-lab/control-designations.csv
```

**Expected outcome:** All commands return valid output with no errors; `hr-sys-final-tailored-catalog.json` contains your tailored control title and modified parameters/controls.

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| 🧩 OSCAL | The NIST Open Security Controls Assessment Language — machine-readable format for catalogs, profiles, and SSPs |
| 📘 SP 800-53 Baseline | A pre-selected set of controls (Low/Moderate/High) forming the starting point for a system's control set |
| ✂️ Tailoring / Overlay | Adjusting a baseline's parameters and controls to fit a system's specific context (e.g., a privacy overlay for PII) |
| 🏷️ Control Designation | Classifying each control as common, hybrid, or system-specific based on how it's implemented and inherited |
| 📤 Profile Resolution | Flattening a profile's imports and modifications into a single resolved catalog for implementation and assessment |

---

## 🏁 Conclusion

In this lab, you installed and configured the NIST OSCAL CLI, downloaded and validated SP 800-53 Rev 5 catalog and moderate baseline content, and resolved that baseline for a sample moderate-impact HR system.

### 🎯 Key Accomplishments
- Applied CGRC Domain 3 skills by tailoring the baseline with a privacy overlay
- Documented rationale for parameter and control modifications
- Classified controls as system-specific, hybrid, or common based on system architecture
- Exported a fully resolved, validated OSCAL JSON control set ready for handoff to implementation and assessment teams

### 🌍 Real-World Applications
These skills directly support real-world **GRC Architect** responsibilities in baseline selection, tailoring, and control inheritance documentation required for CGRC-aligned authorization packages.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
