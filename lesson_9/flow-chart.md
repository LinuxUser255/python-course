
```
┌────────────────────────────────────────────────────────────┐
│ 1. Interpreter starts reading from the FIRST line          │
└────────────────────────────────────────────────────────────┘
       │
       ▼
[Line X] class PhoneBook:
       │   └── Class body is executed
       │       ├── Python creates a CLASS OBJECT named PhoneBook
       │       └── Stores it in memory (namespace)
       │
       ▼
[Line Y] def search_contact(...):
       │   └── Function is defined (stored in memory)
       │
       ▼
... (Other top-level definitions) ...
       │
       ▼
[Line N] if __name__ == "__main__":
       │   └── This condition is checked.
       │       If True (script run directly):
       │
       ▼
    pb = PhoneBook()
       │   ├── Calls the CLASS (PhoneBook)
       │   ├── Allocates memory for a new INSTANCE
       │   ├── Calls __init__(self)
       │   │     ├── Sets up attributes (contacts dict, etc.)
       │   │     └── Returns None
       │   └── The instance is now stored in variable `pb`
       │
       ▼
    pb.add_contact(...)
       │   └── Finds the `add_contact` method in the instance
       │   └── Executes it, adding data to pb.contacts
       │
       ▼
    pb.search_contact(...)
       │   └── Executes search logic
       │
       ▼
[End of file → Program exits]
```



```mermaid
flowchart TD
    A[Interpreter starts at top of file] --> B[Reads class PhoneBook]
    B --> C[Creates CLASS object PhoneBook and stores in namespace]
    C --> D[Reads and stores all method definitions inside PhoneBook]
    D --> E[Continues reading file - stores other top-level functions if any]
    E --> F[Reaches if name equals main]
    F -->|Script run directly| G[Executes code inside name guard]
    G --> H[Call PhoneBook constructor - allocate memory for new instance]
    H --> I[Run init method - set up attributes like contacts dictionary]
    I --> J[Return new object reference to variable pb]
    J --> K[Call pb add_contact method - add entry to contacts dictionary]
    K --> L[Call pb search_contact method - perform search in contacts]
    L --> M[Program reaches end and exits]
```