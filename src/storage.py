import json
import os


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "expenses.json"
)


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file, indent=4)

        return True

    except OSError:
        return False