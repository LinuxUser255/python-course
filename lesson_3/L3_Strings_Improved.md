# Lesson 3: Strings in Python
> **Careerist Python Course** | L3

---

## What You'll Learn
- What a string data type is
- How to concatenate, convert, and format strings
- How to use string methods
- How to use slicing and indexing

---

## Why Strings Matter for QA Engineers

Before we write a single line of code, here's why this lesson is important for your career:

As a QA engineer, strings are everywhere:
- **Parsing error messages** — "ERROR: timeout after 30s on endpoint /login" — you'll slice and search these constantly
- **Validating user input** — does the username contain illegal characters? Is it the right length?
- **Building test reports** — formatting test results into readable output
- **Log analysis** — finding patterns in thousands of lines of log text

Every technique in this lesson has a direct job application. 

---

## 1. What Is a String?

A **string** is a data type used to represent text. It's a sequence of characters enclosed in single (`''`) or double (`""`) quotes. Strings can contain letters, numbers, symbols, and spaces.

```python
string_1 = 'This value is a string'
string_2 = "And this value is a string too"
```

### Quotes and Escape Characters

When your string itself needs to contain quotes or apostrophes, you have options:

```python
# Option 1: use double quotes on the outside, single inside
string1 = "You're awesome"

# Option 2: escape the apostrophe with a backslash
string2 = 'You\'re awesome'

# Option 3: triple quotes for multi-line strings
string3 = '''
You are
So
Awesome
'''
```

### Comments

Comments start with `#` and are ignored when your code runs. Use them to explain your thinking.

```python
# This is a comment — Python will skip this line entirely
name = "Alice"  # This is an inline comment
```

---

## 2. Concatenation

**Concatenation** means joining strings together using `+`. It's how you build dynamic messages from separate pieces.

```python
str_1 = 'Hello'
str_2 = 'World!'
result = str_1 + ' ' + str_2
print(result)
# Output: Hello World!
```

###  The Type Problem

Python **cannot** concatenate a string with an integer directly — it will raise a `TypeError`. Convert numbers to strings first using `str()`.

```python
# This will CRASH:
age = 25
print("Your age is " + age)
# TypeError: can only concatenate str (not "int") to str

# This works:
print("Your age is " + str(age))
# Output: Your age is 25
```

> **QA tip:** Converting integers to strings is also useful when you want to work with individual digits of a number — e.g., checking that a ZIP code is exactly 5 digits long.

---

## 3. Formatting Strings

Python gives you three ways to embed variables in strings. You'll encounter all three in real codebases, so it's worth knowing each.

### Method 1: Concatenation with `+`
```python
name = 'Emily'
age = 26
job_title = 'QA Manager'

print(name + ' is a ' + str(age) + ' years old ' + job_title + ' of our company.')
```

### Method 2: `.format()`
```python
print('{name} is a {age} years old {job_title} of our company.'.format(
    name=name, age=age, job_title=job_title
))
```

You can also reuse or reorder values with positional indices:
```python
print('{0} and {1} and {0}'.format('Alice', 'Bob'))
# Output: Alice and Bob and Alice
```

### Method 3: f-strings  (recommended)
```python
print(f'{name} is a {age} years old {job_title} of our company.')
```

F-strings are the most readable and modern approach. They allow expressions directly inside the braces:

```python
price = 9.99
quantity = 3
print(f'Total: ${price * quantity:.2f}')
# Output: Total: $29.97
```

### All three side by side:
```python
name, age, job_title = 'Emily', 26, 'QA Manager'

# Concatenation
print(name + ' is a ' + str(age) + ' years old ' + job_title + ' of our company.')

# .format()
print('{name} is a {age} years old {job_title} of our company.'.format(
    name=name, age=age, job_title=job_title))

# f-string
print(f'{name} is a {age} years old {job_title} of our company.')
```

---

## 4. Data Input

The `input()` function pauses your program and waits for the user to type something. It **always returns a string**, even if the user types a number.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")

