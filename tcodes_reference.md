# SAP T-Codes Quick Reference — R2R Process

## Core R2R T-Codes

| T-Code | Transaction Name | Module | R2R Step |
|--------|-----------------|--------|----------|
| `FB50` | Enter G/L Account Document | FI-GL | 1 — Journal Entry Posting |
| `FS10N` | G/L Account Balance Display | FI-GL | 2 — General Ledger Update |
| `FBL3N` | G/L Account Line Items | FI-GL | 3 — Account Reconciliation |
| `FBS1` | Enter Accrual/Deferral Document | FI-GL | 4 — Adjustments & Accruals |
| `F.01` | Financial Statements | FI-GL | 5 — Financial Statement Prep |
| `OB52` | Posting Periods | FI | 6 — Financial Closing |

---

## Supporting T-Codes

| T-Code | Description | Use Case |
|--------|-------------|----------|
| `FB03` | Display Document | View any posted FI document |
| `FB08` | Reverse Document | Reverse an incorrect posting |
| `FBV0` | Post Parked Document | Complete and post a parked entry |
| `F-02` | Enter G/L Account Posting | Alternative GL entry screen |
| `FS00` | G/L Account Master Data | View/change GL account settings |
| `FBL1N` | Vendor Line Items | AP sub-ledger reconciliation |
| `FBL5N` | Customer Line Items | AR sub-ledger reconciliation |
| `F.13` | Automatic Clearing | Auto-clear open items |
| `GR55` | Execute Report Group | Run custom financial reports |
| `S_ALR_87012284` | Financial Statements | Alternative financial reporting |

---

## Period Management T-Codes

| T-Code | Description |
|--------|-------------|
| `OB52` | Open and Close Posting Periods |
| `OBH2` | Copy Posting Period Variants |
| `SM30` | Maintain Table Entries (period config) |

---

## Tips

- Always check `OB52` before period-end to confirm which periods are open
- Use `FB03` to verify any document before reconciliation
- `FBL3N` with status = "All items" gives the most complete reconciliation view
- Run `F.01` in simulation mode first to validate before final reporting
