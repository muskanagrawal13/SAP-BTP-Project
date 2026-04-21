# 📊 Record-to-Report (R2R): End-to-End Financial Closing using SAP FI

> **SAP Capstone Project** — Muskan Agrawal | Roll No: 23052736 | B.Tech CSE | 21 April 2026

---

## 📌 Problem Statement

Many organizations rely on manual or fragmented systems for financial reporting and closing, resulting in:

- Delays in financial closing
- Errors in journal entries and ledger postings
- Lack of real-time financial visibility
- Difficulty in account reconciliation
- Compliance risks and poor audit tracking
- Inefficient and delayed reporting processes
- Data inconsistency across departments

This project implements a centralized, automated R2R cycle within **SAP Financial Accounting (FI)** to manage the full financial lifecycle — from journal entry through statutory reporting — in a single integrated environment.

---

## 🔄 R2R Process Flow

```
Journal Entry Posting (FB50)
        ↓
General Ledger Update (FS10N)
        ↓
Account Reconciliation (FBL3N)
        ↓
Adjustments & Accruals (FBS1)
        ↓
Financial Statement Preparation (F.01)
        ↓
Financial Closing — Month/Year-End (OB52)
```

---

## 🧾 SAP T-Codes Reference

| Step | Activity | SAP T-Code |
|------|----------|------------|
| 1 | Post Journal Entry | `FB50` |
| 2 | Display GL Account | `FS10N` |
| 3 | Line Item Reconciliation | `FBL3N` |
| 4 | Accrual / Adjustment Entry | `FBS1` |
| 5 | Financial Statement Report | `F.01` |
| 6 | Closing Activities (Open/Close Periods) | `OB52` |

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| SAP S/4HANA / ECC | ERP Platform |
| SAP FI | Financial Accounting Module |
| SAP MM / SD | Integrated Procurement & Sales Modules |
| SAP GUI | User Interface |
| SAP Database | Data Storage |

---

## 🔗 SAP Module Integrations

- **SAP FI ↔ SAP MM**: Goods receipts and invoice verifications auto-generate FI postings
- **SAP FI ↔ SAP SD**: Customer invoices and revenue postings flow directly into the General Ledger
- **FI-GL ↔ AR/AP/Fixed Assets**: Real-time subledger reconciliation and integration

---

## ✅ Detailed Step Explanations

### 1. Journal Entry Posting (`FB50`)
Finance users record business transactions via FB50. Each entry captures debit/credit postings to relevant GL accounts, creating an immutable audit record.

### 2. General Ledger Update (`FS10N`)
Journal entries instantly update the General Ledger. FS10N provides real-time account balance views by period for monitoring.

### 3. Account Reconciliation (`FBL3N`)
GL line items are reviewed and reconciled to sub-ledgers (AR, AP, Fixed Assets), ensuring accuracy and eliminating discrepancies.

### 4. Adjustments & Accruals (`FBS1`)
Recurring accrual entries and period-end adjustments are posted via FBS1, ensuring compliance with the accrual basis of accounting.

### 5. Financial Statement Preparation (`F.01`)
SAP standard report F.01 generates Balance Sheet and Profit & Loss statements directly from reconciled GL data.

### 6. Financial Closing (`OB52`)
OB52 manages posting period controls — opening and closing accounting periods. Once verified, the period is formally closed to prevent further postings.

---

## 🌟 Key Highlights

- ✅ Full financial lifecycle coverage: journal entry → statutory reporting → period close
- ✅ Real-time GL updates on every posting
- ✅ Tight FI/MM/SD integration — no manual data transfers
- ✅ Automated three-way matching reduces audit risk
- ✅ Period-end controls via OB52 prevent unauthorised backdating
- ✅ End-to-end transaction visibility for informed decision-making

---

## 🚀 Future Improvements

- AI-based financial forecasting models for budget accuracy and variance prediction
- ML-driven automated account reconciliation
- Real-time analytics dashboard for financial KPIs and closing timelines
- Migration to cloud-based SAP S/4HANA Finance
- Direct API integration with external financial tools and tax/regulatory platforms

---

## 📁 Project Structure

```
r2r-sap-project/
├── README.md               # Project overview and documentation
├── LICENSE                 # MIT License
├── CHANGELOG.md            # Version history
├── .gitignore              # Git ignore rules
├── docs/
│   ├── process_flow.md     # Detailed R2R process flow documentation
│   ├── tcodes_reference.md # SAP T-Codes quick reference guide
│   └── integration.md      # SAP module integration documentation
└── scripts/
    ├── r2r_checklist.py    # Python R2R closing checklist utility
    └── tcode_lookup.py     # SAP T-Code lookup tool
```

---

## 📜 Declaration

I hereby declare that the content presented in this project report is entirely my own academic work. No portion of this submission has been reproduced or adapted from the work of peers, seniors, or any online repository.

**Name:** Muskan Agrawal | **Roll No:** 23052736 | **Branch:** B.Tech CSE | **Date:** 21 April 2026

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
