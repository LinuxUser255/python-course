#!/usr/bin/env python3

"""
Real-World Use Cases: When to Use Functional Programming Over Procedural

This guide shows practical scenarios where functional programming shines,
with actual code examples you might encounter in real projects.
"""

# ============================================================================
# USE CASE 1: DATA TRANSFORMATION PIPELINES
# ============================================================================

print("=" * 80)
print("USE CASE 1: DATA TRANSFORMATION PIPELINES")
print("=" * 80)

print("""
SCENARIO: You're processing user data from an API - filtering, transforming,
and calculating statistics. Functional programming makes this cleaner and
easier to reason about.
""")

# Sample data from API
users = [
    {"name": "Alice", "age": 28, "salary": 75000, "department": "Engineering"},
    {"name": "Bob", "age": 35, "salary": 95000, "department": "Engineering"},
    {"name": "Charlie", "age": 42, "salary": 60000, "department": "Sales"},
    {"name": "Diana", "age": 29, "salary": 80000, "department": "Engineering"},
    {"name": "Eve", "age": 38, "salary": 55000, "department": "Marketing"},
    {"name": "Frank", "age": 31, "salary": 70000, "department": "Sales"},
]

# PROCEDURAL (messy, hard to follow)
print("\n--- PROCEDURAL APPROACH ---")
def procedural_process_users():
    # Filter engineers
    engineers = []
    for user in users:
        if user["department"] == "Engineering":
            engineers.append(user)
    
    # Filter those making over 70k
    high_earners = []
    for engineer in engineers:
        if engineer["salary"] > 70000:
            high_earners.append(engineer)
    
    # Get names
    names = []
    for person in high_earners:
        names.append(person["name"])
    
    # Calculate average salary
    total = 0
    count = 0
    for person in high_earners:
        total += person["salary"]
        count += 1
    avg_salary = total / count if count > 0 else 0
    
    return names, avg_salary

names, avg = procedural_process_users()
print(f"High-earning engineers: {names}")
print(f"Average salary: ${avg:,.2f}")


# FUNCTIONAL (clean, declarative, composable)
print("\n--- FUNCTIONAL APPROACH ---")
from functools import reduce

def functional_process_users():
    # Create a pipeline of transformations
    result = (
        users
        # Step 1: Filter for engineers
        | (lambda data: filter(lambda u: u["department"] == "Engineering", data))
        # Step 2: Filter for high earners
        | (lambda data: filter(lambda u: u["salary"] > 70000, data))
        # Step 3: Convert to list
        | (lambda data: list(data))
    )
    
    # Extract names
    names = list(map(lambda u: u["name"], result))
    
    # Calculate average salary
    avg_salary = (
        reduce(lambda acc, u: acc + u["salary"], result, 0) / len(result)
        if result else 0
    )
    
    return names, avg_salary

# Even cleaner with helper functions
def is_engineer(user):
    return user["department"] == "Engineering"

def earns_over_70k(user):
    return user["salary"] > 70000

def get_name(user):
    return user["name"]

def get_salary(user):
    return user["salary"]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Cleanest version
high_earning_engineers = list(filter(earns_over_70k, filter(is_engineer, users)))
names = list(map(get_name, high_earning_engineers))
salaries = list(map(get_salary, high_earning_engineers))
avg = calculate_average(salaries)

print(f"High-earning engineers: {names}")
print(f"Average salary: ${avg:,.2f}")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • Each step is isolated and testable
  • Easy to add/remove transformation steps
  • No temporary variables cluttering the code
  • Clear data flow (input → transformation → output)
  • Easy to parallelize later
