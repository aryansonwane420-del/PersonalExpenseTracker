def search_expenses(expenses, keyword):
    keyword = keyword.lower()

    results = []

    for expense in expenses:
        if (
            keyword in expense.description.lower()
            or keyword in expense.category.lower()
        ):
            results.append(expense)

    return results


def filter_by_category(expenses, category):
    return [
        expense
        for expense in expenses
        if expense.category.lower() == category.lower()
    ]


def filter_by_payment_method(expenses, payment_method):
    return [
        expense
        for expense in expenses
        if expense.payment_method.lower() == payment_method.lower()
    ]