# Personal Expense Tracker

## 1. Project Overview

Personal Expense Tracker is a Python-based console application designed to help users record, manage, search, filter, and analyze their daily expenses.

The application provides a simple and structured way to maintain expense records without requiring a database. Expense information is stored persistently in a JSON file.

The project demonstrates important programming and software development concepts including:

- Object-Oriented Programming
- CRUD operations
- File handling
- JSON data storage
- Input validation
- Searching and filtering
- Data processing and reporting
- Modular programming
- Exception handling
- Automated testing
- Git and GitHub version control

---

## 2. Problem Statement

Managing daily expenses manually can make it difficult to keep track of spending, identify spending patterns, and calculate total expenses.

Users may have multiple expenses related to food, travel, education, shopping, entertainment, and other categories. Maintaining these records manually can become inconvenient and error-prone.

The Personal Expense Tracker provides a simple computerized solution where users can add, view, update, delete, search, and filter expense records.

The system also generates summary reports showing:

- Total spending
- Category-wise spending
- Payment-method-wise spending

---

## 3. Objectives

The main objectives of the project are:

1. To provide an easy way to record personal expenses.
2. To maintain expense records in a structured format.
3. To provide CRUD operations for expense management.
4. To allow users to search expenses.
5. To allow users to filter expenses by category and payment method.
6. To calculate total expenditure.
7. To generate category-wise spending summaries.
8. To generate payment-method-wise spending summaries.
9. To validate user input.
10. To handle invalid input and file-related errors.
11. To demonstrate modular Python programming.
12. To store data persistently using JSON.
13. To demonstrate automated software testing.
14. To maintain the project using Git and GitHub.

---

## 4. Features

### 4.1 Add Expense

Users can add a new expense by entering:

- Description
- Category
- Amount
- Date
- Payment method

Example:

```text
Description: Lunch
Category: Food
Amount: 150
Date: 29-09-2026
Payment Method: UPI
```

The system automatically generates a unique expense ID.

### 4.2 View All Expenses

Users can view all stored expenses.

Each expense displays:

- Expense ID
- Description
- Category
- Amount
- Date
- Payment method

### 4.3 Update Expense

Users can modify an existing expense using its unique expense ID.

### 4.4 Delete Expense

Users can delete an existing expense using its expense ID.

### 4.5 Search Expense

Users can search expenses using a keyword. The search checks:

- Expense description
- Expense category

### 4.6 Filter Expenses

Users can filter expenses based on:

- Category
- Payment method

### 4.7 Expense Report

The application generates a summary report containing:

- Total expenses
- Category-wise spending
- Payment-method-wise spending

Example:

```text
========== EXPENSE REPORT ==========

Total Expenses: ₹500.00

Category-wise Spending:
Food: ₹300.00
Travel: ₹200.00

Payment Method Summary:
Upi: ₹300.00
Cash: ₹200.00

====================================
```

### 4.8 Persistent Data Storage

Expense records are stored in:

```text
data/expenses.json
```

### 4.9 Input Validation

The system validates:

- Empty descriptions
- Empty categories
- Invalid amounts
- Invalid expense IDs
- Empty dates
- Invalid payment methods

Supported payment methods:

```text
Cash
UPI
Card
Bank Transfer
```

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| JSON | Persistent data storage |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |

---

## 6. System Architecture

The project follows a modular architecture where different responsibilities are separated into individual Python modules.

```text
                     USER
                       |
                       v
                  +---------+
                  | main.py |
                  +---------+
                       |
          +------------+------------+
          |            |            |
          v            v            v
   +-------------+ +----------+ +----------+
   |   Expense   | | Validator| |  Search  |
   |   Manager   | |          | |          |
   +-------------+ +----------+ +----------+
          |
          +-------------------+
          |                   |
          v                   v
   +-------------+     +-------------+
   |   Storage   |     |   Report    |
   +-------------+     +-------------+
          |
          v
   +----------------+
   | expenses.json  |
   +----------------+
```

---

## 7. Project Structure