""")


# ============================================================================
# USE CASE 2: TESTING - PURE FUNCTIONS ARE EASIER TO TEST
# ============================================================================

print("\n" + "=" * 80)
print("USE CASE 2: TESTING - PURE FUNCTIONS ARE EASIER TO TEST")
print("=" * 80)

print("""
SCENARIO: You need to write unit tests. Pure functions are dramatically
easier to test because they have no side effects or hidden dependencies.
""")

# PROCEDURAL (hard to test - has global state)
print("\n--- PROCEDURAL (HARD TO TEST) ---")

total_revenue = 0  # Global state

def procedural_process_sale(amount, discount_percent):
    global total_revenue
    discounted = amount - (amount * discount_percent / 100)
    total_revenue += discounted  # Side effect - modifies global state
    print(f"Sale processed: ${discounted:.2f}")  # Side effect - prints
    if discounted > 100:
        print("Big sale!")  # Side effect - prints
    return discounted

# Testing this is painful:
# - Need to reset global state before each test
# - Can't test in parallel
# - Print statements clutter test output

result = procedural_process_sale(150, 10)
print(f"Total revenue so far: ${total_revenue:.2f}")


# FUNCTIONAL (easy to test - pure function)
print("\n--- FUNCTIONAL (EASY TO TEST) ---")

def functional_process_sale(amount, discount_percent):
    """Pure function - no side effects, same input = same output."""
    return amount - (amount * discount_percent / 100)

def is_big_sale(amount):
    """Pure function - easy to test."""
    return amount > 100

def calculate_total_revenue(sales):
    """Pure function - easy to test."""
    return sum(sales)

# Testing is trivial:
sale_amount = functional_process_sale(150, 10)
print(f"Sale amount: ${sale_amount:.2f}")
print(f"Is big sale: {is_big_sale(sale_amount)}")

sales = [135, 90, 200, 75]
total = calculate_total_revenue(sales)
print(f"Total revenue: ${total:.2f}")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • No setup/teardown needed for tests
  • Tests run in any order
  • Tests can run in parallel
  • No mocking required
  • Predictable: same input always gives same output
""")


# ============================================================================
# USE CASE 3: PARALLEL/CONCURRENT PROCESSING
# ============================================================================

print("\n" + "=" * 80)
print("USE CASE 3: PARALLEL/CONCURRENT PROCESSING")
print("=" * 80)

print("""
SCENARIO: You need to process large amounts of data quickly using multiple
CPU cores. Functional programming makes parallelization safe and easy.
""")

import time
from multiprocessing import Pool

# Expensive computation (simulated)
def expensive_calculation(n):
    """Simulates a CPU-intensive task."""
    time.sleep(0.1)  # Simulate work
    return n * n

numbers = list(range(20))

# PROCEDURAL (sequential - slow)
print("\n--- PROCEDURAL (SEQUENTIAL) ---")
start = time.time()

results_procedural = []
for n in numbers:
    results_procedural.append(expensive_calculation(n))

procedural_time = time.time() - start
print(f"Procedural time: {procedural_time:.2f} seconds")
print(f"Results sample: {results_procedural[:5]}")


# FUNCTIONAL (parallel - fast)
print("\n--- FUNCTIONAL (PARALLEL) ---")
start = time.time()

with Pool() as pool:
    results_functional = pool.map(expensive_calculation, numbers)

functional_time = time.time() - start
print(f"Functional time: {functional_time:.2f} seconds")
print(f"Results sample: {results_functional[:5]}")
print(f"Speedup: {procedural_time / functional_time:.2f}x faster")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • Pure functions have no shared state (safe to parallelize)
  • No race conditions or deadlocks
  • Easy to use with multiprocessing/threading
  • Scales to multiple cores automatically
  • No need for locks or synchronization
