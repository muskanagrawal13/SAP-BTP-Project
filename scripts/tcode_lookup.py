"""
tcode_lookup.py
===============
A simple command-line SAP T-Code lookup tool for the R2R process.

Usage:
    python tcode_lookup.py
    python tcode_lookup.py FB50
"""

import sys

# ── T-Code Database ──────────────────────────────────────────────────────────

TCODES = {
    # Core R2R T-Codes
    "FB50": {
        "name": "Enter G/L Account Document",
        "module": "FI-GL",
        "category": "Journal Entry",
        "description": "Post a journal entry directly to GL accounts. Used for manual financial postings, corrections, and period-end entries.",
        "r2r_step": "Step 1 — Journal Entry Posting",
    },
    "FS10N": {
        "name": "G/L Account Balance Display",
        "module": "FI-GL",
        "category": "Reporting",
        "description": "Display GL account balances by period. Provides real-time view of account positions for monitoring and review.",
        "r2r_step": "Step 2 — General Ledger Update",
    },
    "FBL3N": {
        "name": "G/L Account Line Items",
        "module": "FI-GL",
        "category": "Reconciliation",
        "description": "Display and manage GL account line items. Used for reconciliation of open items and sub-ledger matching.",
        "r2r_step": "Step 3 — Account Reconciliation",
    },
    "FBS1": {
        "name": "Enter Accrual/Deferral Document",
        "module": "FI-GL",
        "category": "Period-End",
        "description": "Post accrual and deferral entries with automatic reversal dates. Ensures period reflects true financial position.",
        "r2r_step": "Step 4 — Adjustments & Accruals",
    },
    "F.01": {
        "name": "Financial Statements",
        "module": "FI-GL",
        "category": "Reporting",
        "description": "Generate Balance Sheet and Profit & Loss statements from GL data. Key statutory reporting tool.",
        "r2r_step": "Step 5 — Financial Statement Preparation",
    },
    "OB52": {
        "name": "Posting Periods",
        "module": "FI",
        "category": "Period Management",
        "description": "Open and close accounting posting periods. Controls which periods are available for postings by account type.",
        "r2r_step": "Step 6 — Financial Closing",
    },
    # Supporting T-Codes
    "FB03": {
        "name": "Display Document",
        "module": "FI",
        "category": "Document Management",
        "description": "Display any posted FI accounting document. Useful for audit and verification.",
        "r2r_step": "Supporting — Document Review",
    },
    "FB08": {
        "name": "Reverse Document",
        "module": "FI",
        "category": "Document Management",
        "description": "Reverse a previously posted FI document. Creates an offsetting reversal document.",
        "r2r_step": "Supporting — Corrections",
    },
    "FBL1N": {
        "name": "Vendor Line Items",
        "module": "FI-AP",
        "category": "Reconciliation",
        "description": "Display AP vendor account line items. Used for accounts payable sub-ledger reconciliation.",
        "r2r_step": "Supporting — AP Reconciliation",
    },
    "FBL5N": {
        "name": "Customer Line Items",
        "module": "FI-AR",
        "category": "Reconciliation",
        "description": "Display AR customer account line items. Used for accounts receivable sub-ledger reconciliation.",
        "r2r_step": "Supporting — AR Reconciliation",
    },
    "AFAB": {
        "name": "Post Depreciation",
        "module": "FI-AA",
        "category": "Fixed Assets",
        "description": "Run the depreciation posting program for fixed assets. Posts depreciation to GL accounts.",
        "r2r_step": "Supporting — Asset Accounting",
    },
    "F.13": {
        "name": "Automatic Clearing",
        "module": "FI-GL",
        "category": "Reconciliation",
        "description": "Automatically clear open items in GL, AP, or AR accounts based on matching criteria.",
        "r2r_step": "Supporting — Open Item Clearing",
    },
}

# ── Display Helpers ──────────────────────────────────────────────────────────

def display_tcode(code):
    code = code.upper()
    if code not in TCODES:
        print(f"\n  ❌ T-Code '{code}' not found in the R2R reference database.")
        print("     Try one of: " + ", ".join(sorted(TCODES.keys())))
        return

    info = TCODES[code]
    print(f"\n{'─' * 50}")
    print(f"  T-Code  : {code}")
    print(f"  Name    : {info['name']}")
    print(f"  Module  : {info['module']}")
    print(f"  Category: {info['category']}")
    print(f"  R2R Step: {info['r2r_step']}")
    print(f"{'─' * 50}")
    print(f"  {info['description']}")
    print(f"{'─' * 50}\n")


def list_all():
    print(f"\n{'─' * 60}")
    print(f"  {'T-CODE':<10} {'NAME':<35} {'MODULE'}")
    print(f"{'─' * 60}")
    for code, info in sorted(TCODES.items()):
        print(f"  {code:<10} {info['name']:<35} {info['module']}")
    print(f"{'─' * 60}\n")


def interactive_mode():
    print("\n" + "=" * 50)
    print("  SAP T-Code Lookup — R2R Reference Tool")
    print("=" * 50)
    print("  Commands: <tcode> to look up | list | quit\n")

    while True:
        user_input = input("  Enter T-Code: ").strip().lower()
        if user_input in ("quit", "exit", "q"):
            print("\n  Goodbye!\n")
            break
        elif user_input == "list":
            list_all()
        elif user_input:
            display_tcode(user_input)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) > 1:
        # Direct lookup from command line argument
        display_tcode(sys.argv[1])
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
