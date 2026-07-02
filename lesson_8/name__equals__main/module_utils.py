#!/usr/bin/env python3
"""
Demonstrates if __name__ == "__main__"

Python automatically sets __name__ to:
  "__main__"       → when this file is run directly
  "module_utils"   → when this file is imported by another file

Run this file two ways and watch __name__ change:
  1. python module_utils.py          → __name__ is "__main__"
  2. python runner.py                → __name__ is "module_utils"
"""

# ─── This line runs ALWAYS — imported or run directly ───────────────────────
print(f'module_utils __name__: {__name__}')


# ─── Functions another file might want to import ────────────────────────────
def validate_username(username):
    """Returns True if username is at least 3 characters, False otherwise."""
    return len(username) >= 3


def validate_email(email):
    """Returns True if the email contains '@' and '.', False otherwise."""
    return "@" in email and "." in email


# ─── This block ONLY runs when the file is executed directly ─────────────────
# ─── It is SKIPPED when this file is imported ───────────────────────────────
if __name__ == "__main__":
    print("\nRunning directly — executing quick self-tests:\n")

    print(validate_username("jo"))          # False — too short
    print(validate_username("ada"))         # True
    print(validate_email("bad-email"))      # False
    print(validate_email("ada@test.com"))   # True