```text
Personal-Expense-Tracker/
│
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── expense.py
│   ├── expense_manager.py
│   ├── storage.py
│   ├── validator.py
│   ├── search.py
│   └── report.py
│
├── data/
│   └── expenses.json
│
├── tests/
│   ├── test_expense.py
│   ├── test_validator.py
│   └── test_storage.py
│
├── screenshots/
│
└── docs/
    ├── architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── class_diagram.png
    └── sequence_diagram.png
```

---

## 8. Description of Modules

### `main.py`

The main entry point of the application.

Responsibilities:

- Display main menu
- Accept user input
- Call appropriate functions
- Display results
- Handle user interaction

### `expense.py`

Contains the `Expense` class.

Responsibilities:

- Represent an expense
- Convert expense objects into dictionaries
- Create expense objects from stored dictionaries

### `expense_manager.py`

Contains the `ExpenseManager` class.

Responsibilities:

- Add expenses
- View expenses
- Find expenses
- Update expenses
- Delete expenses
- Save expense data

### `storage.py`

Responsible for persistent JSON storage.

Responsibilities:

- Load expenses from JSON
- Save expenses to JSON
- Handle missing or invalid JSON files

### `validator.py`

Responsible for input validation.

Responsibilities:

- Validate descriptions
- Validate categories
- Validate amounts
- Validate dates
- Validate payment methods
- Validate expense IDs

### `search.py`

Responsible for searching and filtering expense records.

Functions include:

- Keyword search
- Category filtering
- Payment-method filtering

### `report.py`

Responsible for expense calculations and reporting.

Functions include:

- Calculate total expenses
- Generate category summary
- Generate payment-method summary
- Display expense report

---

## 9. Functional Requirements

The system shall:

### FR1 — Add Expense

Allow the user to add a new expense with required details.

### FR2 — View Expenses

Allow the user to view all stored expenses.

### FR3 — Update Expense

Allow the user to update an existing expense.

### FR4 — Delete Expense

Allow the user to delete an existing expense.

### FR5 — Search Expense

Allow the user to search expenses using keywords.

### FR6 — Filter Expense

Allow the user to filter expenses by category or payment method.

### FR7 — Generate Report

Calculate total expenditure and generate spending summaries.

### FR8 — Persistent Storage

Save expense information so that it remains available after restarting the application.

### FR9 — Input Validation

Reject invalid or incomplete user input.

---

## 10. Non-Functional Requirements

### 10.1 Performance

The application should process normal personal expense records quickly.

### 10.2 Usability

The system uses a simple menu-driven console interface.

### 10.3 Reliability

Expense data is stored persistently in a JSON file.

### 10.4 Maintainability

The application is divided into multiple modules, making it easier to modify and maintain.

### 10.5 Error Handling

The application validates user input and handles file and JSON-related errors.

### 10.6 Scalability

The modular architecture allows the project to be extended with database storage, graphical interfaces, and additional reporting features.

---

## 11. Requirements

The project requires:

- Python 3.8 or higher
- pip
- Git

For automated testing:

```text
pytest
```

---

## 12. Installation

### Step 1 — Clone the Repository

Replace the repository URL with your GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2 — Open the Project Directory

```bash
cd Personal-Expense-Tracker
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 13. Running the Application

From the project root directory, run:

```bash
python src/main.py
```

The application will display the main menu.

```text
======================================
       PERSONAL EXPENSE TRACKER
======================================

1. Add Expense
2. View All Expenses
3. Update Expense
4. Delete Expense
5. Search Expense
6. Filter Expenses
7. Generate Expense Report
8. Exit

Enter your choice:
```

---

## 14. Example Usage

### Add an Expense

```text
========== ADD EXPENSE ==========

Enter description: Lunch
Enter category: Food
Enter amount: 150
Enter date (DD-MM-YYYY): 29-09-2026
Enter payment method (Cash/UPI/Card/Bank Transfer): UPI

Expense added successfully! Expense ID: 1
```

### View Expenses

```text
========== ALL EXPENSES ==========

ID: 1 | Description: Lunch | Category: Food | Amount: ₹150.00 | Date: 29-09-2026 | Payment: Upi
```

### Search Expense

```text
========== SEARCH EXPENSE ==========

Enter keyword: Food

