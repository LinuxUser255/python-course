# When to Use Functional Programming - Quick Decision Guide

## 🎯 Use Functional Programming When...

### 1. **Processing Collections of Data**
```python
# GOOD USE: Transforming lists
users = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 35}]

# Functional approach is cleaner
adults = list(filter(lambda u: u["age"] >= 18, users))
names = list(map(lambda u: u["name"], adults))
```

**Examples:**
- 📊 Processing CSV files
- 🔍 Filtering database results
- 🧹 Cleaning API responses
- 📈 Calculating statistics

---

### 2. **Writing Testable Code**
```python
# GOOD USE: Pure functions are easy to test

# Easy to test - no side effects
def calculate_discount(price, percent):
    return price * (1 - percent / 100)

# Hard to test - has side effects
total = 0
def add_to_cart(price):
    global total
    total += price
    print(f"Added ${price}")
```

**Examples:**
- 🧪 Unit testing business logic
- 🔬 Scientific computations
- 💰 Financial calculations
- 🎯 Rules engines

---

### 3. **Parallel/Concurrent Processing**
```python
# GOOD USE: Processing large datasets with multiple cores

from multiprocessing import Pool

# Safe to parallelize (pure function)
def process_item(item):
    return item * item

# Can use all CPU cores
with Pool() as pool:
    results = pool.map(process_item, large_list)
```

**Examples:**
- 📊 Big data processing
- 🖼️ Image processing (filters on each pixel)
- 📝 Text analysis on documents
- 🧮 Batch calculations

---

### 4. **Data Transformation Pipelines**
```python
# GOOD USE: Chaining transformations

# Clean, declarative pipeline
result = (
    data
    | (lambda d: filter(is_valid, d))
    | (lambda d: map(transform, d))
    | (lambda d: sorted(d, key=sort_key))
)
```

**Examples:**
- 🔄 ETL jobs (Extract, Transform, Load)
- 🌐 Web scraping
- 📡 API data processing
- 🎨 Data visualization prep

---

### 5. **Configuration & Settings**
```python
# GOOD USE: Computing configuration values

def get_timeout(environment):
    timeouts = {
        "prod": 30,
        "staging": 60,
        "dev": 120
    }
    return timeouts.get(environment, 30)

# Pure function - easy to test all environments
```

**Examples:**
- ⚙️ Environment settings
- 🎚️ Feature flags
- 🔧 Dynamic configuration
- 📐 Computed properties

---

### 6. **Event/Stream Processing**
```python
# GOOD USE: Analyzing logs or events

error_logs = list(filter(lambda log: log["level"] == "ERROR", logs))
error_users = set(map(lambda log: log["user"], error_logs))
```

**Examples:**
- 📋 Log analysis
- 📊 Analytics dashboards
- 🔔 Event monitoring
- 🎮 Game replay systems

---

## ❌ Use Procedural Programming When...

### 1. **Simple Sequential Scripts**
```python
# BETTER AS PROCEDURAL: Simple automation

# Just do these steps in order
def backup_database():
    print("Starting backup...")
    connect_to_db()
    dump_data()
    compress_file()
    upload_to_s3()
    print("Backup complete!")
```

**Examples:**
- 🤖 Automation scripts
- 📝 Simple CLI tools
- 🔧 System administration
- 📦 Build scripts

---

### 2. **Heavy I/O Operations**
```python
# BETTER AS PROCEDURAL: File/network operations

def read_and_process_file(filename):
    with open(filename, 'r') as f:  # I/O operation
        data = f.read()
        process(data)
        write_results()  # Another I/O operation
```

**Examples:**
- 📁 File operations
- 🌐 Network requests
- 💾 Database queries
- 🖨️ Hardware interaction

---

### 3. **Stateful Systems**
```python
# BETTER AS PROCEDURAL: Managing complex state

class GameState:
    def __init__(self):
        self.player_health = 100
        self.enemies = []
        self.score = 0

    def update(self):
        # Lots of state changes
        self.move_player()
        self.update_enemies()
        self.check_collisions()
```

**Examples:**
- 🎮 Games
- 🖥️ GUI applications
- 🤖 Stateful protocols
- 🔄 Animation systems

---

### 4. **Learning/Teaching Basics**
```python
# BETTER AS PROCEDURAL: Beginner-friendly

def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}!")

greet_user()
```

