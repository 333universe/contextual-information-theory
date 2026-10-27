
# Contextual Information Theory (CIT): Tripartite Unitary Matrix (TUM)

[![Verification Sweep](https://github.com)](https://github.com)
[![License: MIT](https://shields.io)](https://opensource.org)

This repository contains the official production reference implementation and empirical verification suite for **Contextual Information Theory (CIT)** using the **Tripartite Unitary Matrix (TUM)** architecture. This replication package is designed to support the peer-review process, allowing reviewers to verify the mathematical phase transitions, bandwidth scaling contraction vectors, and error-hardening limits established in the core manuscript.

## 🔬 Core Mathematical Background

Traditional information metrics rely heavily on passive, uncoupled channel structures. CIT introduces a non-equilibrium thermodynamic perspective, framing the communication link as a self-regulating geometric lattice.

The system capacity is governed by the **NFL-Corrected TUM Capacity Equation**:

\[C_{\text{TUM}} = B_{\text{NFL}} \log_2 \left( 1 + \frac{P_S}{N(1 - \tau) + (1 - \epsilon)P_S \cdot \Omega_{\text{SNR}}} \right)\]

Where:
* **\(B_{\text{NFL}}\)**: The dynamically contracted channel bandwidth governed by structural latency costs (\(B_0 / (1 + \alpha \cdot \text{STM})\)).
* **\(\tau\)**: The Semantic Thermodynamic Torque representing localized structural friction via a Boltzmann partition.
* **\(\epsilon\)**: The Dynamic Matrix Shortfall preserving structural boundary invariants (\(\epsilon \ge 10^{-4}\)).

---

## 📂 Repository Organization

* `src/engine.py`: Core execution protocol embedding denoised subspace projection and anti-symmetric tensor rotation.
* `src/sweeper.py`: Logarithmic multi-regime simulation generator sweeping four orders of noise power magnitude.
* `notebooks/`: Visual playgrounds mirroring the figures used in Section 7 of the manuscript.

---

## 🛠️ Quick Start & Installation

### Prerequisites
Ensure you have Python 3.9+ installed locally.

### 1. Clone the Repository
```bash
git clone https://github.com
cd contextual-information-theory
```

### 2. Set Up Environment & Dependencies
We recommend isolating execution configurations inside a virtual workspace environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Running Verification & Reproducibility Sweeps

To recalculate the parametric data matrices and confirm the second-order thermodynamic phase transition bounds, execute the sweeper module from the repository root:

```bash
python3 src/sweeper.py
```

### Expected Critical Baseline Targets
Upon execution completion, verify that your output terminal metrics conform to the following target validation envelopes:

1. **Regime A (High-Fidelity Optimization Limit):**
   * Target Noise: \(\sim 0.05\)
   * Expected Yield: **\(> 4,500 \text{ bps}\)**
   * Mechanism: Active isolation of structural friction tracking.
2. **Regime B (Catastrophic Guardrail Saturation Limit):**
   * Target Noise: \(\sim 50.0\)
   * Expected Yield: **\(\approx 200 \text{ bps}\)**
   * Mechanism: Smooth activation of the anti-symmetric transformation tensor (\(\mathbf{\Phi}\)), locking the Bit Error Rate to a maximum boundary floor (\(\text{BER} \le 0.5000\)).

---

## 📊 Data Verification Panel

The system automatically generates a publication-ready verification panel tracking the dynamic bandwidth contraction directly against the error-hardening waterfall profile:

```text
output/cit_validation_panel.png
  ├── Panel A: Continuous Second-Order Capacity/BW Collapse
  └── Panel B: Error Floor Hardening vs. Thermodynamic Torque (Tau)
```

---

## 📜 Citation & Peer Review Context
This codebase functions as a verifiable replication artifact for submissions regarding next-gen contextual channel bounds. For anonymous review distributions, identities can be mirrored cleanly via cloud-hosted sandbox environments without breaching double-blind submission rules.