""")


# ============================================================================
# USE CASE 4: API RESPONSE PROCESSING
# ============================================================================

print("\n" + "=" * 80)
print("USE CASE 4: API RESPONSE PROCESSING")
print("=" * 80)

print("""
SCENARIO: You're building a web scraper or consuming multiple APIs.
You need to clean, validate, and transform the data.
""")

# Sample API responses (messy real-world data)
api_responses = [
    {"id": 1, "name": "Product A", "price": "29.99", "stock": "15", "category": "electronics"},
    {"id": 2, "name": "Product B", "price": "invalid", "stock": "0", "category": "electronics"},
    {"id": 3, "name": "", "price": "49.99", "stock": "8", "category": ""},
    {"id": 4, "name": "Product D", "price": "19.99", "stock": "20", "category": "books"},
    {"id": 5, "name": "Product E", "price": "99.99", "stock": "-5", "category": "electronics"},
]

# PROCEDURAL (error-prone, hard to maintain)
print("\n--- PROCEDURAL ---")
def procedural_clean_data():
    valid_products = []
    
    for product in api_responses:
        # Validate and clean
        if product["name"] == "" or product["category"] == "":
            continue
        
        try:
            price = float(product["price"])
        except ValueError:
            continue
        
        try:
            stock = int(product["stock"])
        except ValueError:
            continue
        
        if stock < 0:
            continue
        
        if price <= 0:
            continue
        
        # Transform
        cleaned = {
            "id": product["id"],
            "name": product["name"].strip().title(),
            "price": price,
            "stock": stock,
            "category": product["category"].strip().title(),
            "in_stock": stock > 0
        }
        
        valid_products.append(cleaned)
    
    return valid_products

cleaned = procedural_clean_data()
print(f"Valid products: {len(cleaned)}")
for p in cleaned:
    print(f"  {p['name']}: ${p['price']:.2f} ({p['stock']} in stock)")


# FUNCTIONAL (composable, testable, clear)
print("\n--- FUNCTIONAL ---")

def has_required_fields(product):
    """Validate required fields are present."""
    return product.get("name") and product.get("category")

def parse_price(product):
    """Try to parse price, return None if invalid."""
    try:
        return {**product, "price": float(product["price"])}
    except (ValueError, KeyError):
        return None

def parse_stock(product):
    """Try to parse stock, return None if invalid."""
    try:
        return {**product, "stock": int(product["stock"])}
    except (ValueError, KeyError):
        return None

def has_valid_values(product):
    """Validate business rules."""
    return (
        product.get("price", 0) > 0 and
        product.get("stock", -1) >= 0
    )

def transform_product(product):
    """Clean and enhance product data."""
    return {
        "id": product["id"],
        "name": product["name"].strip().title(),
        "price": product["price"],
        "stock": product["stock"],
        "category": product["category"].strip().title(),
        "in_stock": product["stock"] > 0
    }

# Build a processing pipeline
def process_api_responses(responses):
    return list(
        map(transform_product,
            filter(has_valid_values,
                filter(None,  # Remove None values
                    map(parse_stock,
                        filter(None,
                            map(parse_price,
                                filter(has_required_fields, responses)
                            )
                        )
                    )
                )
            )
        )
    )

cleaned_functional = process_api_responses(api_responses)
print(f"Valid products: {len(cleaned_functional)}")
for p in cleaned_functional:
    print(f"  {p['name']}: ${p['price']:.2f} ({p['stock']} in stock)")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • Each validation step is a separate, testable function
  • Easy to add/remove validation rules
  • Clear pipeline: input → validate → parse → transform → output
  • Each function has single responsibility
  • Easy to reuse functions in other contexts
""")


# ============================================================================
# USE CASE 5: CONFIGURATION AND FEATURE FLAGS
# ============================================================================

print("\n" + "=" * 80)
print("USE CASE 5: CONFIGURATION AND FEATURE FLAGS")
print("=" * 80)

print("""
SCENARIO: Your app has different configurations for different environments
or users. Pure functions make it easy to compute configurations without
global state.
""")

# PROCEDURAL (global state, hard to test different configs)
print("\n--- PROCEDURAL ---")

# Global configuration
ENVIRONMENT = "production"
DEBUG_MODE = False

def procedural_get_api_url():
    global ENVIRONMENT
    if ENVIRONMENT == "production":
        return "https://api.example.com"
    elif ENVIRONMENT == "staging":
        return "https://staging-api.example.com"
    else:
        return "http://localhost:3000"