# input() always returns a string — convert if you need a number:
age = int(input("Enter your age: "))
print(f"In 10 years you will be {age + 10}.")
```

---

## 5. String Methods

Methods are built-in tools that operate on a string. You call them with dot notation: `string.method()`.

| Method | What it does | Example | Output |
|---|---|---|---|
| `.upper()` | All uppercase | `"hello".upper()` | `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` | `"hello"` |
| `.title()` | Title Case | `"hello world".title()` | `"Hello World"` |
| `.replace(old, new)` | Swap substrings | `"cat".replace("c","b")` | `"bat"` |
| `.count(x)` | Count occurrences | `"hello".count("l")` | `2` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` | `"hi"` |
| `len(string)` | Length of string | `len("hello")` | `5` |

### Method Chaining

You can chain methods together — each one runs on the result of the previous:

```python
messy_input = "  eRROR: conNEcTion tIMEouT  "

cleaned = messy_input.strip().lower().replace("error: ", "")
print(cleaned)
# Output: connection timeout
```

> **QA scenario:** Log lines are often inconsistently formatted. Method chaining lets you normalize them before searching for patterns.

###  Challenge: Fix the Broken Log Line

Given this messy error string, use method chaining to produce clean output:

```python
raw_log = "  WARNING : disk USAge at 91%  "

# Your goal — produce this output:
# "disk usage at 91%"

# Hint: you'll need .strip(), .lower(), and .replace()
```

**Solution:**
```python
raw_log = "  WARNING : disk USAge at 91%  "
cleaned = raw_log.strip().lower().replace("warning : ", "")
print(cleaned)
# Output: disk usage at 91%
```

---

## 6. Indexing

Each character in a string has a **position number** called an index. Python counts from `0`, and also supports negative indices that count from the end.

```
String:    H  e  l  l  o
Positive:  0  1  2  3  4
Negative: -5 -4 -3 -2 -1
```

```python
string = "Hello"

print(string[0])   # H
print(string[1])   # e
print(string[-1])  # o  (last character)
print(string[-2])  # l  (second to last)
```

###  Predict the Output

Before running this code, predict what each line prints:

```python
word = "Python"

print(word[0])    # ?
print(word[-1])   # ?
print(word[3])    # ?
print(word[-3])   # ?
```

<details>
<summary>Reveal answers</summary>

```
P
n
h
h
```

`word[3]` and `word[-3]` both land on `'h'` — the middle of "Python"!

</details>

---

## 7. Slicing

**Slicing** extracts a substring using `[start:end]`. The end index is **not included** in the result.

```
String:  P  y  t  h  o  n  _  s  t  u  d  e  n  t
Index:   0  1  2  3  4  5  6  7  8  9  10 11 12 13
```

```python
string = "Python_student"

print(string[2:5])   # tho   (indices 2, 3, 4)
print(string[:6])    # Python (from start to index 5)
print(string[7:])    # student (from index 7 to end)
print(string[:])     # Python_student (entire string)
```

### Slicing with a Step

Add a third value to skip characters: `[start:end:step]`

```python
text = "Python"

print(text[0:6:2])  # Pto  (every 2nd character)
print(text[::2])    # Pto  (same, shorthand)
print(text[::-1])   # nohtyP  (reversed!)
```

> The `[::-1]` trick is a Python classic — it reverses any string with no loops needed.

###  Predict the Output

```python
s = "Python programming is fun!"

print(s[7:18])     # ?
print(s[7:])       # ?
print(s[0::3])     # ?
print(s[::-1])     # ?
```

<details>
<summary>Reveal answers</summary>

```
programming
programming is fun!
Ph oai n
!nuf si gnimmargorp nohtyP
```

</details>

---

## 8. Spotting and Fixing Bugs 

One of the most important QA skills is reading code carefully. Here's a buggy solution — can you spot the error?

```python
sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

# Intended: replace new_word with "REPLACED"
print(sentence.replace(new_word, sentence))   # 🐛 Bug here!
print(sentence.count(letter))
```

**What's wrong?**

`sentence.replace(new_word, sentence)` replaces the target word with the *entire sentence* — not with `"REPLACED"`. The second argument should be the string `"REPLACED"`.

