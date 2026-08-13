<div align="center">

# 📊 Categorize System Impact Using FIPS 199 and SP 800-60

![CGRC](https://img.shields.io/badge/CGRC-Domain%202%20%26%203-orange?style=for-the-badge)
![FIPS 199](https://img.shields.io/badge/FIPS-199-0052CC?style=for-the-badge)
![NIST SP 800-60](https://img.shields.io/badge/NIST-SP%20800--60-0052CC?style=for-the-badge)
![GRC](https://img.shields.io/badge/GRC-Governance%20Risk%20Compliance-4B0082?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Terminal-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**A hands-on security categorization exercise for a healthcare scheduling workload**

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Environment Setup](#️-environment-setup)
- [🏥 Scenario](#-scenario)
- [📗 Task 1: Set Up Your Workbook](#-task-1-set-up-your-workbook)
- [🔎 Task 2: Identify Information Types (SP 800-60 Vol 2)](#-task-2-identify-information-types-sp-800-60-vol-2)
- [⚖️ Task 3: Assign Provisional Impact Ratings](#️-task-3-assign-provisional-impact-ratings)
- [🧭 Task 4: Adjust Impact Based on Operational Context](#-task-4-adjust-impact-based-on-operational-context)
- [✍️ Task 5: Produce a Signed Categorization Memo](#️-task-5-produce-a-signed-categorization-memo)
- [✅ Verification](#-verification)
- [🧠 Key Concepts](#-key-concepts)
- [🔧 Troubleshooting](#-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Identify information types for a sample system using **NIST SP 800-60 Volume 2** |
| 2 | Assign provisional **Confidentiality, Integrity, and Availability (C-I-A)** impact ratings using **FIPS 199** |
| 3 | Adjust impact levels based on operational context and document justifications |
| 4 | Use basic command-line and spreadsheet tools to record a security categorization |
| 5 | Produce a signed categorization memo for an authorizing official (AO) |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 💻 Terminal familiarity | Basic — navigating folders, running commands |
| 📚 GRC experience | None required |
| 🔺 C-I-A concepts | Basic understanding of confidentiality, integrity, and availability (reviewed in-lab) |

## 🖥️ Environment Setup

> 🧪 **Al Nafi provides a single Linux machine via Start Lab.** All tools used are open-source and installed locally — no cloud or external accounts needed.

**1️⃣ Start your lab machine and open a terminal.**

**2️⃣ Update packages and install required tools:**

```bash
sudo apt update
sudo apt install -y libreoffice-calc git python3 python3-pip
```

**3️⃣ Install the OSCAL CLI tool** (used to validate categorization data in OSCAL format):

```bash
pip3 install --user oscal-cli
# ✅ Verify install
oscal-cli --version
```

**4️⃣ Create a working directory:**

```bash
mkdir -p ~/fips199-lab && cd ~/fips199-lab
```

---

## 🏥 Scenario

> 👤 **You are a Cybersecurity Risk & Controls Analyst** reviewing a sample workload: a **Patient Appointment Scheduling System** used by a mid-size clinic network. It stores patient names, appointment times, and basic contact information (no medical diagnosis data).

---

## 📗 Task 1: Set Up Your Workbook

**1️⃣ Launch LibreOffice Calc:**

```bash
libreoffice --calc &
```

**2️⃣ Create a new spreadsheet named `categorization_workbook.ods` in `~/fips199-lab`.**

**3️⃣ Create these column headers in Row 1:**

```
A: Information Type | B: Confidentiality | C: Integrity | D: Availability | E: Justification
```

**4️⃣ Save the file.**

---

## 🔎 Task 2: Identify Information Types (SP 800-60 Vol 2)

> 📘 SP 800-60 Vol 2 provides pre-defined information types (e.g., "Patient Identity Management," "Appointment/Scheduling Information").

**1️⃣ Create a text file to record your research:**

```bash
nano information_types.txt
```

**2️⃣ List two information types relevant to the scenario.** Example format:

```
Information Type: Scheduling Information (D.16.3 - similar reference category)
Description: Appointment dates, times, provider assignments

Information Type: Identity/PII Management
Description: Patient name, phone number, email
```

💾 Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## ⚖️ Task 3: Assign Provisional Impact Ratings

> 📘 FIPS 199 defines impact levels as **Low**, **Moderate**, or **High** for C, I, and A.

**Reference guide** (use this table while rating):

| Impact | Meaning |
|---|---|
| Low | Limited adverse effect |
| Moderate | Serious adverse effect |
| High | Severe or catastrophic effect |

In your spreadsheet, fill in provisional ratings for each information type. Example starting point:

```
Row 2: Scheduling Information   | Low      | Moderate | Moderate | (justification pending)
Row 3: Identity/PII Management  | Moderate | Moderate | Low      | (justification pending)
```

**📝 TODO for you to complete:**
- Assign a provisional C-I-A rating for both information types listed in your `information_types.txt`
- Base your rating on the SP 800-60 provisional guidance (PII typically starts at **Moderate confidentiality**)

---

## 🧭 Task 4: Adjust Impact Based on Operational Context

> 💡 Provisional ratings are a starting point — adjust based on real-world context.

**Consider these adjustment factors:**

- ⏱️ Does losing availability delay urgent care? (raises Availability)
- 🔗 Is data aggregated with other sensitive data? (may raise Confidentiality)
- ⚖️ Is the clinic subject to regional privacy law (e.g., GCC data protection regulations)?

**1️⃣ Update the Justification column (E) for each row** explaining your adjustment. Example:

```
E2: "Availability raised to Moderate — scheduling delays could impact patient care continuity."
E3: "Confidentiality kept at Moderate — PII limited to contact info, no medical records stored."
```

**2️⃣ Determine the overall system categorization** using the FIPS 199 high-water mark rule (highest rating across all information types wins per objective):

```bash
# 🐍 Create a small script to help calculate the high-water mark
nano calculate_impact.py
```

```python
def high_water_mark(ratings: list) -> str:
    """
    Determine the overall impact level using FIPS 199 high-water mark rule.

    Args:
        ratings: List of strings, e.g. ["Low", "Moderate", "High"]

    Returns:
        The highest impact level found (as a string)
    """
    # Order of severity, lowest to highest
    order = ["Low", "Moderate", "High"]

    # TODO: Find the rating in 'ratings' with the highest severity
    # Hint: use order.index() to compare severity levels
    # TODO: Return that rating as a string
    pass


# TODO: Call the function separately for Confidentiality, Integrity, and Availability
# Example:
# c_ratings = ["Low", "Moderate"]
# print("Overall Confidentiality:", high_water_mark(c_ratings))
```

**3️⃣ Run your script and record the results:**

```bash
python3 calculate_impact.py
```

---

## ✍️ Task 5: Produce a Signed Categorization Memo

**1️⃣ Create the memo file:**

```bash
nano categorization_memo.txt
```

**2️⃣ Use this template** (fill in your findings):

```
SECURITY CATEGORIZATION MEMO

System Name: Patient Appointment Scheduling System
Prepared By: [Your Name], Cybersecurity Risk & Controls Analyst
Date: [Today's Date]

Information Types Identified:
1. Scheduling Information
2. Identity/PII Management

Overall System Categorization (FIPS 199 High-Water Mark):
- Confidentiality: [Fill in]
- Integrity: [Fill in]
- Availability: [Fill in]

Justification Summary:
[Summarize key reasons from your spreadsheet]

Recommendation: Categorize system as [Low/Moderate/High] impact overall.

Authorizing Official Signature: ____________________
Date: ____________________
```

**3️⃣ Save the memo, then "sign" it digitally** using a simple checksum as a stand-in for a digital signature:

```bash
sha256sum categorization_memo.txt > categorization_memo.sig
cat categorization_memo.sig
```

> 🔏 This checksum acts as an integrity marker — any future edit to the memo will produce a different hash, showing tampering.

---

## ✅ Verification

Run these checks to confirm your work is complete:

```bash
# Check all required files exist
ls -l ~/fips199-lab
```

Expected files:

- `categorization_workbook.ods`
- `information_types.txt`
- `calculate_impact.py`
- `categorization_memo.txt`
- `categorization_memo.sig`

```bash
# Confirm the memo contains your ratings (should return matching lines)
grep -i "Confidentiality" categorization_memo.txt
grep -i "Integrity" categorization_memo.txt
grep -i "Availability" categorization_memo.txt
```

```bash
# Verify the signature file matches the memo
sha256sum -c categorization_memo.sig
```

Expected output: `categorization_memo.txt: OK`

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| 🔺 C-I-A Triad | Confidentiality, Integrity, and Availability — the three impact dimensions rated under FIPS 199 |
| 📘 FIPS 199 | Federal standard defining Low/Moderate/High security categorization for information and information systems |
| 📗 NIST SP 800-60 | Guidance mapping information types to provisional C-I-A impact levels |
| 📈 High-Water Mark Rule | The overall system rating equals the highest individual rating across all information types |
| 🧭 Provisional vs. Adjusted Impact | Provisional ratings from SP 800-60 are a starting point, adjusted for real operational context |
| ✍️ Categorization Memo | The signed deliverable documenting findings for an authorizing official (AO) |

---

## 🔧 Troubleshooting

<details>
<summary>Click to expand common issues and fixes</summary>

- **LibreOffice won't open:** Run `libreoffice --calc` without `&` and check terminal for errors; ensure the package installed correctly.
- **`oscal-cli` command not found:** Ensure `~/.local/bin` is in your PATH: `export PATH=$PATH:~/.local/bin`
- **`sha256sum -c` fails:** You edited the memo after generating the signature — rerun `sha256sum` to regenerate it.
- **Python script errors:** Check indentation; Python requires consistent spacing (4 spaces recommended).

</details>

---

## 🏁 Conclusion

In this lab, you performed a complete FIPS 199 / SP 800-60 security categorization exercise on a sample healthcare scheduling system.

### 🎯 Key Accomplishments
- Identified relevant information types using NIST SP 800-60 Volume 2
- Assigned and adjusted provisional C-I-A impact ratings based on operational context
- Calculated an overall system categorization using the high-water mark method
- Produced a signed categorization memo suitable for an authorizing official's review

### 🌍 Real-World Applications
These skills directly support **CGRC Domain 2 (Categorization)** and **Domain 3 (Selection)** objectives and reflect real-world tasks performed by Cybersecurity Risk & Controls Analysts.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