def procedural_should_log():
    global DEBUG_MODE
    return DEBUG_MODE

print(f"API URL: {procedural_get_api_url()}")
print(f"Should log: {procedural_should_log()}")


# FUNCTIONAL (pass config explicitly, easy to test)
print("\n--- FUNCTIONAL ---")

def functional_get_api_url(environment):
    """Pure function - easy to test all environments."""
    urls = {
        "production": "https://api.example.com",
        "staging": "https://staging-api.example.com",
        "development": "http://localhost:3000"
    }
    return urls.get(environment, urls["development"])

def functional_should_log(config):
    """Pure function - easy to test."""
    return config.get("debug", False)

def get_timeout(environment):
    """Pure function - compute timeout based on environment."""
    timeouts = {"production": 30, "staging": 60, "development": 120}
    return timeouts.get(environment, 30)

# Configuration is just data
config = {
    "environment": "production",
    "debug": False,
    "features": {"new_ui": True, "beta_api": False}
}

print(f"API URL: {functional_get_api_url(config['environment'])}")
print(f"Should log: {functional_should_log(config)}")
print(f"Timeout: {get_timeout(config['environment'])}s")

# Easy to test different configurations
test_configs = [
    {"environment": "production", "debug": False},
    {"environment": "staging", "debug": True},
    {"environment": "development", "debug": True},
]

print("\nTesting all configurations:")
for cfg in test_configs:
    print(f"  {cfg['environment']}: {functional_get_api_url(cfg['environment'])}")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • No global state - easy to test different configs
  • Can run multiple configurations simultaneously
  • Configuration is explicit (passed as argument)
  • Easy to test all combinations
  • No surprising behavior from hidden global state
""")


# ============================================================================
# USE CASE 6: EVENT PROCESSING / LOG ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("USE CASE 6: EVENT PROCESSING / LOG ANALYSIS")
print("=" * 80)

print("""
SCENARIO: You're analyzing application logs or processing event streams.
Functional composition makes complex queries simple and declarative.
""")

# Sample log entries
logs = [
    {"timestamp": "2025-01-15 10:23:45", "level": "INFO", "user": "alice", "action": "login"},
    {"timestamp": "2025-01-15 10:24:12", "level": "ERROR", "user": "bob", "action": "payment_failed"},
    {"timestamp": "2025-01-15 10:25:33", "level": "INFO", "user": "alice", "action": "view_product"},
    {"timestamp": "2025-01-15 10:26:01", "level": "ERROR", "user": "charlie", "action": "login_failed"},
    {"timestamp": "2025-01-15 10:27:15", "level": "INFO", "user": "alice", "action": "purchase"},
    {"timestamp": "2025-01-15 10:28:42", "level": "ERROR", "user": "bob", "action": "timeout"},
    {"timestamp": "2025-01-15 10:29:03", "level": "WARNING", "user": "diana", "action": "slow_query"},
]

# PROCEDURAL
print("\n--- PROCEDURAL ---")
def procedural_analyze_logs():
    # Find users with errors
    users_with_errors = set()
    for log in logs:
        if log["level"] == "ERROR":
            users_with_errors.add(log["user"])
    
    # Count errors per user
    error_counts = {}
    for log in logs:
        if log["level"] == "ERROR":
            user = log["user"]
            if user in error_counts:
                error_counts[user] += 1
            else:
                error_counts[user] = 1
    
    # Get error actions
    error_actions = []
    for log in logs:
        if log["level"] == "ERROR":
            error_actions.append(log["action"])
    
    return users_with_errors, error_counts, error_actions

users, counts, actions = procedural_analyze_logs()
print(f"Users with errors: {users}")
print(f"Error counts: {counts}")
print(f"Error actions: {actions}")


# FUNCTIONAL
print("\n--- FUNCTIONAL ---")
from collections import Counter

def is_error(log):
    return log["level"] == "ERROR"

def get_user(log):
    return log["user"]

def get_action(log):
    return log["action"]

def functional_analyze_logs(logs):
    # Get all error logs
    error_logs = list(filter(is_error, logs))
    
    # Extract users
    users_with_errors = set(map(get_user, error_logs))
    
    # Count errors per user
    error_counts = Counter(map(get_user, error_logs))
    
    # Get error actions
    error_actions = list(map(get_action, error_logs))
    
    return users_with_errors, error_counts, error_actions

users_f, counts_f, actions_f = functional_analyze_logs(logs)
print(f"Users with errors: {users_f}")
print(f"Error counts: {dict(counts_f)}")
print(f"Error actions: {actions_f}")

# Bonus: Easy to compose more complex queries
print("\n--- COMPLEX QUERY (FUNCTIONAL) ---")
def is_alice(log):
    return log["user"] == "alice"

def is_purchase_or_view(log):
    return log["action"] in ["purchase", "view_product"]

# What did Alice purchase or view?
alice_shopping = list(
    map(get_action,
        filter(is_purchase_or_view,
            filter(is_alice, logs)
        )
    )
)
print(f"Alice's shopping actions: {alice_shopping}")

print("""
✅ WHY FUNCTIONAL WINS HERE:
  • Queries are declarative (what, not how)
  • Easy to compose complex filters
  • Each filter is reusable
  • Easy to build query DSL
  • Reads like SQL (filter, map, reduce)