**Examples:**
- 📚 Teaching programming
- 👶 Beginner exercises
- 📖 Code examples
- 🎓 Tutorials

---

## 🔍 Decision Flowchart

```
Start Here
    ↓
Are you processing a collection/list?
    YES → Use Functional ✅
    NO → Continue
         ↓
    Do you need this code to be easily testable?
        YES → Use Functional ✅
        NO → Continue
             ↓
        Is performance critical and you need parallelization?
            YES → Use Functional ✅
            NO → Continue
                 ↓
            Is this mostly I/O operations (files, network, DB)?
                YES → Use Procedural ⚙️
                NO → Continue
                     ↓
                Does it have complex mutable state?
                    YES → Use Procedural ⚙️ (or OOP)
                    NO → Continue
                         ↓
                    Is it a simple script?
                        YES → Use Procedural ⚙️
                        NO → Use Functional ✅
```

---

## 📊 Real-World Examples

### Example 1: Web Scraper
```python
# FUNCTIONAL for data processing
def scrape_website(url):
    # Procedural I/O
    html = fetch_page(url)

    # Functional data processing
    products = extract_products(html)
    valid_products = list(filter(is_valid_product, products))
    cleaned = list(map(clean_product_data, valid_products))

    # Procedural I/O
    save_to_database(cleaned)
```
**Mix of both!** I/O is procedural, data processing is functional.

---

### Example 2: Data Analytics
```python
# FUNCTIONAL - perfect for data transformation
def analyze_sales(data):
    # All functional - pure transformations
    filtered = filter(lambda x: x['date'] >= '2025-01-01', data)
    by_category = group_by(filtered, key='category')
    totals = {k: sum(map(lambda x: x['amount'], v))
              for k, v in by_category.items()}
    return totals
```
**All functional!** Pure data transformation.

---

### Example 3: CLI Tool
```python
# PROCEDURAL - simple sequential steps
def main():
    print("Welcome!")

    filename = input("Enter filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    process_file(filename)
    print("Done!")
```
**All procedural!** Simple user interaction.

---

## 🎓 Key Principles

### Choose Functional When:
1. ✅ Data flows through transformations
2. ✅ Functions don't need to remember state
3. ✅ You want easy testing
4. ✅ Parallelization might be needed
5. ✅ Code is about "what" not "how"

### Choose Procedural When:
1. ✅ Step-by-step instructions make sense
2. ✅ Lots of I/O operations
3. ✅ State management is central
4. ✅ Simplicity trumps elegance
5. ✅ Code is about "how" not "what"

---

## 💡 Pro Tips

### 1. **Mix Both Styles**
Most real code uses both! Use functional for data processing and procedural for I/O.

```python
def process_csv(filename):
    # Procedural: I/O
    with open(filename) as f:
        data = csv.reader(f)

    # Functional: data processing
    valid_rows = filter(is_valid_row, data)
    transformed = map(transform_row, valid_rows)
    results = list(transformed)

    # Procedural: I/O
    save_to_db(results)
```

### 2. **Start Simple**
Don't force functional style. If procedural is clearer, use it!

### 3. **Pure Functions Are Your Friend**
Even in procedural code, write pure functions when possible:
```python
# Good: Pure function (testable)
def calculate_tax(amount):
    return amount * 0.08

# Bad: Impure function (hard to test)
tax_total = 0
def add_tax(amount):
    global tax_total
    tax_total += amount * 0.08
```

### 4. **Functional Doesn't Mean Lambda Everywhere**
```python
# Don't do this
result = list(filter(lambda x: x > 0,
              map(lambda x: x * 2,
              filter(lambda x: x % 2 == 0, numbers))))

# Do this instead
def is_even(x): return x % 2 == 0
def double(x): return x * 2
def is_positive(x): return x > 0

result = list(filter(is_positive,
              map(double,
              filter(is_even, numbers))))
```

---

## 🎯 Bottom Line

**There's no "always use functional" or "always use procedural".**

The best code:
- ✅ Uses functional for data transformation
- ✅ Uses procedural for I/O and simple scripts
- ✅ Uses OOP for complex state management
- ✅ Mixes styles based on what's clearest

**Choose the style that makes your code:**
- Easier to read
- Easier to test
- Easier to maintain
- Easier for your team to understand
