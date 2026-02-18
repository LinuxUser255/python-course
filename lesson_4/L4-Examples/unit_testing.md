Below is a **clean, step-by-step walkthrough** for unit testing your `drink_age` function using **pytest**, following standard Python testing best practices.

I will keep this simple, explicit, and correct.

---

## 1. Identify the Challenges in This Function

Your function:

```python
def drink_age():
    age = int(input("Enter your age: "))

    if age >= 21:
        print("You can drink.")
    else:
        print("You can't drink.")
```

### What Makes This Tricky to Test

* It calls `input()` (interactive user input)
* It uses `print()` instead of returning a value

### Testing Strategy

We will:

1. **Mock `input()`** to simulate user input
2. **Capture stdout** to verify what was printed

---

## 2. Recommended Project Structure

```
project/
├── age.py
└── tests/
    └── test_age.py
```

Assume your code lives in `age.py`.

---

## 3. Core Pytest Tools We’ll Use

* `monkeypatch` → override `input()`
* `capsys` → capture printed output

These are **built-in pytest fixtures**, no extra libraries required.

---

## 4. First Test: Age ≥ 21

### Test Goal

Verify that entering an age of 21 or more prints:

```
You can drink.
```

### `tests/test_age.py`

```python
def test_drink_age_can_drink(monkeypatch, capsys):
    # Arrange: mock input()
    monkeypatch.setattr("builtins.input", lambda _: "21")

    # Act
    from age import drink_age
    drink_age()

    # Assert: capture printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "You can drink."
```

---

## 5. Second Test: Age < 21

```python
def test_drink_age_cannot_drink(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "20")

    from age import drink_age
    drink_age()

    captured = capsys.readouterr()
    assert captured.out.strip() == "You can't drink."
```

---

## 6. Optional: Test Invalid Input (Edge Case)

Your function will raise a `ValueError` if input is not numeric. This is acceptable behavior, but it should be **explicitly tested**.

```python
import pytest

def test_drink_age_invalid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")

    from age import drink_age

    with pytest.raises(ValueError):
        drink_age()
```

---

## 7. Run the Tests

From the project root:

```bash
pytest -v
```

---

## 8. Best-Practice Refactor (Optional but Recommended)

### Why Refactor?

Functions that:

* return values
* avoid direct I/O

are **much easier to test**.

### Refactored Version

```python
def can_drink(age: int) -> bool:
    return age >= 21
```

```python
def drink_age():
    age = int(input("Enter your age: "))
    if can_drink(age):
        print("You can drink.")
    else:
        print("You can't drink.")
```

### Unit Test Becomes Trivial

```python
def test_can_drink():
    assert can_drink(21) is True
    assert can_drink(20) is False
```

This separation of **business logic vs. I/O** is a core Python testing best practice.

---

## 9. Summary of What You Learned

* How to test functions that use `input()`
* How to assert printed output using `capsys`
* How to handle error cases explicitly
* Why separating logic from I/O improves testability

If you want, next we can:

* Parameterize these tests
* Convert this into a CLI-style test
* Add coverage measurement
* Apply the same approach to API-style input validation

Just say what direction you want to go.
