## Nested vs Non-Nested Dictionaries

### Non-Nested (Flat) Dictionary

```python
person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'state': 'NY',
    'married': False
}
```

**Access:** `person['city']`

### Nested Dictionary

```python
person = {
    'name': 'John Doe',
    'age': 30,
    'location': {
        'city': 'New York',
        'state': 'NY'
    },
    'married': False
}
```

**Access:** `person['location']['city']`

---

## Key Differences

| Aspect | Flat | Nested |
|--------|------|--------|
| Structure | All keys at one level | Keys contain other dictionaries |
| Access | Single bracket `['key']` | Chained brackets `['key']['subkey']` |
| Complexity | Simpler | More complex |

---

## When to Use Each

**Flat:** When data is simple and unrelated. A person's name and age don't need grouping.

**Nested:** When data has logical relationships. `city` and `state` both describe location—grouping them makes that relationship explicit.

---

## Real-World Significance

Nested dictionaries mirror how real data is structured. API responses (JSON) almost always come nested:

```python
api_response = {
    'user': {
        'profile': {
            'name': 'Jane',
            'avatar_url': '...'
        },
        'settings': {
            'theme': 'dark',
            'notifications': True
        }
    }
}
```

Learning and using nested dictionaries prepares for you for working with APIs, 
config files, and databases—where flat structures are rare.