<div align="center">

# 🛡️ Define System Scope and Authorization Boundary

![CGRC](https://img.shields.io/badge/CGRC-Domain%202-orange?style=for-the-badge)
![NIST SP 800-37](https://img.shields.io/badge/NIST-SP%20800--37-0052CC?style=for-the-badge)
![draw.io](https://img.shields.io/badge/draw.io-Desktop-F08705?style=for-the-badge&logo=diagramsdotnet&logoColor=white)
![GRC](https://img.shields.io/badge/GRC-Governance%20Risk%20Compliance-4B0082?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Terminal-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**A hands-on lab in system characterization, authorization boundary scoping, and SSP documentation**

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🛠️ Task 1: Install draw.io Desktop](#️-task-1-install-drawio-desktop)
- [📊 Task 2: Inventory Assets, Users, and Data Classification](#-task-2-inventory-assets-users-and-data-classification)
- [🗺️ Task 3: Draw Authorization Boundary and Data Flow Diagrams](#️-task-3-draw-authorization-boundary-and-data-flow-diagrams)
- [📝 Task 4: Write the System Characterization Narrative](#-task-4-write-the-system-characterization-narrative)
- [📄 Task 5: Produce the SSP Scope Section](#-task-5-produce-the-ssp-scope-section)
- [✅ Verification](#-verification)
- [🧠 Key Concepts](#-key-concepts)
- [🔧 Troubleshooting Tips](#-troubleshooting-tips)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 1 | Explain the purpose of system scoping and authorization boundaries under **CGRC Domain 2** |
| 2 | Build a basic asset and data inventory for a sample workload |
| 3 | Create authorization boundary and data flow diagrams using **draw.io desktop** |
| 4 | Write a system characterization narrative referencing **NIST SP 800-37** |
| 5 | Draft the scope section of a **System Security Plan (SSP)** |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 💻 Terminal familiarity | Basic — opening it, typing commands |
| 📚 GRC/diagramming experience | None required |
| 🖥️ Environment | A single Linux machine (Al Nafi Start Lab) with internet access and a desktop GUI |

## 🖥️ Lab Environment

> 🧪 **Your Al Nafi Start Lab provides one Linux machine with a graphical desktop.**
> Open a terminal application from the desktop menu. All tools used in this lab are free and open-source.

---

## 🛠️ Task 1: Install draw.io Desktop

**1️⃣ Update package lists:**

```bash
sudo apt update
```

**2️⃣ Download the draw.io desktop AppImage** (a self-contained app file):

```bash
# 📥 Fetch the draw.io desktop release
wget https://github.com/jgraph/drawio-desktop/releases/download/v24.7.17/drawio-x86_64-24.7.17.AppImage -O drawio.AppImage
```

**3️⃣ Make it executable and run it:**

```bash
# 🔓 Grant execute permission
chmod +x drawio.AppImage
# ▶️ Launch draw.io
./drawio.AppImage
```

> ⚠️ **Troubleshooting tip:** If a "FUSE" error appears, install FUSE support:
> ```bash
> sudo apt install -y libfuse2
> ```

**4️⃣ Confirm the draw.io window opens.** Leave it running or close it — you will use it in Task 3.

---

## 📊 Task 2: Inventory Assets, Users, and Data Classification

Instead of a full CMDB server install (heavy for a basic lab), you'll build a lightweight CMDB using CSV files — a common beginner-friendly technique for asset inventory.

**1️⃣ Create a working folder:**

```bash
mkdir ~/cgrc-lab && cd ~/cgrc-lab
```

**2️⃣ Create the asset inventory file:**

```bash
nano asset_inventory.csv
```

Add the following sample data (edit values as needed):

```csv
AssetID,AssetName,Type,Owner,DataClassification,Location
A001,WebApp-Server,Server,IA Manager,Confidential,On-Prem
A002,DB-Server,Database,GRC Architect,Restricted,On-Prem
A003,Admin-Laptop,Endpoint,IT Admin,Internal,Office
A004,BCI-Sensor-Gateway,IoT Device,Research Team,Confidential,Lab
```

💾 Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`)

**3️⃣ Create a users file:**

```bash
nano user_inventory.csv
```

```csv
UserID,Role,AccessLevel,System
U001,Information Assurance Manager,Admin,WebApp-Server
U002,GRC Architect,Admin,DB-Server
U003,Researcher,Read-Only,BCI-Sensor-Gateway
```

💾 Save and exit

**4️⃣ Verify both files exist:**

```bash
ls -l ~/cgrc-lab
cat asset_inventory.csv
cat user_inventory.csv
```

> 📌 **Note:** Snipe-IT (a full CMDB tool) normally requires a web server, PHP, and MySQL. For this basic lab, the CSV inventory approach demonstrates the same CGRC concept — identifying assets, owners, and data sensitivity — without complex server setup.

---

## 🗺️ Task 3: Draw Authorization Boundary and Data Flow Diagrams

**1️⃣ Open draw.io desktop again:**

```bash
./drawio.AppImage
```

**2️⃣ Select `Create New Diagram > Blank Diagram`.**

**3️⃣ Using the shapes panel, build a simple diagram:**

- 🔲 Draw a large **dashed rectangle** labeled `Authorization Boundary`
- 📦 Inside it, place boxes for: `WebApp-Server`, `DB-Server`, `BCI-Sensor-Gateway`
- 📤 Outside the boundary, place a box labeled `Admin-Laptop` (external management access)

**4️⃣ Draw arrows showing data flow:**

| From | To | Label |
|---|---|---|
| Admin-Laptop | WebApp-Server | `HTTPS Management` |
| WebApp-Server | DB-Server | `SQL Query` |
| BCI-Sensor-Gateway | WebApp-Server | `Sensor Data Feed` |

**5️⃣ Save the diagram:**

```
File > Save As > ~/cgrc-lab/authorization_boundary.drawio
```

**6️⃣ Export a PNG copy for the SSP document:**

```
File > Export as > PNG > Save to ~/cgrc-lab/authorization_boundary.png
```

---

## 📝 Task 4: Write the System Characterization Narrative

**1️⃣ Create the narrative file:**

```bash
nano ~/cgrc-lab/system_characterization.md
```

**2️⃣ Use this template** — fill in the blanks based on your inventory and diagram:

```markdown
# System Characterization Narrative

## System Name
[Enter a name, e.g., "BCI Research Data Platform"]

## System Purpose
[Briefly describe what the system does]

## Authorization Boundary
The authorization boundary includes: [list assets inside the boundary from Task 3]
The following are outside the boundary: [list external components]

## Data Classification
- Restricted data: [list assets]
- Confidential data: [list assets]
- Internal data: [list assets]

## Interconnections
[Describe each data flow arrow from your diagram, e.g., "The WebApp-Server connects to the DB-Server via SQL for data storage."]

## Reference
This characterization follows NIST SP 800-37 Rev. 2, Step 1 (Prepare) and Step 2 (Categorize),
which require organizations to define system boundaries before assessing risk and authorizing operation.
```

💾 Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## 📄 Task 5: Produce the SSP Scope Section

**1️⃣ Create the SSP scope file:**

```bash
nano ~/cgrc-lab/ssp_scope_section.md
```

**2️⃣ Fill in this template:**

```markdown
# System Security Plan (SSP) - Scope Section

## 1. System Identification
- System Name: [same as Task 4]
- System Owner: [Information Assurance Manager]

## 2. Authorization Boundary Description
[Copy/summarize from system_characterization.md]
Diagram Reference: authorization_boundary.png

## 3. Asset Inventory Summary
Total Assets: [count from asset_inventory.csv]
Total Users: [count from user_inventory.csv]

## 4. Data Flows and Interconnections
[List each interconnection and its security control, e.g., "HTTPS encryption for Admin-Laptop to WebApp-Server"]

## 5. Applicable Standard
Documented in accordance with NIST SP 800-37 Rev. 2.
```

💾 Save and exit.

---

## ✅ Verification

Confirm your work is complete by running:

```bash
ls -l ~/cgrc-lab
```

You should see these files:

- `asset_inventory.csv`
- `user_inventory.csv`
- `authorization_boundary.drawio`
- `authorization_boundary.png`
- `system_characterization.md`
- `ssp_scope_section.md`

Check file contents are filled in (not empty):

```bash
wc -l ~/cgrc-lab/*.md ~/cgrc-lab/*.csv
```

Each file should show more than 1 line of content.

Open the PNG to visually confirm the diagram exists:

```bash
xdg-open ~/cgrc-lab/authorization_boundary.png
```

---

## 🧠 Key Concepts

| Concept | Description |
|---|---|
| 🛡️ Authorization Boundary | The set of system components and data flows formally accepted for risk assessment and authorization to operate |
| 📦 Asset & Data Inventory | A record of system components, owners, and data sensitivity — the foundation for scoping |
| 🏷️ Data Classification | Categorizing data (e.g., Restricted, Confidential, Internal) to drive protection requirements |
| 🗺️ Data Flow Diagram | Visual mapping of how data moves between components, both inside and outside the boundary |
| 📄 System Security Plan (SSP) | The formal document describing a system's boundary, controls, and characterization for authorization |
| 📘 NIST SP 800-37 | The Risk Management Framework guidance defining the Prepare and Categorize steps that scoping supports |

---

## 🔧 Troubleshooting Tips

<details>
<summary>Click to expand common issues and fixes</summary>

- **draw.io won't launch:** Ensure `libfuse2` is installed and the AppImage has execute permission (`chmod +x`).
- **wget download fails:** Check internet connectivity with `ping github.com`; retry the download.
- **nano commands confusing:** Remember `Ctrl+O` saves, `Ctrl+X` exits; you can also use `gedit` if available as a GUI alternative.
- **CSV file looks wrong when opened:** Open with `cat filename.csv` in terminal to check formatting, or use a spreadsheet app if installed.
- **Diagram export missing:** Ensure you selected "Export as PNG" and chose the correct save folder path.

</details>

---

## 🏁 Conclusion

In this lab, you applied **CGRC Domain 2** concepts by defining the scope of a sample information system on a single Linux machine.

### 🎯 Key Accomplishments
- Installed draw.io desktop for authorization boundary diagramming
- Built a lightweight asset and user inventory using CSV files
- Created an authorization boundary and data flow diagram
- Documented a system characterization narrative referencing NIST SP 800-37
- Produced the scope section of a System Security Plan (SSP)

### 🌍 Real-World Applications
These artifacts represent foundational governance, risk, and compliance documentation used by **Information Assurance Managers** and **GRC Architects** when preparing systems for security authorization.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1E90FF?style=for-the-badge)

</div>
