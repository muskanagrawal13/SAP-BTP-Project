# SAP Module Integration — R2R Project

## Overview

The R2R process relies on seamless real-time integration between SAP FI and other core SAP modules. This document describes the key integration points.

---

## SAP FI ↔ SAP MM (Materials Management)

**Trigger:** Goods Receipt or Invoice Verification in MM

**Flow:**
```
MM: Goods Receipt (MIGO)
        ↓
Automatic FI Posting Created
        ↓
FI: GL Account Debited (Inventory / GR/IR Account)
        ↓
MM: Invoice Verification (MIRO)
        ↓
FI: AP Vendor Account Updated
```

**Key Points:**
- No manual FI entry required — MM drives the posting automatically
- GR/IR (Goods Receipt / Invoice Receipt) account acts as a clearing account
- Three-way matching: PO ↔ GR ↔ Invoice

---

## SAP FI ↔ SAP SD (Sales & Distribution)

**Trigger:** Customer Billing in SD

**Flow:**
```
SD: Sales Order Created (VA01)
        ↓
SD: Delivery & Goods Issue (VL01N)
        ↓
Automatic FI Posting: COGS Debited, Inventory Credited
        ↓
SD: Billing Document Created (VF01)
        ↓
Automatic FI Posting: AR Debited, Revenue Credited
        ↓
FI: GL Updated in Real Time
```

**Key Points:**
- Revenue recognition is triggered automatically from SD billing
- AR sub-ledger updated simultaneously with GL
- Eliminates manual reconciliation between sales and finance

---

## FI-GL Sub-Ledger Integrations

### Accounts Receivable (FI-AR)
- Every customer invoice and payment posts to both the AR sub-ledger and the GL reconciliation account
- T-code `FBL5N` for line item display

### Accounts Payable (FI-AP)
- Every vendor invoice and payment posts to both the AP sub-ledger and the GL reconciliation account
- T-code `FBL1N` for line item display

### Fixed Assets (FI-AA)
- Asset acquisitions, depreciation runs, and disposals post automatically to GL
- Depreciation run via T-code `AFAB`

---

## Integration Architecture Summary

```
        ┌─────────┐      ┌─────────┐
        │  SAP MM │      │  SAP SD │
        └────┬────┘      └────┬────┘
             │  Auto-posting  │
             ▼                ▼
        ┌─────────────────────────┐
        │        SAP FI           │
        │  ┌──────────────────┐   │
        │  │   General Ledger │   │
        │  └──────────────────┘   │
        │  ┌────┐ ┌────┐ ┌─────┐  │
        │  │ AR │ │ AP │ │ AA  │  │
        │  └────┘ └────┘ └─────┘  │
        └─────────────────────────┘
                    │
                    ▼
           Financial Reports
           (F.01 — Balance Sheet / P&L)
```
