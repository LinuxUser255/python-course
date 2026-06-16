### Demo:

- [ ] **Operator Precedence** (Slides 12–14)
- [ ] **Handling Error Messages** (Slides 16–17)
- [ ] **Variables — Assigning & Reassigning** (Slides 19–21)
- [ ] **Python Keywords** (Slide 26)
- [ ] **Constants** (Slide 27)
- [ ] **Data Types Overview** (Slides 31–33)


**1. Error Messages (Slides 16–17) — highest priority**


```bash
1 / 0

* 5

5 *
```

**2. `type()` with the status code gotcha (Slide 33)**
```python
status_code = '200'
type(status_code)      # <class 'str'>
status_code = 200
type(status_code)      # <class 'int'>
```

**3. Variable reassignment (Slide 20)**
```python
pi = 3.14159265359
pi = 3.14
```

**4. `print()` vs bare variable name (Slide 21)**


**5. Operator Precedence surprise (Slide 12)**


**6. Constants "aren't really constant" (Slide 27)**


```python
GRAVITY = 9.81
GRAVITY = 0        # Python lets you do this
print(GRAVITY)     # 0 — oops
```
