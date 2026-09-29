def validate_description(description):
    return bool(description.strip())


def validate_category(category):
    return bool(category.strip())


def validate_amount(amount):
    try:
        return float(amount) > 0
    except ValueError:
        return False


def validate_date(date):
    return bool(date.strip())


def validate_payment_method(payment_method):
    valid_methods = [
        "cash",
        "upi",
        "card",
        "bank transfer"
    ]

    return payment_method.lower() in valid_methods


def validate_expense_id(expense_id):
    try:
        return int(expense_id) > 0
    except ValueError:
        return False