# Bottom-up development 

### Build the smallest working piece first, confirm it works, then build the next piece on top of it.

Here's the brick-by-brick order for this specific problem:

---

### Brick 1 — get a single greeting working

Forget the loop, forget collecting names, forget `main`. 
Just prove you can take one name and print the two lines correctly.

```python
def greet(name):
    # just make this print correctly for ONE name
    pass
```

Test it immediately by calling it directly at the bottom of the file temporarily:

```python
greet("Alice")
```

Run it. See the output. Confirm it's right. **Then delete that test call.**

---

### Brick 2 — get the collection loop working

Now write `collect_names`. Don't call `greet` yet — just prove your loop collects names and stops on `"end"`.

Temporarily print the list at the end to verify:

```python
def collect_names():
    pass

# temporary test
print(collect_names())
```

Run it. Enter a few names, type `"end"`, confirm the list looks right. **Then delete the test call.**

---

### Brick 3 — wire it together in `main`

Only now do you write `main`. At this point both functions are already proven to work — `main` is just connecting them:

```python
def main():
    # call collect_names
    # loop over the result
    # call greet for each name
    pass
```

This should be 3 lines. If it's more than that, something belongs in one of the other functions instead.

---

### The principle behind it

Each brick answers one question:

| Brick | Question being answered |
|---|---|
| `greet` | Can I format and print correctly for one name? |
| `collect_names` | Can I gather input and stop at the right time? |
| `main` | Can I connect the two together? |

Never move to the next brick until the current one answers its question with a yes.

---

Keep in mind — **don't start in `main`**. `main` is the last brick, not the first. It's the roof, not the foundation. Start with the function that has the least dependencies and the simplest job, which is always `greet` here.