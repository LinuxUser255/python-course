# String Slicing - Practice 7


## Given String
```python
string = "Python programming is fun!"
```

## Visual Index Reference

### Positive Indices
```
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
 P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !
```

### Negative Indices
```
-26-25-24-23-22-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
 P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !
```

---

## Solution 1: Extract "programming"

### Code
```python
substring1 = string[7:18]
print(substring1)  # Output: programming
```

### Explanation
- **Slice notation**: `string[7:18]`
- **Start index**: `7` (the letter 'p')
- **Stop index**: `18` (stops before index 18, which is the space after 'g')
- **Result**: Characters from index 7 through 17 (inclusive)

### Breakdown
```
Index:  7  8  9 10 11 12 13 14 15 16 17
Char:   p  r  o  g  r  a  m  m  i  n  g
```

The slice `[7:18]` extracts exactly 11 characters that spell "programming".

---

## Solution 2: Extract "programming is fun!"

### Code
```python
substring2 = string[7:]
print(substring2)  # Output: programming is fun!
```

### Explanation
- **Slice notation**: `string[7:]`
- **Start index**: `7` (the letter 'p')
- **Stop index**: *omitted* (goes to the end of the string)
- **Result**: Everything from index 7 to the end

### Breakdown
```
Index:  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
Char:   p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !
```

When you omit the stop index in a slice, Python automatically includes all characters from the start index to the end of the string.

---

## Solution 3: Extract "Ph oai  n" (Every 3rd Character)

### Code
```python
substring3 = string[0::3]
print(substring3)  # Output: Ph oai  n
```

### Explanation
- **Slice notation**: `string[0::3]`
- **Start index**: `0` (beginning of string)
- **Stop index**: *omitted* (goes to the end)
- **Step**: `3` (take every 3rd character)

### Breakdown
This slice starts at index 0 and takes every 3rd character:

```
Index 0:  'P'
Index 3:  'h'
Index 6:  ' ' (space)
Index 9:  'o'
Index 12: 'a'
Index 15: 'i'
Index 18: ' ' (space)
Index 21: ' ' (space)
Index 24: 'n'
```

**Visual representation**:
```
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
 P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !
 ^        ^        ^        ^        ^        ^        ^        ^        ^
```

The step of 3 means we jump 3 positions each time, creating the pattern "Ph oai  n".

---

## Key Concepts

### Slice Syntax
```python
string[start:stop:step]
```

- **start**: Index where slice begins (inclusive)
- **stop**: Index where slice ends (exclusive)
- **step**: Interval between indices

### Omitting Parameters
- **Omit start**: Defaults to beginning (index 0)
- **Omit stop**: Defaults to end of string
- **Omit step**: Defaults to 1 (every character)

### Examples
```python
string[7:18]   # From index 7 to 17
string[7:]     # From index 7 to end
string[0::3]   # Every 3rd character from start to end
string[::2]    # Every 2nd character (entire string)
string[::-1]   # Reverse the string (step of -1)
```

---

## Complete Code Output

Running `slice-with-step.py` produces:
```
programming
programming is fun!
Ph oai  n
```

Each line demonstrates a different slicing technique, showing the power and flexibility of Python's slice notation.



# Practice 8

Given the string
"Python is amazing!"
Please provide the reversed string:

```text
"!gnizama si nohtyP"
```

```python

string = "Python is amazing!"

# !gnizama si nohtyP
reversed_string = [::-1]

print(reversed_string)


<br>

# Other Slicing challange explained

```python

letters = "abcdefghijklmnopqrstuvwxyz"

# Create a slice that produces the chars: qpo
print(letters[16:13:-1]) # qpo


# Create a slice that produces the chars: edcba
print(letters[4::-1]) # edcba


# Slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1]) # zyxwvuts

```


A **detailed, beginner-friendly breakdown** of how each of these Python slicing examples works using the string:

```python
letters = "abcdefghijklmnopqrstuvwxyz"
```

We’ll visualize the string with **indices** (both positive and negative) to make everything crystal clear:

```
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```

Python slicing syntax:
```python
string[start:stop:step]
```
- `start` → inclusive
- `stop` → **exclusive**
- `step` → direction and size of jump (negative = backwards)

---

### 1. `letters[16:13:-1]` → **qpo**

```python
print(letters[16:13:-1])  # qpo
```

**Step-by-step:**

- **Start**: `16` → letter **q** (included)
- **Stop**: `13` → letter **n** (excluded because stop is exclusive)
- **Step**: `-1` → move **backwards** one character at a time

Walking backwards:
```
16 → q
15 → p
14 → o
13 → n  (stop before including n)
```

**Result**: `qpo`

**Why it works**: When step is negative, Python treats `start` as the first character and walks **towards** `stop` (but never includes `stop`).

---

### 2. `letters[4::-1]` → **edcba**

```python
print(letters[4::-1])  # edcba
```

**Step-by-step:**

- **Start**: `4` → letter **e** (included)
- **Stop**: (omitted) → defaults to **very beginning** when stepping backwards
- **Step**: `-1` → backwards

So it goes:
```
4 → e
3 → d
2 → c
1 → b
0 → a
(stop — reached the beginning)
```

**Result**: `edcba`

**Key rule**:
When `stop` is omitted **and** step is negative → go all the way to index `0`.

---

### 3. `letters[:-9:-1]` → **zyxwvuts**

```python
print(letters[:-9:-1])  # zyxwvuts
```

**Step-by-step:**

- **Start**: (omitted) → defaults to **very end** when stepping backwards → index `25` → **z**
- **Stop**: `-9` → that's index `len(letters) - 9 = 26 - 9 = 17` → letter **r** (excluded)
- **Step**: `-1` → backwards

So:
```
25 → z
24 → y
23 → x
22 → w
21 → v
20 → u
19 → t
18 → s
17 → r  (stop before including r)
```

**Result**: `zyxwvuts` (exactly 8 characters)

**Why 8?**
From index 25 down to 18 inclusive:
`25,24,23,22,21,20,19,18` → 8 steps

**Key rule**:
When `start` is omitted **and** step is negative → start from the **last character**.

---

### Summary Table

| Slice              | Start Index | Stop Index | Step | Direction | Result       | Length |
|--------------------|-------------|------------|------|-----------|--------------|--------|
| `[16:13:-1]`       | 16 (q)      | 13 (n)     | -1   | ←         | `qpo`        | 3      |
| `[4::-1]`          | 4 (e)       | 0          | -1   | ←         | `edcba`      | 5      |
| `[:-9:-1]`         | 25 (z)      | 17 (r)     | -1   | ←         | `zyxwvuts`   | 8      |

---

### Pro Tips

- Always remember: **stop is exclusive**
- Negative step + omitted start → start from end
- Negative step + omitted stop → go to beginning
- Use negative indices for "counting from the end" (`-1` = last char)

Try these bonus ones:
```python
letters[::-1]       # whole string reversed: zyx...a
letters[-1:-10:-1]  # same as[:-9:-1] but more explicit
letters[::2]        # every second char: aceg...


