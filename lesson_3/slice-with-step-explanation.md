# String Slicing Solutions - Practice 7

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