ID: 1 | Description: Lunch | Category: Food | Amount: ₹150.00 | Date: 29-09-2026 | Payment: Upi
```

### Generate Report

```text
========== EXPENSE REPORT ==========

Total Expenses: ₹150.00

Category-wise Spending:
Food: ₹150.00

Payment Method Summary:
Upi: ₹150.00

====================================
```

---

## 15. Data Storage

The application uses JSON for local persistent storage.

File:

```text
data/expenses.json
```

Example:

```json
[
    {
        "id": 1,
        "description": "Lunch",
        "category": "Food",
        "amount": 150.0,
        "date": "29-09-2026",
        "payment_method": "Upi"
    },
    {
        "id": 2,
        "description": "Bus Ticket",
        "category": "Travel",
        "amount": 50.0,
        "date": "29-09-2026",
        "payment_method": "Cash"
    }
]
```

---

## 16. CRUD Operations

The project implements all major CRUD operations.

| Operation | Description |
|---|---|
| Create | Add a new expense |
| Read | View stored expenses |
| Update | Modify an existing expense |
| Delete | Remove an expense |

---

## 17. Search and Filtering

The application provides multiple ways to locate expense records.

### Keyword Search

Searches the:

- Description
- Category

### Category Filter

Examples:

```text
Food
Travel
Education
Entertainment
Shopping
```

### Payment Method Filter

Examples:

```text
Cash
UPI
Card
Bank Transfer
```

---

## 18. Reporting and Analysis

The reporting module provides basic expense analysis.

### Total Expenses

Calculates the sum of all stored expenses.

### Category Summary

Groups expenses according to their categories.

Example:

```text
Food: ₹500
Travel: ₹300
Education: ₹200
```

### Payment Method Summary

Groups expenses according to payment method.

Example:

```text
UPI: ₹600
Cash: ₹250
Card: ₹150
```

---

## 19. Input Validation

Input validation helps prevent invalid data from entering the system.

Examples of invalid input:

```text
Empty description
Empty category
Negative amount
Zero amount
Invalid expense ID
Empty date
Invalid payment method
```

Example error:

```text
Error: Amount must be greater than 0.
```

---

## 20. Error Handling

The application includes basic error handling for:

- Invalid user input
- Invalid expense IDs
- Missing data files
- Invalid JSON files
- File read/write errors
- Invalid payment methods

The storage module catches file and JSON errors to prevent the application from crashing because of a missing or corrupted data file.

---

## 21. Testing

Automated tests are included in the `tests/` directory.

Test files:

```text
tests/
├── test_expense.py
├── test_validator.py
└── test_storage.py
```

Run all tests:

```bash
pytest
```

Run individual test files:

```bash
pytest tests/test_expense.py
pytest tests/test_validator.py
pytest tests/test_storage.py
```

Run tests with detailed output:

```bash
pytest -v
```

> Note: The test section should be considered complete after the test files have been implemented and executed successfully.

---

## 22. Git and GitHub

Git is used for version control.

Example Git workflow:

```bash
git init
git add .
git commit -m "Initial project setup"
```

Connect the project to GitHub and push:

```bash
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

Suggested meaningful commits:

```text
Initial project structure
Implemented expense management
Added JSON storage
Added validation
Added search and filtering
Added expense reports
Added automated tests
Added project documentation
Added UML diagrams
```

---

## 23. Project Workflow

The overall application workflow is:

```text
                         START
                           |
                           v
                    Display Main Menu
                           |
                           v
                    Select Operation
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
      Add Expense      View Expense     Update Expense
          |                |                |
          +----------------+----------------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
      Delete           Search/Filter      Report
          |                |                |
          +----------------+----------------+
                           |
                           v
                     Display Result
                           |
                           v
                    Return to Menu
                           |
                           v
                         Exit
```

---

## 24. Design Approach

The project follows a modular design approach.

Each module has a specific responsibility.

```text
User Interface
      |
      v
Application Logic
      |
      +---- Validation
      |
      +---- Expense Management
      |
      +---- Search and Filtering
      |
      +---- Reporting
      |
      v
Data Storage
      |
      v
JSON File
```

