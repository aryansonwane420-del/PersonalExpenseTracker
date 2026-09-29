def calculate_total(expenses):
    return sum(
        expense.amount
        for expense in expenses
    )


def category_summary(expenses):

    summary = {}

    for expense in expenses:

        category = expense.category

        if category not in summary:
            summary[category] = 0

        summary[category] += expense.amount

    return summary


def payment_method_summary(expenses):

    summary = {}

    for expense in expenses:

        method = expense.payment_method

        if method not in summary:
            summary[method] = 0

        summary[method] += expense.amount

    return summary


def generate_report(expenses):

    total = calculate_total(expenses)

    print("\n========== EXPENSE REPORT ==========")

    print(f"Total Expenses: ₹{total:.2f}")

    print("\nCategory-wise Spending:")

    categories = category_summary(expenses)

    if categories:
        for category, amount in categories.items():
            print(f"{category}: ₹{amount:.2f}")
    else:
        print("No category data available.")

    print("\nPayment Method Summary:")

    methods = payment_method_summary(expenses)

    if methods:
        for method, amount in methods.items():
            print(f"{method}: ₹{amount:.2f}")
    else:
        print("No payment method data available.")

    print("====================================")