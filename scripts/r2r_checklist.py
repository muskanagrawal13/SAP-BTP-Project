"""
r2r_checklist.py
================
A simple command-line utility to walk through the Record-to-Report (R2R)
month-end / year-end closing checklist for SAP FI.

Usage:
    python r2r_checklist.py

The user is guided through each closing step and can mark items complete,
flag issues, or skip. A summary report is printed at the end.
"""

import datetime

# ── Checklist Definition ────────────────────────────────────────────────────

CHECKLIST = [
    {
        "step": 1,
        "title": "Post All Journal Entries",
        "tcode": "FB50",
        "description": "Ensure all period transactions are posted to the GL.",
        "checks": [
            "All recurring entries posted",
            "Manual adjustments posted",
            "Intercompany entries posted",
        ],
    },
    {
        "step": 2,
        "title": "Review General Ledger Balances",
        "tcode": "FS10N",
        "description": "Verify GL account balances are complete and accurate.",
        "checks": [
            "Balance sheet accounts reviewed",
            "P&L accounts reviewed",
            "Unusual variances investigated",
        ],
    },
    {
        "step": 3,
        "title": "Perform Account Reconciliation",
        "tcode": "FBL3N",
        "description": "Reconcile GL to AR, AP, and Fixed Asset sub-ledgers.",
        "checks": [
            "AR sub-ledger reconciled to GL",
            "AP sub-ledger reconciled to GL",
            "Fixed assets reconciled to GL",
            "Open items reviewed and cleared",
        ],
    },
    {
        "step": 4,
        "title": "Post Accruals and Adjustments",
        "tcode": "FBS1",
        "description": "Post period-end accruals, deferrals, and corrections.",
        "checks": [
            "Accrued expenses posted",
            "Prepaid adjustments posted",
            "Revenue deferrals posted",
            "Reversal dates set correctly",
        ],
    },
    {
        "step": 5,
        "title": "Generate Financial Statements",
        "tcode": "F.01",
        "description": "Run Balance Sheet and P&L reports for review.",
        "checks": [
            "Balance Sheet generated and reviewed",
            "P&L Statement generated and reviewed",
            "Compared to prior period",
            "Approved by Finance Controller",
        ],
    },
    {
        "step": 6,
        "title": "Close the Posting Period",
        "tcode": "OB52",
        "description": "Lock the period to prevent further postings.",
        "checks": [
            "All entries verified and approved",
            "Posting period closed for all account types",
            "Next period opened if required",
            "Closing confirmation sent to stakeholders",
        ],
    },
]

# ── Helpers ─────────────────────────────────────────────────────────────────

def print_banner():
    print("\n" + "=" * 60)
    print("   SAP R2R — Month/Year-End Closing Checklist")
    print(f"   Date: {datetime.date.today().strftime('%d %B %Y')}")
    print("=" * 60 + "\n")


def prompt_check(check_text):
    """Ask user to confirm a single check item. Returns status string."""
    while True:
        response = input(f"  [ ] {check_text}\n      (c=complete, s=skip, i=issue): ").strip().lower()
        if response in ("c", "complete"):
            return "✅ Complete"
        elif response in ("s", "skip"):
            return "⏭  Skipped"
        elif response in ("i", "issue"):
            note = input("      Describe the issue: ").strip()
            return f"⚠️  Issue — {note}"
        else:
            print("      Please enter c, s, or i.")


def run_step(step_data):
    """Run a single checklist step interactively."""
    print(f"\n{'─' * 60}")
    print(f"  STEP {step_data['step']}: {step_data['title']}")
    print(f"  T-Code : {step_data['tcode']}")
    print(f"  Info   : {step_data['description']}")
    print(f"{'─' * 60}")

    results = {}
    for check in step_data["checks"]:
        results[check] = prompt_check(check)

    return results


def print_summary(all_results):
    """Print a summary report of all steps and their status."""
    print("\n\n" + "=" * 60)
    print("   CLOSING CHECKLIST SUMMARY")
    print(f"   Generated: {datetime.datetime.now().strftime('%d %B %Y %H:%M')}")
    print("=" * 60)

    issues_found = False
    for step_data in CHECKLIST:
        step_results = all_results.get(step_data["step"], {})
        print(f"\nStep {step_data['step']}: {step_data['title']} ({step_data['tcode']})")
        for check, status in step_results.items():
            print(f"  {status} — {check}")
            if "Issue" in status:
                issues_found = True

    print("\n" + "=" * 60)
    if issues_found:
        print("  ⚠️  STATUS: Closing complete with issues — review required.")
    else:
        print("  ✅  STATUS: All steps complete. Period close successful.")
    print("=" * 60 + "\n")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print_banner()
    print("This utility guides you through each R2R closing step.")
    print("For each check: enter  c = complete | s = skip | i = issue\n")

    all_results = {}

    for step_data in CHECKLIST:
        step_results = run_step(step_data)
        all_results[step_data["step"]] = step_results

        cont = input("\n  Proceed to next step? (y/n): ").strip().lower()
        if cont != "y":
            print("\nChecklist paused. Re-run the script to start again.")
            break

    print_summary(all_results)


if __name__ == "__main__":
    main()
