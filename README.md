# TitanAI – Secure Fraud Detection for Digital Payments

## Overview
TitanAI is a fraud detection system built for modern digital payment platforms such as **UPI, cards, and online transactions**.  
It acts as a **fraud-risk and decision layer** that analyzes transactions in real time and helps platforms take safe and informed actions.

The project focuses on **practical fintech problems**, keeping the design realistic, secure, and easy to explain during a hackathon.

---

## Problem Statement
Digital payments in India are growing rapidly, especially through UPI.  
At the same time, fraud cases are increasing due to evolving attack patterns.

Most existing systems still depend heavily on rule-based checks, which:
- **Fail to detect** new fraud patterns.
- **Generate too many false alerts**, affecting genuine users.
- **Create operational and compliance challenges**.

There is a need for a **secure, intelligent, and real-time fraud detection layer** that supports today’s fintech systems.

---

## What is TitanAI?
TitanAI is an AI-powered fraud detection platform that:
- Monitors transactions.
- Assigns a fraud risk score.
- Helps decide whether a transaction should be approved, challenged, or blocked.

It is designed to **support banks and payment apps**, not replace existing payment infrastructure. You can think of TitanAI as a **smart security layer added on top of digital payment systems**.

---

## How TitanAI Works

The following flowchart illustrates how a transaction moves from a request to a final decision through the TitanAI engine:

![TitanAI Fraud Risk Scoring Flow](images/AI%20Fraud%20Decision%20%26%20Risk%20Scoring%20Flow.png)

### The Logic Flow:
1. **Payment Request** (Initiated by user)
2. **Encrypted Channel** (Secured via TLS)
3. **AI Fraud Scoring Engine** (Analysis of patterns)
4. **Risk-Based Decision** (Approve / OTP Challenge / Block)

---

## Why TitanAI Is Relevant to UPI (Real World)
To understand TitanAI’s relevance, it is important to know how UPI actually works.

### How UPI Systems Operate
UPI transactions involve multiple entities including Banks, NPCI, and PSP apps (GPay, PhonePe, Paytm). Fraud detection is **not handled by NPCI alone**. Each bank and payment app runs its **own internal fraud and risk engines**.

👉 **TitanAI fits exactly at this level** — as an internal fraud-risk engine for banks or PSPs.

---

## System Architecture

TitanAI is built to handle data efficiently across different layers, ensuring low latency and high security.

![Transaction Fraud Detection Timeline](TitanAI/images/Transaction%20Fraud%20Detection%20Timeline.png)

### The Pipeline:
* **Client / Dashboard:** The interface for monitoring.
* **API Gateway:** Routes requests securely using TLS.
* **Flask Backend:** The core logic of TitanAI.
* **ML Fraud Engine:** Processes data using Scikit-learn.
* **Transaction Ledger:** Stores the audit trail for compliance.

---

## Key Features
- **Secure Communication:** Using TLS encryption for all data in transit.
- **ML Risk Scoring:** Uses Isolation Forest and Random Forest for pattern recognition.
- **Explainable AI:** Provides clear reasoning for why a transaction was flagged.
- **KYC-Aware:** Evaluates risk based on user history and verification status.
- **Audit-Friendly:** Maintains a detailed ledger for regulatory compliance.

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Chart.js for visualization)
- **Backend:** Python with Flask
- **Machine Learning:** Scikit-learn (Isolation Forest, Random Forest)
- **Security:** TLS (HTTPS), JWT Authentication
- **Database:** PostgreSQL (SQLite for demo/testing)
- **Deployment:** Git, GitHub, Docker (optional)

---

## Project Objective
The objective of TitanAI is to build a **realistic and reliable fraud detection layer** that:
- Reduces fraud in digital payments.
- Minimizes false alerts.
- Improves trust in UPI and fintech platforms.
- Aligns with real-world banking practices.

---

## Why TitanAI Works Well in a Hackathon
- **Real-World Impact:** Solves a current fintech problem in India.
- **Feasibility:** Technically achievable within hackathon timelines.
- **Professional Design:** Demonstrates industry-level thinking regarding security and compliance.

---

## Conclusion
TitanAI shows how AI and security can be combined to support real-world digital payment systems. The project is practical, well-scoped, and aligned with how fintech systems actually operate today.

### One-Line Summary
**TitanAI is a secure, AI-based fraud detection layer that supports UPI and digital payment platforms by identifying risky transactions in real time.**
