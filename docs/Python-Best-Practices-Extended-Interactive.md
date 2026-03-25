# Exhaustive Procedural Checklist of Python Programming Best Practices

---

## Table of Contents

1. [General Principles and Philosophies](#1-general-principles-and-philosophies)
2. [Code Style and Formatting (PEP 8 Compliance)](#2-code-style-and-formatting-pep-8-compliance)
3. [Imports](#3-imports)
4. [Naming Conventions](#4-naming-conventions)
5. [Documentation and Comments](#5-documentation-and-comments)
6. [Type Hints and Static Analysis](#6-type-hints-and-static-analysis)
7. [Pythonic Idioms and Code Writing](#7-pythonic-idioms-and-code-writing)
8. [Error Handling and Exceptions](#8-error-handling-and-exceptions)
9. [Testing and Refactoring](#9-testing-and-refactoring)
10. [Project Structure and Dependencies](#10-project-structure-and-dependencies)
11. [Performance, Optimization, and Algorithmic Efficiency](#11-performance-optimization-and-algorithmic-efficiency)
12. [Security and Maintenance](#12-security-and-maintenance)
13. [Links to Official Resources and Documentation](#links-to-official-resources-and-documentation)

---

## 1. General Principles and Philosophies

1. **Enforce DRY (Don't Repeat Yourself):** Extract repeated logic into reusable functions, classes, modules, or utilities to avoid code duplication.

2. **Apply KISS (Keep It Simple, Stupid):** Use simple, readable solutions; avoid over-engineering or unnecessary complexity.

3. **Apply YAGNI (You Ain't Gonna Need It):** Never add unrequested features, abstractions, or functionality.

4. **Apply SOLID principles:** Ensure single responsibility per class or function; design for open extension via composition or inheritance while closed for modification; use interface segregation, dependency inversion, and Liskov substitution where appropriate.

5. **Follow the Zen of Python (`import this`):** Prioritize beautiful, explicit, simple, and readable code; errors should never pass silently unless explicitly handled; prefer flat over nested structures; sparsity over density; and one obvious way to do things.

6. **Practicality beats purity:** When theoretical elegance conflicts with real-world needs, choose pragmatic solutions.

7. **Refuse ambiguity:** Avoid guessing in unclear situations; validate inputs and document assumptions.

8. **Readability counts:** Always prioritize code that is easy to read and understand over clever or dense implementations.

9. Special cases aren't special enough to break rules, but be practical when needed.

10. **Namespaces are great:** Use modules and packages to organize code and prevent name conflicts.

[↑ Back to Top](#table-of-contents)

---

## 2. Code Style and Formatting (PEP 8 Compliance)

11. **Enforce PEP 8:** Limit lines to 79–99 characters (72 for docstrings/comments); use `snake_case` for variables/functions, `CamelCase` for classes; sort imports; use descriptive names.

12. **Indentation:** Use 4 spaces per level; never mix tabs and spaces; align continuation lines vertically or use hanging indents.

13. **Blank lines:** Surround top-level functions/classes with 2 blank lines; methods inside classes with 1; use sparingly for logical grouping.

14. **Whitespace in expressions:** Single spaces around operators (`=`, `==`, `+`, etc.); no extraneous spaces inside parentheses/brackets/braces or before commas/colons/semicolons.

15. **Binary operators:** Break lines before operators for readability; surround with equal spaces.

16. **Trailing commas:** Use in lists/dicts/arguments for easier extension; required for single-element tuples.

17. **String quotes:** Consistent use of single or double quotes; prefer double for triple-quoted strings; use opposite inside to avoid escapes.

18. **Avoid trailing whitespace:** Strip it everywhere to prevent issues.

19. **Format automatically:** Use `Black` for code formatting, `isort` (with Black profile) for import sorting.

20. **Lint and check:** Use `flake8` for style enforcement, `mypy` for type checking (strict mode), `bandit` for security scans.

21. **Require pre-commit hooks:** Enforce Black, isort, flake8, mypy, and bandit on every commit to maintain consistency.

22. **Source encoding:** Use UTF-8; ASCII-compatible identifiers; avoid non-ASCII unless necessary (e.g., for names/places).

[↑ Back to Top](#table-of-contents)

---

## 3. Imports

23. **Place imports at the top:** After docstrings, before globals/constants; group standard library, third-party, local; separate groups with blank lines.

24. **Prefer absolute imports:** For readability; use explicit relative only in complex packages.

25. **Avoid wildcard imports (`*`):** They pollute namespaces and obscure origins.

26. **Module-level dunders:** Place `__all__`, `__version__`, etc., after docstring but before other imports (except `__future__`).

[↑ Back to Top](#table-of-contents)

---

## 4. Naming Conventions

27. **Descriptive names:** Use clear, concise variable/function names reflecting usage (e.g., verbs for functions like `calculate_total`); avoid single-letter names like `l`, `O`, `I`.

28. **Variables/functions/methods:** `lowercase_with_underscores`

29. **Classes:** `CamelCase`

30. **Constants:** `UPPERCASE_WITH_UNDERSCORES`

31. **Exceptions:** `CamelCase` with `"Error"` suffix if error-related.

32. **Type variables:** `CamelCase`, short (e.g., `T`, `Num`); add `_co`/`_contra` for variance.

33. **Non-public:** Single leading underscore (`_private_var`) for internal use.

34. **Name mangling:** Double leading underscore (`__mangled`) for class attributes to avoid subclass conflicts.

35. **Avoid keyword conflicts:** Append trailing underscore (e.g., `class_`).

36. **Globals:** Same as functions; use `__all__` to control exports.

[↑ Back to Top](#table-of-contents)

---

## 5. Documentation and Comments

37. **Write docstrings:** For all public modules, functions, classes, methods; use Google-style or reStructuredText for clarity.

38. **One-line docstrings:** Imperative phrase ending in period; triple quotes, closing on same line.

39. **Multi-line docstrings:** Summary line, blank line, then details; closing quotes on own line; document args, returns, exceptions, side effects.

40. **Comments:** Complete sentences; block comments indented to code level, starting with `#`; inline comments separated by 2 spaces, used sparingly for non-obvious parts.

41. **Keep comments updated:** Contradictory comments are worse than none; use English.

42. **Directory ownership comments:** Every directory used for inter-process data exchange must contain a clear ownership comment in every reader and writer. State (1) the sole authorized writer, (2) what metadata (e.g. `mtime`) is relied upon, and (3) the invariants that depend on it. Any second writer to a declared single-writer directory requires explicit review and documentation.

    In practice, place the following comment block at the top of every function that reads from or writes to a shared directory:

    ```python
    # DIRECTORY OWNER: <sole authorized writer — script or process name>
    # SORT KEY: <field used for ordering, e.g. signal["timestamp"]> — NOT os.path.getmtime()
    # INVARIANT: <what must remain true for this code to be correct>
    # WARNING: Any process that writes to this directory after file creation
    #          invalidates the above invariant. Treat as a breaking change.
    ```

43. **Attribute docstrings:** For module/class attributes, place string literal right after assignment.

44. **Scripts:** Use module docstring as usage message covering function, syntax, and dependencies.

[↑ Back to Top](#table-of-contents)

---

## 6. Type Hints and Static Analysis

45. **Add type hints everywhere:** Use the `typing` module; avoid `Any`; enable strict `mypy` mode for full checks.

46. **Shared data contracts:** Any dict, schema, or data contract passed between modules must be defined in one shared location (`TypedDict`, `dataclass`, or constants module). Producers and consumers must import the same definition. Enforce with strict `mypy` to catch mismatches at commit time rather than runtime.

    > This rule has no enforcement without the pre-commit `mypy` hook required by Rule 21. Rule 46 and Rule 21 are co-dependent — neither is sufficient alone.

47. **Function annotations:** Follow PEP 484; space after colon, around `->` (e.g., `def func(arg: int) -> str:`).

[↑ Back to Top](#table-of-contents)

---

## 7. Pythonic Idioms and Code Writing

48. **Write Pythonic code:** Use list/dict/set comprehensions; generator expressions; context managers (`with` statements); f-strings for formatting; walrus operator (`:=`) only where it improves clarity.

49. **Use builtins efficiently:** `startswith`/`endswith` over slicing; `isinstance` over `type()`; `if seq`/`not seq` over `len(seq)`.

50. **Boolean checks:** `if greeting` (not `== True`); avoid comparing to `True`/`False`.

51. **Returns:** Consistent (all with values or all explicit `None`); add explicit `return` at end if reachable.

52. **Lambdas:** Prefer `def` for named functions (better tracebacks); use lambdas only for simple, anonymous cases.

53. **Comparisons:** Use `is`/`is not` for singletons like `None`; implement all rich methods (`__eq__`, etc.) for custom classes.

[↑ Back to Top](#table-of-contents)

---

## 8. Error Handling and Exceptions

54. **Handle errors properly:** Catch specific exceptions only; no bare `except:` (use `except Exception:`); log tracebacks.

55. **Financial/safety-critical pipelines:** Never use a dictionary `.get()` with a neutral fallback value where the neutral value is a plausible in-range result (e.g. `50.0` for RSI). Treat missing keys as data errors. Use direct access to raise `KeyError`, or explicitly log a high-visibility warning before any substitution.

    The minimum acceptable pattern when a fallback must be preserved for backward compatibility:

    ```python
    if KEY not in data_dict:
        logger.warning(
            "Missing key '%s' in indicator dict — signal degraded. "
            "Keys present: %s",
            KEY, list(data_dict.keys())
        )
    value = data_dict.get(KEY, neutral_fallback)
    ```

    > The warning must fire **before** the fallback is used, not after, so that degraded signals are visible in logs at the moment they occur.

56. **Define custom exceptions:** For domain-specific errors (e.g., `ValueNotFoundError` inheriting from `Exception`).

57. **Raise explicitly:** Use `raise X from Y` for chaining; don't silence errors without intent.

58. **Derive from `Exception`:** Not `BaseException`; add `"Error"` suffix for errors.

59. **Minimize try blocks:** Only wrap necessary code.

60. **Use `with` for resources:** Ensures cleanup via context managers.

[↑ Back to Top](#table-of-contents)

---

## 9. Testing and Refactoring

61. **Follow TDD:** Write unit tests before code; test every bug fix and refactor to preserve behavior.

62. **Integration tests:** For any pipeline where module A writes data that module B subsequently reads, create at least one integration test that runs both A and B in sequence and asserts correct end-to-end data flow. Unit tests alone are insufficient for detecting interface mismatches and implicit contracts.

63. **Write unit tests:** For functions, classes; aim for high coverage.

64. **Refactor triggers:** >2 duplicates, function >30 lines, nesting >3 levels; extract methods or simplify.

65. **Use `pytest` or `unittest`:** For test frameworks; include assertions and edge cases.

[↑ Back to Top](#table-of-contents)

---

## 10. Project Structure and Dependencies

66. **Structure project:** Use `src/package` for code; separate config, tests (unit/integration); follow modular design.

67. **Use virtual environments:** Isolate dependencies; lock in `requirements.txt` via `pip freeze`.

68. **Scan dependencies:** Use `safety` or similar for vulnerability checks.

69. **Manage config:** Via environment variables or config files; never hardcode sensitive data.

[↑ Back to Top](#table-of-contents)

---

## 11. Performance, Optimization, and Algorithmic Efficiency

70. **Optimize judiciously:** Avoid premature optimization; profile first with `cProfile` or `timeit` to confirm a bottleneck exists before refactoring.

71. **Monitor runtime:** Log start/end of long operations; track memory/CPU with `psutil` if needed.

72. **Join strings efficiently:** Use `''.join()` over `+` concatenation in loops.

73. **Choose the right collection:**
    - `list` — ordered sequences (`O(1)` append, `O(n)` search)
    - `set` / `dict` — membership tests and lookups (`O(1)` average)
    - `deque` — `O(1)` append/pop from both ends
    - `heapq` — `O(log n)` min/max access without re-sorting
    - `bisect` — `O(log n)` insertion into a sorted list

74. **Always consider time and space complexity** before choosing a data structure or algorithm: Prefer `O(1)` or `O(log n)` solutions over `O(n²)` or worse wherever practical.

75. **Never rely on filesystem timestamps** (`os.path.getmtime` or `st_mtime`) for logical ordering of records. Always embed a creation timestamp in the data itself at generation time and sort on that field. Filesystem metadata is unreliable due to copies, overwrites, and OS behavior.

76. **Prefer sets and dicts over lists for membership tests:** `if x in my_set` is `O(1)`; `if x in my_list` is `O(n)` — never use list scans inside loops.

77. **Avoid nested loops over large collections:** If you find yourself writing `for x in A: for y in B`, ask whether a dict/set pre-index can collapse it from `O(n²)` to `O(n)`.

78. **Sort once, query many:** If a sorted list will be searched repeatedly, sort it once `O(n log n)` then use `bisect` for `O(log n)` lookups rather than repeated `O(n)` scans.

79. **Use generators and lazy evaluation for large datasets:** `yield` and `itertools` keep memory at `O(1)` per item rather than loading `O(n)` items into memory at once.

80. **Pre-compute and cache repeated calculations:** Use `functools.lru_cache` or explicit dicts for memoization; never recompute inside a loop what can be computed once before it.

81. **Annotate non-obvious complexity in comments:** e.g., `O(n log n)` sort + `O(n)` scan = `O(n log n)` overall, so reviewers understand intent without re-deriving it.

82. **Treat unbounded data structures with extra caution:** Financial and time-series data (transactions, equity history, rebalance logs) grow indefinitely; never scan full history inside another loop — pre-index by timestamp or ID upfront before any iteration.

[↑ Back to Top](#table-of-contents)

---

## 12. Security and Maintenance

83. **Secure code:** Avoid `eval`/`exec` unless necessary; validate inputs; use the `secrets` module for cryptography.

84. **Design for inheritance:** Make attributes non-public by default; use properties for data access.

85. **Public vs. internal:** Use `__all__` for public APIs; underscore prefix for internal.

[↑ Back to Top](#table-of-contents)

---

> This checklist covers a procedural flow: Start with principles, enforce style, document, handle errors, test, structure, and optimize. Apply iteratively during development.

---

## Links to Official Resources and Documentation

| Resource | URL |
|---|---|
| PEP 8 – Style Guide for Python Code | https://peps.python.org/pep-0008/ |
| PEP 20 – The Zen of Python | https://peps.python.org/pep-0020/ |
| PEP 257 – Docstring Conventions | https://peps.python.org/pep-0257/ |
| The Hitchhiker's Guide to Python | https://docs.python-guide.org/ |
| Python Official Documentation | https://www.python.org/doc/ |
| Google Python Style Guide | https://google.github.io/styleguide/pyguide.html |

[↑ Back to Top](#table-of-contents)