This separation improves:

- Maintainability
- Readability
- Testing
- Reusability
- Error handling

---

## 25. Design Decisions

### JSON Instead of Database

JSON was selected because:

- The project is designed for individual use.
- It is easy to read and modify.
- It does not require database installation.
- Python provides built-in JSON support.

### Modular Python Files

Different responsibilities are separated into different modules to make the code easier to understand and maintain.

### Object-Oriented Design

The `Expense` class represents an individual expense, while `ExpenseManager` handles expense operations.

### Automated Testing

Pytest is used to verify important components such as:

- Expense object creation
- Input validation
- Data storage

---

## 26. Security Considerations

The current application is designed for local personal use.

Security-related considerations include:

- Input validation
- Controlled file operations
- No hard-coded passwords
- No external network communication
- No collection of banking credentials

The current version does not provide authentication or encryption because it is a local academic project.

---

## 27. Project Limitations

The current version has the following limitations:

- Console-based interface
- Local JSON storage
- Single-user design
- No cloud synchronization
- No database
- No graphical dashboard
- No bank account integration
- No authentication
- No automatic budget alerts

---

## 28. Future Enhancements

The project can be extended with the following features:

1. Graphical User Interface using Tkinter or another GUI framework.
2. SQLite or MySQL database support.
3. Monthly expense reports.
4. Yearly expense reports.
5. Graphical charts.
6. Budget management.
7. Budget limit notifications.
8. CSV export.
9. PDF report generation.
10. User authentication.
11. Password-protected expense data.
12. Recurring expense support.
13. Cloud-based synchronization.
14. Mobile application.
15. Advanced financial analytics.

---

## 29. Learning Outcomes

Through this project, the following concepts are demonstrated:

- Python programming
- Object-Oriented Programming
- Classes and objects
- Functions
- Modules
- CRUD operations
- File handling
- JSON processing
- Input validation
- Exception handling
- Searching
- Filtering
- Data aggregation
- Report generation
- Modular architecture
- Automated testing
- Git
- GitHub
- Software documentation

---

## 30. Academic Requirements Covered

This project addresses the major project requirements.

### Functional Requirements

- Add expense
- View expenses
- Update expense
- Delete expense
- Search expense
- Filter expense
- Generate report

### Non-Functional Requirements

- Performance
- Usability
- Reliability
- Maintainability
- Error handling
- Scalability

### Technical Requirements

- Modular architecture
- Object-oriented programming
- JSON persistence
- Input validation
- Exception handling
- Automated testing
- Git version control
- Documentation

---

## 31. Screenshots

Screenshots can be added to the `screenshots/` directory.

Recommended screenshots:

```text
screenshots/
├── main_menu.png
├── add_expense.png
├── view_expenses.png
├── search_expense.png
└── expense_report.png
```

Example Markdown:

```markdown
## Main Menu

![Main Menu](screenshots/main_menu.png)

## Add Expense

![Add Expense](screenshots/add_expense.png)

## Expense Report

![Expense Report](screenshots/expense_report.png)
```

---

## 32. Documentation

The `docs/` directory contains project design documentation.

Expected documents:

```text
docs/
├── architecture.png
├── workflow.png
├── use_case.png
├── class_diagram.png
└── sequence_diagram.png
```

These diagrams document:

- System architecture
- Application workflow
- User interactions
- Classes and modules
- Sequence of operations

---

## 33. References

The project uses the following general technical references:

- Python Documentation
- Python JSON Documentation
- Pytest Documentation
- Git Documentation
- GitHub Documentation

---

## 34. Author

**Name:** Your Name

**Course:** Your Course Name

**College:** Your College Name

**Project:** Personal Expense Tracker

**Academic Year:** 2026

---

## 35. License

This project was developed for academic and educational purposes.

---

## 36. Conclusion

The Personal Expense Tracker provides a simple solution for recording and managing personal expenses.

The project combines Python programming, object-oriented design, JSON-based persistence, input validation, searching, filtering, reporting, automated testing, and version control.

The modular architecture also provides a foundation for future improvements such as database integration, graphical interfaces, budgeting features, data visualization, and cloud synchronization.
