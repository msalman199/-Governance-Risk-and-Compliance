# 🎲 Risk Quantification with FAIR & Monte Carlo

### 🛡️ Quantitative Cyber Risk • FAIR Taxonomy • Monte Carlo Simulation • Loss Exceedance Curves • CGRC

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge\&logo=numpy\&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Statistics-8CAAE6?style=for-the-badge\&logo=scipy\&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge\&logo=plotly\&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white)](https://jupyter.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)](https://ubuntu.com/)
[![FAIR](https://img.shields.io/badge/FAIR-Risk%20Analysis-6A1B9A?style=for-the-badge)](https://www.fairinstitute.org/)

> 🚀 **Hands-on quantitative cyber-risk engineering lab**
>
> Build a FAIR-inspired quantitative risk model, represent uncertainty with probability distributions, run vectorized Monte Carlo simulations, generate Loss Exceedance Curves, and translate statistical results into an executive-ready risk treatment recommendation.

---

# 🌟 Project Overview

This lab demonstrates how to transform a qualitative cybersecurity scenario into a **quantitative financial risk model**.

The scenario used throughout the lab is:

> 🔐 **Unauthorized access to a cloud-hosted patient records database due to compromised third-party vendor credentials.**

The analysis follows the FAIR risk model:

```text
                 🎯 RISK SCENARIO
                       │
              ┌────────┴────────┐
              ▼                 ▼
        📈 Loss Event       💰 Loss
         Frequency         Magnitude
              │                 │
        ┌─────┴─────┐      ┌────┴─────┐
        ▼           ▼      ▼          ▼
       TEF      Vulnerability  Primary   Secondary
                    │         Loss       Loss
              ┌─────┴─────┐
              ▼           ▼
        Threat Capability  Control Strength
```

Monte Carlo simulation then converts these uncertain factors into a distribution of possible **Annualized Loss Exposure (ALE)**.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 🧠 Decompose cyber risk using FAIR taxonomy.
* 📊 Model uncertainty using probability distributions.
* 🎲 Implement Monte Carlo simulation.
* 📈 Calculate Annualized Loss Exposure.
* 📉 Generate Loss Exceedance Curves.
* 💵 Calculate P10, P50, P90, P95 and tail-risk metrics.
* 🔬 Perform sensitivity analysis.
* 🛡️ Quantify the financial impact of improved controls.
* 👔 Translate quantitative risk into executive language.
* 📋 Produce a report aligned with CGRC risk assessment and communication requirements.

---

# 🧰 Technology Stack

## 💻 Core Technologies

| Technology          | Purpose                                  |
| ------------------- | ---------------------------------------- |
| 🐍 **Python 3.10+** | Risk-model implementation                |
| 🎲 **NumPy**        | Vectorized Monte Carlo simulation        |
| 📊 **Pandas**       | Data manipulation and reporting          |
| 🧮 **SciPy**        | Probability distributions and statistics |
| 📈 **Matplotlib**   | LEC and sensitivity charts               |
| 📓 **JupyterLab**   | Interactive risk modeling                |
| 🐧 **Ubuntu Linux** | Lab environment                          |
| 🧩 **PyFAIR**       | Optional FAIR implementation             |
| 📄 **Pandoc**       | Optional PDF/report conversion           |

---

# 📋 Prerequisites

Before starting, you should have:

* 🟢 Working Python knowledge.
* 🟢 Familiarity with `numpy` and `pandas`.
* 🟢 Understanding of Python functions and classes.
* 🟢 Understanding of FAIR terminology.
* 🟢 Knowledge of probability distributions.
* 🟢 Basic Linux CLI skills.
* 🟢 Understanding of cybersecurity risk assessment.
* 🟢 Basic knowledge of CGRC risk reporting.

---

# 🧠 FAIR Concepts Used

This lab focuses on:

| FAIR Factor                        | Meaning                                              |
| ---------------------------------- | ---------------------------------------------------- |
| 🎯 **TEF**                         | Threat Event Frequency                               |
| 🛡️ **Vulnerability**              | Probability that a threat event becomes a loss event |
| ⚔️ **Threat Capability**           | Capability of the threat actor                       |
| 🔐 **Control/Resistance Strength** | Organization's ability to resist the threat          |
| 📈 **LEF**                         | Loss Event Frequency                                 |
| 💰 **Primary Loss**                | Direct organizational loss                           |
| 💸 **Secondary Loss**              | Loss caused by external stakeholders                 |
| 💵 **LM**                          | Loss Magnitude                                       |
| 📊 **ALE**                         | Annualized Loss Exposure                             |

Core relationships:

```text
Vulnerability
      =
f(Threat Capability, Control Strength)

LEF
      =
TEF × Vulnerability

LM
      =
Primary Loss + Secondary Loss

ALE
      =
LEF × LM
```

---

# 🚀 STEP 0 — Environment Setup

### 🟢 Objective

Create an isolated Python environment and install the quantitative-risk toolchain.

---

## 🐧 Install Linux Packages

```bash
sudo apt update

sudo apt install -y \
    python3-pip \
    python3-venv \
    git
```

---

## 🐍 Create Virtual Environment

```bash
python3 -m venv fair-env

source fair-env/bin/activate
```

Your terminal should now show something similar to:

```text
(fair-env) user@linux:~$
```

---

## 📦 Install Dependencies

```bash
pip install --upgrade pip

pip install \
    jupyterlab \
    numpy \
    pandas \
    matplotlib \
    scipy \
    pyfair
```

---

## 🔍 Validate Installation

```bash
python3 -c "import numpy, pandas, scipy, matplotlib; print('Risk stack OK')"
```

If PyFAIR is installed:

```bash
python3 -c "import pyfair; print(pyfair.__version__)"
```

> 🟡 **Fallback:** If `pyfair` is unavailable or outdated, implement the FAIR calculations directly using NumPy and SciPy. This is an acceptable and encouraged architectural decision for the lab.

---

## 📓 Launch JupyterLab

```bash
jupyter lab \
    --no-browser \
    --ip=0.0.0.0 \
    --port=8888
```

---

### 🎉 Success Indicator

```text
╔══════════════════════════════════════════╗
║                                          ║
║       ✅ STEP 0 — ENVIRONMENT READY      ║
║                                          ║
║  🐍 Python       → READY                 ║
║  🎲 NumPy        → READY                 ║
║  🧮 SciPy        → READY                 ║
║  📊 Pandas       → READY                 ║
║  📈 Matplotlib   → READY                 ║
║  📓 Jupyter      → READY                 ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 🎯 STEP 1 — Scenario Decomposition

### 🔵 Objective

Convert the cybersecurity scenario into measurable FAIR factors.

## 🔐 Scenario

**Unauthorized access to a cloud-hosted patient records database due to compromised third-party vendor credentials.**

---

## 🧩 FAIR Decomposition

```text
                    🔐 CLOUD DATABASE BREACH
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
       📈 LOSS EVENT                       💰 LOSS
        FREQUENCY                         MAGNITUDE
             │                                 │
       ┌─────┴─────┐                     ┌─────┴─────┐
       ▼           ▼                     ▼           ▼
      TEF      Vulnerability          Primary    Secondary
                   │                   Loss         Loss
              ┌────┴────┐
              ▼         ▼
           Threat    Control
         Capability  Strength
```

---

# 📊 Build the Factor Table

Create a CSV or Python dictionary containing:

| Factor            | Minimum | Most Likely | Maximum | Distribution            | Reasoning                      |
| ----------------- | ------: | ----------: | ------: | ----------------------- | ------------------------------ |
| TEF               |  Define |      Define |  Define | Lognormal/Poisson       | Historical/threat intelligence |
| Threat Capability |  Define |      Define |  Define | PERT                    | Threat assessment              |
| Control Strength  |  Define |      Define |  Define | PERT                    | Control maturity               |
| Primary Loss      |  Define |      Define |  Define | PERT/Lognormal          | Recovery and response          |
| Secondary Loss    |  Define |      Define |  Define | PERT/Lognormal          | Regulatory/reputation impact   |
| SLEF              |  Define |      Define |  Define | Conditional probability | Stakeholder response           |

> ⚠️ Do not simply invent numbers without explanation. Every estimate should have an assumption, source, expert calibration, or documented estimation rationale.

---

# 💰 STEP 2 — Model Loss Magnitude

Separate losses into two major categories.

## 🟢 Primary Loss

Potential direct costs include:

* 🚨 Incident response.
* 🔧 System recovery.
* 🧑‍💻 Forensic investigation.
* 🖥️ Infrastructure restoration.
* ⚖️ Legal response.
* 📋 Internal remediation.

---

## 🟠 Secondary Loss

Potential indirect/external costs include:

* 🏛️ Regulatory penalties.
* 📣 Notification costs.
* 🤝 Customer attrition.
* ⭐ Reputational damage.
* ⚖️ Litigation.
* 📉 Lost business.
* 🛡️ Additional compliance requirements.

For GCC scenarios, regulatory assumptions should be documented carefully and validated against the applicable jurisdiction and sector.

---

# 🎲 STEP 3 — Distribution Design

### 🟣 Objective

Represent uncertainty rather than pretending that risk has one exact value.

---

## 📊 Recommended Distributions

| FAIR Variable     | Distribution        | Reason                        |
| ----------------- | ------------------- | ----------------------------- |
| TEF               | Poisson / Lognormal | Event frequency               |
| Threat Capability | PERT / Beta         | Bounded capability            |
| Control Strength  | PERT / Beta         | Bounded resistance            |
| Primary Loss      | PERT / Lognormal    | Right-skewed financial impact |
| Secondary Loss    | PERT / Lognormal    | Uncertain external impact     |
| SLEF              | Probability         | Conditional event             |

---

# 🧮 PERT Distribution

SciPy does not provide a dedicated PERT distribution.

Implement PERT using a Beta distribution.

A common parameterization is:

```text
alpha = 1 + λ × (mode - min) / (max - min)

beta  = 1 + λ × (max - mode) / (max - min)
```

Then transform:

```text
PERT Sample
     ↓
Beta(alpha, beta)
     ↓
[min, max]
```

---

# 🐍 Reusable Risk Node

Create:

```text
risk_model.py
```

Example:

```python
from dataclasses import dataclass
import numpy as np


@dataclass
class FairNode:
    name: str
    dist_type: str
    params: dict

    def sample(self, n: int) -> np.ndarray:
        """
        Generate n Monte Carlo samples.
        """
        raise NotImplementedError
```

Supported distribution types should include:

```text
pert
lognormal
poisson
triangular
beta
```

---

# 🧱 STEP 4 — Build the FAIR Risk Model

### 🔵 Objective

Compose individual uncertainty distributions into a complete risk model.

The model should calculate:

```text
Threat Capability
        +
Control Strength
        ↓
Vulnerability
        ↓
TEF × Vulnerability
        ↓
       LEF
        │
        ▼
Primary Loss + Secondary Loss
        │
        ▼
       LM
        │
        ▼
   LEF × LM
        │
        ▼
       ALE
```

---

## 🐍 Model Interface

```python
from typing import Callable


def build_risk_model(
    nodes: dict[str, FairNode]
) -> Callable[[int], np.ndarray]:
    """
    Return a callable that generates ALE samples.
    """
    pass
```

The implementation should be vectorized.

### 🚫 Avoid

```python
for i in range(50000):
    ...
```

### ✅ Prefer

```python
samples = rng.random(50000)
```

or vectorized NumPy/SciPy operations.

---

# 🎲 STEP 5 — Monte Carlo Simulation

### 🟢 Objective

Run thousands of simulated risk scenarios to estimate the distribution of annualized loss.

Recommended range:

```text
10,000 → 100,000 iterations
```

Recommended default:

```text
50,000 iterations
```

---

## 🐍 Simulation Function

```python
def run_simulation(
    model,
    iterations: int = 50000
) -> np.ndarray:
    """
    Return ALE samples.
    """
    pass
```

---

## 📊 Required Metrics

Calculate:

```text
P10
P50
P90
P95
Mean
Maximum
```

Example:

```python
np.percentile(
    ale_samples,
    [10, 50, 90, 95]
)
```

---

# ⚠️ STEP 6 — Handle Simulation Edge Cases

### 🔴 Negative Values

Financial losses cannot normally be negative.

Clip or reject non-physical values:

```python
ale_samples = np.maximum(ale_samples, 0)
```

---

## 🐘 Heavy-Tailed Results

Cyber losses can be strongly right-skewed.

Therefore, never report only the mean.

Use:

```text
Median
P90
P95
Tail statistics
```

Example:

```text
Mean ALE      → $X
Median ALE    → $Y
P90 ALE       → $Z
P95 ALE       → $W
```

---

# 📉 STEP 7 — Generate the Loss Exceedance Curve

### 🟣 Objective

Show the probability that annual loss exceeds a given dollar value.

A Loss Exceedance Curve answers:

> **"What is the probability that annual loss will exceed $X?"**

---

## 📈 LEC Concept

```text
Probability
100% ┤╲
     │ ╲
 80% ┤  ╲
     │   ╲
 60% ┤    ╲
     │     ╲
 40% ┤      ╲
     │       ╲
 20% ┤         ╲
     │           ╲
  0% └──────────────────────
        Loss ($)
```

The curve should monotonically decrease.

---

## 🐍 LEC Function

```python
def plot_loss_exceedance_curve(
    ale_samples: np.ndarray,
    save_path: str
) -> None:
    """
    Create and save a Loss Exceedance Curve.
    """
    pass
```

---

## 📊 Calculation

Sort loss values:

```python
losses = np.sort(ale_samples)
```

Calculate exceedance probabilities based on empirical ranks.

Then plot:

```text
X = Loss
Y = Probability of Exceedance
```

Save:

```text
loss_exceedance_curve.png
```

---

# 📌 STEP 8 — Annotate P90 and P95

The LEC should clearly identify important risk thresholds.

Example:

```text
        Probability
            │
       10% ─┤──────● P90
            │       │
        5% ─┤───────● P95
            │
            └────────────────── Loss
```

The report should state these values in plain language.

For example:

> **The modeled 95th-percentile annual loss is approximately $X, meaning 95% of simulated annual losses are at or below that value under the model assumptions.**

---

# 🔬 STEP 9 — Control Improvement & Sensitivity Analysis

### 🟢 Objective

Quantify the financial value of improving security controls.

Baseline:

```text
Control Strength = Current State
```

Improved scenario:

```text
Control Strength = Current State + 20%
```

Run the simulation again.

---

## 📊 Compare

Generate:

```text
Baseline LEC
       VS
Improved Control LEC
```

Example:

```text
Loss
 ▲
 │  ╲ Baseline
 │   ╲
 │    ╲
 │     ╲ Improved
 │      ╲
 └──────────────────► Probability
```

---

## 💡 Control ROI

Calculate:

```text
Risk Reduction
=
Baseline ALE - Improved ALE
```

Then compare against control implementation cost:

```text
Net Risk Benefit
=
Risk Reduction - Control Cost
```

This provides an evidence-based foundation for mitigation decisions.

---

# 👔 STEP 10 — Executive Risk Report

### 🟠 Objective

Translate statistical output into a concise executive report.

Create:

```text
risk_report.md
```

or:

```text
risk_report.pdf
```

---

# 📑 Required Report Sections

## 1. Executive Summary

Keep this to approximately 2–3 sentences.

Example structure:

```text
The modeled annualized financial exposure for the scenario is approximately $X at
the median and $Y at the 95th percentile. Improving control strength by 20%
reduces modeled exposure by approximately $Z, supporting investment in the
proposed mitigation.
```

---

## 2. Scenario Description

Explain:

* What happened.
* Who the threat actor is.
* What asset is affected.
* Why the third-party relationship matters.
* What data is exposed.

---

## 3. FAIR Factor Table

Include:

| Factor            | Distribution | Min | Mode | Max | Rationale        |
| ----------------- | ------------ | --: | ---: | --: | ---------------- |
| TEF               | Lognormal    |   X |    X |   X | Assumption       |
| Threat Capability | PERT         |   X |    X |   X | Assessment       |
| Control Strength  | PERT         |   X |    X |   X | Control maturity |
| Primary Loss      | PERT         |  $X |   $X |  $X | Cost estimate    |
| Secondary Loss    | PERT         |  $X |   $X |  $X | Impact estimate  |

---

## 4. Loss Exceedance Curve

Embed:

```text
loss_exceedance_curve.png
```

Annotate:

* P50.
* P90.
* P95.

---

## 5. Control Improvement Comparison

Include:

```text
Baseline
   VS
+20% Control Strength
```

Show:

* Median reduction.
* P90 reduction.
* P95 reduction.
* Estimated annualized risk reduction.

---

# 🛡️ STEP 11 — Risk Treatment Recommendation

Use standard risk treatment options:

```text
🟢 ACCEPT
🟡 MITIGATE
🔵 TRANSFER
🔴 AVOID
```

---

## 🟡 MITIGATE

Recommended when:

```text
Risk Reduction > Control Cost
```

---

## 🔵 TRANSFER

Potential mechanisms:

* Cyber insurance.
* Contractual risk transfer.
* Vendor liability provisions.

---

## 🟢 ACCEPT

Appropriate when:

```text
Residual Risk
<
Risk Appetite
```

and the mitigation cost is disproportionate.

---

## 🔴 AVOID

Appropriate when the organization can eliminate the activity or architecture causing unacceptable exposure.

---

# 📊 STEP 12 — Assumptions & Limitations

Every quantitative risk report should explicitly document uncertainty.

Include:

### 📌 Calibration Confidence

Explain whether estimates are:

* Historical.
* Industry-derived.
* Expert-elicited.
* Scenario-based.

### 📌 Data Quality

Document:

* Sample size.
* Missing historical events.
* Financial uncertainty.
* Distribution assumptions.

### 📌 Model Limitations

State that:

* Monte Carlo produces modeled estimates, not guarantees.
* Results depend on input distributions.
* Correlations between variables may materially affect results.
* Regulatory and litigation outcomes are uncertain.
* Extreme-tail events may be underrepresented.

---

# 🔍 STEP 13 — Verification

### 🧪 Verify Project Files

```bash
ls *.ipynb risk_report.md loss_exceedance_curve.png
```

Expected:

```text
risk_analysis.ipynb
risk_report.md
loss_exceedance_curve.png
```

---

## 💾 Verify Simulation Output

Save samples:

```text
ale_samples.npy
```

Then:

```bash
python3 -c \
"import numpy as np; a=np.load('ale_samples.npy'); print(a.mean(), np.percentile(a,[50,90,95]))"
```

---

## 📓 Execute Notebook Automatically

```bash
jupyter nbconvert \
    --execute \
    --to notebook \
    risk_analysis.ipynb
```

The notebook must execute from start to finish without errors.

---

# ✅ Verification Checklist

```text
☑️ Python environment works
☑️ NumPy/SciPy installed
☑️ FAIR factors documented
☑️ Probability distributions implemented
☑️ Monte Carlo simulation executes
☑️ 10,000+ iterations completed
☑️ ALE distribution generated
☑️ P10 calculated
☑️ P50 calculated
☑️ P90 calculated
☑️ P95 calculated
☑️ LEC generated
☑️ LEC monotonically decreases
☑️ P90/P95 annotated
☑️ Control sensitivity completed
☑️ Risk reduction quantified
☑️ Executive report generated
```

---

# 🏆 FINAL SUCCESS SCREEN

```text
╔══════════════════════════════════════════════════════╗
║                                                      ║
║       🎲 FAIR QUANTITATIVE RISK LAB COMPLETE         ║
║                                                      ║
║   🧠 FAIR Model              ✅                      ║
║   📊 Probability Models      ✅                      ║
║   🎲 Monte Carlo             ✅                      ║
║   💰 ALE Calculation         ✅                      ║
║   📉 Loss Exceedance Curve   ✅                      ║
║   🔬 Sensitivity Analysis    ✅                      ║
║   🛡️ Control ROI             ✅                      ║
║   👔 Executive Report        ✅                      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

---

# 🏗️ Solution Architecture

```text
                 🔐 CYBER RISK SCENARIO
                          │
                          ▼
                 🧠 FAIR DECOMPOSITION
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    📈 LOSS EVENT                    💰 LOSS
     FREQUENCY                      MAGNITUDE
          │                               │
     ┌────┴────┐                     ┌────┴────┐
     ▼         ▼                     ▼         ▼
    TEF    Vulnerability          Primary   Secondary
              │                    Loss       Loss
        ┌─────┴─────┐
        ▼           ▼
     Threat      Control
   Capability   Strength
          │
          ▼
       🎲 MONTE CARLO
          │
          ▼
     📊 ALE SAMPLES
          │
     ┌────┴────┐
     ▼         ▼
  PERCENTILES  LEC
     │         │
     └────┬────┘
          ▼
   🔬 SENSITIVITY ANALYSIS
          │
          ▼
   🛡️ CONTROL ROI
          │
          ▼
     👔 EXECUTIVE
       REPORT
```

---



---

# 🚀 Advanced Extensions

After completing the core lab, consider implementing:

* 🔗 Correlated FAIR factors.
* 🎲 Latin Hypercube Sampling.
* 🧮 Bayesian parameter estimation.
* 📈 Multiple LEC scenarios.
* 🏢 Business-unit-specific risk models.
* ☁️ Cloud/vendor concentration risk.
* 📊 Interactive Plotly dashboards.
* 🤖 Automated risk narratives.
* 💵 Control-cost optimization.
* 🔄 Continuous risk monitoring.
* 📡 Threat-intelligence-driven TEF updates.
* 📋 Automated CGRC evidence generation.

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

```text
🐍 Python Engineering
        ↓
🧠 FAIR Risk Modeling
        ↓
🎲 Probability Distributions
        ↓
📊 Monte Carlo Simulation
        ↓
📈 Quantitative Risk Analysis
        ↓
📉 Loss Exceedance Curves
        ↓
🔬 Sensitivity Analysis
        ↓
💵 Control ROI
        ↓
👔 Executive Risk Communication
        ↓
🛡️ CGRC Risk Management
```

---

# ⚠️ Important Modeling Disclaimer

This laboratory exercise is intended for **educational and risk-engineering practice**.

The numerical results generated by the model are not predictions or guarantees. They are conditional estimates based on the assumptions, distributions, dependencies, and data used in the simulation.

For production risk decisions:

* Validate assumptions with subject-matter experts.
* Use reliable historical and actuarial data where available.
* Document estimation methods.
* Review distribution choices.
* Model dependencies and correlations where appropriate.
* Recalibrate inputs as new evidence becomes available.
* Clearly distinguish modeled risk from realized loss.
* Have appropriate risk, legal, compliance, and financial stakeholders review material decisions.

---

# 🏁 Conclusion

This lab provides a complete quantitative cyber-risk workflow:

```text
🔐 Scenario
    ↓
🧠 FAIR Taxonomy
    ↓
📊 Probability Distributions
    ↓
🎲 Monte Carlo
    ↓
💰 Annualized Loss Exposure
    ↓
📉 Loss Exceedance Curve
    ↓
🔬 Control Sensitivity
    ↓
💵 Risk Reduction / ROI
    ↓
👔 Executive Recommendation
```

By completing the lab, you will have built an end-to-end **FAIR-inspired quantitative risk analysis pipeline** using open-source Python tooling.

You will have demonstrated the ability to move from an uncertain cybersecurity scenario to a defensible financial risk distribution, visualize tail exposure, evaluate control improvements, and communicate the results in language suitable for executive decision-making.

## 🏆 Final Outcome

> **Measure the uncertainty. Quantify the exposure. Compare the controls. Communicate the decision.**

### 🛡️ FAIR + Monte Carlo + CGRC = Quantitative Cyber Risk Engineering
