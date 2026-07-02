#!/usr/bin/env python3
"""
Imports module_utils and uses its functions.
Notice: the if __name__ == "__main__" block in module_utils does NOT run.
"""

import module_utils   # triggers module_utils' top-level code, but NOT its __main__ block

print(f'runner.py __name__: {__name__}')  # This file IS __main__

# Use the imported functions directly
print(module_utils.validate_username("testuser"))  # True
print(module_utils.validate_email("user@qa.com"))  # True