**Fixed version:**
```python
sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

print(sentence.replace(new_word, "REPLACED"))
print(sentence.count(letter))
```

**Test it:**
```
Enter a sentence: I love cats and dogs, but cats are my favorite.
Enter the word to replace: cats
Enter the letter to count: o

Output:
I love REPLACED and dogs, but REPLACED are my favorite.
3
```

> **QA mindset:** Always test with a concrete example. If the output doesn't match expectations, read the arguments carefully — a small typo can completely change behavior.

---

## 9. Practices

### Practice 1 — String Formatting (3 ways)

Given these variables, print the message three ways:

```python
name = 'Emily'
age = 26
job_title = 'QA Manager'

# Target output: "Emily is a 26 years old QA Manager of our company."
```

Try: concatenation, `.format()`, and f-strings.

<details>
<summary>Solution</summary>

```python
# Concatenation
print(name + ' is a ' + str(age) + ' years old ' + job_title + ' of our company.')

# .format()
print('{name} is a {age} years old {job_title} of our company.'.format(
    name=name, age=age, job_title=job_title))

# f-string
print(f'{name} is a {age} years old {job_title} of our company.')
```

</details>

---

### Practice 2 — User Input

Write a program that:
1. Asks the user: `"What is your name: "`
2. Prints: `"Your name is [name]."`

**Example:**
```
What is your name: John
Your name is John.
```

<details>
<summary>Solution</summary>

```python
name = input("What is your name: ")
print(f"Your name is {name}.")
```

</details>

---

### Practice 3 — Text Formatting Tool

Build a mini formatter. Ask for text, then print it in 4 formats:

```
Enter the text to be formatted: hello wORLD

Uppercase: HELLO WORLD
Lowercase: hello world
Title: Hello World
Length: 11
```

<details>
<summary>Solution</summary>

```python
text = input('Enter the text to be formatted: ')

print("Uppercase: " + text.upper())
print("Lowercase: " + text.lower())
print("Title: " + text.title())
print("Length: " + str(len(text)))
```

</details>

---

### Practice 4 — Find, Replace, and Count

Write a program that takes three inputs and produces two outputs:

```
Enter a sentence: I love cats and dogs, but cats are my favorite.
Enter the word to replace: cats
Enter the letter to count: o

I love REPLACED and dogs, but REPLACED are my favorite.
3
```

<details>
<summary>Solution</summary>

```python
sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

print(sentence.replace(new_word, "REPLACED"))
print(sentence.count(letter))
```

</details>

---

### Practice 5 — Slicing

Given `"Python programming is fun!"`, extract:

1. `"programming"`
2. `"programming is fun!"`
3. `"Ph oai n"` (every 3rd character)
4. `"!nuf si gnimmargorp nohtyP"` (reversed)

<details>
<summary>Solution</summary>

```python
string = "Python programming is fun!"

print(string[7:18])   # programming
print(string[7:])     # programming is fun!
print(string[0::3])   # Ph oai n
print(string[::-1])   # !nuf si gnimmargorp nohtyP
```

</details>

---

## 10. Summary: Strings in QA Engineering

Here's a cheat sheet of what you'll actually reach for on the job:

| Situation | Tool | Example |
|---|---|---|
| Building a test result message | f-string | `f"Test {test_id}: {status}"` |
| Normalizing user input before comparison | `.strip().lower()` | `input.strip().lower() == "yes"` |
| Checking password length | `len()` | `len(password) >= 8` |
| Extracting an error code from a log | Slicing | `log_line[7:12]` |
| Counting how many times an error appears | `.count()` | `log.count("ERROR")` |
| Masking sensitive data in output | `.replace()` | `log.replace(api_key, "***")` |
| Reversing a string to check palindromes | `[::-1]` | `word == word[::-1]` |

---

## Homework

1. Clone and pull the repository before starting
2. Complete Lesson 3 homework in PyCharm
3. Upload solutions to Git Gist
4. Submit for review through your Learning Space
5. Use the Reference Sheet for extra methods

---

*Questions? Reach out through your Careerist Learning Space.*
*support@careerist.com | www.careerist.com | 1 415 862-2563*
