from expense_manager import ExpenseManager

from search import (
    search_expenses,
    filter_by_category,
    filter_by_payment_method
)

from report import generate_report

from validator import (
    validate_description,
    validate_category,
    validate_amount,
    validate_date,
    validate_payment_method,
    validate_expense_id
)


manager = ExpenseManager()


def display_expense(expense):

    print(
        f"ID: {expense.expense_id} | "
        f"Description: {expense.description} | "
        f"Category: {expense.category} | "
        f"Amount: ₹{expense.amount:.2f} | "
        f"Date: {expense.date} | "
        f"Payment: {expense.payment_method}"
    )


def add_expense():

    print("\n========== ADD EXPENSE ==========")

    description = input("Enter description: ")

    if not validate_description(description):
        print("Error: Description cannot be empty.")
        return

    category = input("Enter category: ")

    if not validate_category(category):
        print("Error: Category cannot be empty.")
        return

    amount = input("Enter amount: ")

    if not validate_amount(amount):
        print("Error: Amount must be greater than 0.")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    if not validate_date(date):
        print("Error: Date cannot be empty.")
        return

    payment_method = input(
        "Enter payment method "
        "(Cash/UPI/Card/Bank Transfer): "
    )

    if not validate_payment_method(payment_method):
        print("Error: Invalid payment method.")
        return

    expense = manager.add_expense(
        description,
        category,
        amount,
        date,
        payment_method.title()
    )

    print(
        f"Expense added successfully! "
        f"Expense ID: {expense.expense_id}"
    )


def view_expenses():

    print("\n========== ALL EXPENSES ==========")

    expenses = manager.get_all_expenses()

    if not expenses:
        print("No expenses available.")
        return

    for expense in expenses:
        display_expense(expense)


def update_expense():

    print("\n========== UPDATE EXPENSE ==========")

    expense_id = input("Enter expense ID: ")

    if not validate_expense_id(expense_id):
        print("Invalid expense ID.")
        return

    expense_id = int(expense_id)

    expense = manager.find_expense(expense_id)

    if expense is None:
        print("Expense not found.")
        return

    description = input("Enter new description: ")
    category = input("Enter new category: ")
    amount = input("Enter new amount: ")
    date = input("Enter new date: ")

    payment_method = input(
        "Enter new payment method "
        "(Cash/UPI/Card/Bank Transfer): "
    )

    if not validate_description(description):
        print("Invalid description.")
        return

    if not validate_category(category):
        print("Invalid category.")
        return

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    if not validate_date(date):
        print("Invalid date.")
        return

    if not validate_payment_method(payment_method):
        print("Invalid payment method.")
        return

    manager.update_expense(
        expense_id,
        description,
        category,
        amount,
        date,
        payment_method.title()
    )

    print("Expense updated successfully.")


def delete_expense():

    print("\n========== DELETE EXPENSE ==========")

    expense_id = input("Enter expense ID: ")

    if not validate_expense_id(expense_id):
        print("Invalid expense ID.")
        return

    if manager.delete_expense(int(expense_id)):
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")


def search_expense():

    print("\n========== SEARCH EXPENSE ==========")

    keyword = input("Enter keyword: ")

    results = search_expenses(
        manager.get_all_expenses(),
        keyword
    )

    if not results:
        print("No matching expenses found.")
        return

    for expense in results:
        display_expense(expense)


def filter_expenses():

    print("\n========== FILTER EXPENSES ==========")

    print("1. Filter by Category")
    print("2. Filter by Payment Method")

    choice = input("Choose option: ")

    if choice == "1":

        category = input("Enter category: ")

        results = filter_by_category(
            manager.get_all_expenses(),
            category
        )

    elif choice == "2":

        payment_method = input(
            "Enter payment method "
            "(Cash/UPI/Card/Bank Transfer): "
        )

        results = filter_by_payment_method(
            manager.get_all_expenses(),
            payment_method
        )

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching expenses found.")
        return

    for expense in results:
        display_expense(expense)


def show_report():

    print("\n========== EXPENSE REPORT ==========")

    generate_report(
        manager.get_all_expenses()
    )


def main():

    while True:

        print("\n")
        print("======================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("======================================")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Filter Expenses")
        print("7. Generate Expense Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_expense()

        elif choice == "6":
            filter_expenses()

        elif choice == "7":
            show_report()

        elif choice == "8":
            print(
                "Thank you for using "
                "Personal Expense Tracker!"
            )
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()