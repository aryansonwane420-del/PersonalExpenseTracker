# Project Statement — Personal Expense Tracker

## 1. Project Title

**Personal Expense Tracker**

---

## 2. Problem Statement

Managing personal expenses manually can be difficult when the number of transactions increases. Users may find it difficult to remember where money was spent, calculate total expenditure, compare spending across categories, and track different payment methods.

The Personal Expense Tracker is designed to provide a simple computerized solution for recording and managing personal expenses. The system allows users to add, view, update, delete, search, and filter expense records. It also generates summary reports to help users understand their spending.

---

## 3. Scope of the Project

The project focuses on developing a Python-based console application for managing personal expense records.

The system includes:

- Expense creation and management
- Expense modification and deletion
- Expense searching
- Expense filtering
- Input validation
- Persistent JSON-based storage
- Total expense calculation
- Category-wise expense analysis
- Payment-method-wise expense analysis
- Automated testing

The current project is intended for individual users and uses local JSON storage.

The project does not currently include online banking integration, cloud synchronization, or multi-user functionality.

---

## 4. Target Users

The primary target users are:

### Students

Students can use the system to track daily expenses such as:

- Food
- Travel
- Education
- Entertainment
- Shopping

### Individual Users

Individuals can use the application to maintain a simple record of personal spending.

### Users Learning Python

The project can also serve as an example of applying Python programming concepts to a real-world problem.

---

## 5. High-Level Features

### 5.1 Expense Management

Users can:

- Add a new expense
- View all expenses
- Update an existing expense
- Delete an expense

---

### 5.2 Expense Search

Users can search expenses using keywords from:

- Expense description
- Expense category

---

### 5.3 Expense Filtering

Users can filter expenses based on:

- Category
- Payment method

---

### 5.4 Expense Reports

The system calculates and displays:

- Total expenditure
- Category-wise expenditure
- Payment-method-wise expenditure

---

### 5.5 Data Storage

Expense records are stored persistently in a JSON file.

The storage file is:

```text
data/expenses.json