""")


# ============================================================================
# SUMMARY: WHEN TO USE FUNCTIONAL
# ============================================================================

print("\n" + "=" * 80)
print("SUMMARY: WHEN TO USE FUNCTIONAL PROGRAMMING")
print("=" * 80)

print("""
USE FUNCTIONAL WHEN:

1. ✅ DATA TRANSFORMATIONS
   - Processing lists, filtering, mapping
   - ETL pipelines (Extract, Transform, Load)
   - Data cleaning and validation

2. ✅ TESTING IS CRITICAL
   - Need predictable, testable code
   - Complex business logic
   - Mathematical computations

3. ✅ PARALLEL PROCESSING
   - Multi-core CPU usage
   - Big data processing
   - Independent computations

4. ✅ API/DATA PROCESSING
   - Web scraping
   - API consumption
   - JSON/data transformation

5. ✅ CONFIGURATION
   - Computing settings
   - Feature flags
   - Environment-specific behavior

6. ✅ EVENT PROCESSING
   - Log analysis
   - Stream processing
   - Complex filtering

7. ✅ COMPOSABILITY MATTERS
   - Building pipelines
   - Reusing logic
   - Combining operations


USE PROCEDURAL WHEN:

1. ✅ SIMPLE SCRIPTS
   - One-off tasks
   - Small programs
   - Learning basics

2. ✅ I/O HEAVY
   - File operations
   - Network requests
   - Database queries

3. ✅ STATEFUL SYSTEMS
   - Games (lots of mutable state)
   - UI applications
   - Real-time systems

4. ✅ PERFORMANCE CRITICAL
   - Tight loops
   - System programming
   - Low-level operations

5. ✅ TEAM PREFERENCE
   - Team knows procedural better
   - Legacy codebase
   - Company standards


REALITY: MOST REAL PROJECTS USE BOTH!

Example: Web API
  • Functional: Data validation, transformation
  • Procedural: Database queries, HTTP handling
  • OOP: Controllers, models, services
""")


print("\n" + "=" * 80)
print("KEY TAKEAWAY")
print("=" * 80)
print("""
Functional programming isn't about using lambdas everywhere.
It's about:
  • Writing pure functions (predictable, testable)
  • Avoiding side effects where possible
  • Treating data as immutable
  • Composing small functions into larger ones

Use it when these principles make your code:
  ✓ Easier to understand
  ✓ Easier to test
  ✓ Easier to maintain
  ✓ Easier to parallelize

Don't force it when procedural is clearer!
""")
