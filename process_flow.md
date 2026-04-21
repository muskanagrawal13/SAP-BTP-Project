# R2R Process Flow — Detailed Documentation

## Overview

The Record-to-Report (R2R) process is a finance management process that involves collecting, processing, analysing, and delivering accurate financial data. Implemented in SAP FI, it provides an end-to-end, automated workflow from initial transaction capture to statutory reporting and period close.

---

## Step 1: Journal Entry Posting (`FB50`)

**Purpose:** Capture all business transactions as double-entry accounting records.

**Process:**
- Finance user navigates to T-code `FB50` in SAP GUI
- Enters posting date, document type, and company code
- Records debit and credit line items against relevant GL accounts
- Attaches supporting documentation references
- Posts the entry — creating an immutable, time-stamped audit record

**Key Outputs:**
- FI Document Number
- GL Account postings
- Audit trail entry

---

## Step 2: General Ledger Update (`FS10N`)

**Purpose:** Review real-time GL account balances after journal posting.

**Process:**
- Navigate to T-code `FS10N`
- Enter GL account number, company code, and fiscal year
- Review balance per posting period
- Drill down to individual line items as needed

**Key Outputs:**
- Period-by-period account balances
- Cumulative balance view
- Drill-down to source documents

---

## Step 3: Account Reconciliation (`FBL3N`)

**Purpose:** Reconcile GL balances against sub-ledgers (AR, AP, Fixed Assets) to ensure accuracy.

**Process:**
- Navigate to T-code `FBL3N`
- Select GL account(s), company code, and line item status (open/cleared/all)
- Review individual transactions and match against sub-ledger entries
- Identify and investigate discrepancies
- Clear matched items

**Key Outputs:**
- Reconciled GL line items
- Open item list
- Discrepancy report

---

## Step 4: Adjustments & Accruals (`FBS1`)

**Purpose:** Post period-end accrual entries and corrections to ensure the financial period reflects the true financial position.

**Process:**
- Navigate to T-code `FBS1`
- Create accrual/deferral document with reversal date
- Post entries for prepaid expenses, accrued liabilities, and revenue deferrals
- System automatically schedules reversal for the next period

**Key Outputs:**
- Accrual documents
- Scheduled reversal entries
- Adjusted trial balance

---

## Step 5: Financial Statement Preparation (`F.01`)

**Purpose:** Generate statutory Balance Sheet and Profit & Loss statements from reconciled GL data.

**Process:**
- Navigate to T-code `F.01`
- Select financial statement version, company code, and reporting period
- Execute report to generate Balance Sheet and P&L
- Review and validate against prior periods
- Export for management review and statutory filing

**Key Outputs:**
- Balance Sheet
- Profit & Loss Statement
- Comparative period analysis

---

## Step 6: Financial Closing (`OB52`)

**Purpose:** Formally close the accounting period to prevent further postings and preserve financial integrity.

**Process:**
- Navigate to T-code `OB52`
- Review current open/closed posting periods
- Close the current period for all account types (A, D, K, M, S)
- Open the next posting period if required
- Confirm period close with authorized approval

**Key Outputs:**
- Closed posting period
- Locked financial records
- Period-close audit log

---

## End-to-End Flow Summary

```
Business Transaction Occurs
         ↓
FB50 — Post Journal Entry
         ↓
FS10N — Verify GL Balance Updated
         ↓
FBL3N — Reconcile Line Items to Sub-ledgers
         ↓
FBS1 — Post Accruals / Period-End Adjustments
         ↓
F.01 — Generate Financial Statements
         ↓
OB52 — Close Posting Period
         ↓
Period Closed ✅ — Records Locked & Auditable
```
