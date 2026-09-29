from expense import Expense
from storage import load_expenses, save_expenses


class ExpenseManager:

    def __init__(self):
        self.expenses = [
            Expense.from_dict(expense)
            for expense in load_expenses()
        ]

    def get_next_id(self):
        if not self.expenses:
            return 1

        return max(
            expense.expense_id
            for expense in self.expenses
        ) + 1

    def add_expense(
        self,
        description,
        category,
        amount,
        date,
        payment_method
    ):
        expense = Expense(
            self.get_next_id(),
            description,
            category,
            float(amount),
            date,
            payment_method
        )

        self.expenses.append(expense)
        self.save()

        return expense

    def get_all_expenses(self):
        return self.expenses

    def find_expense(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense

        return None

    def update_expense(
        self,
        expense_id,
        description,
        category,
        amount,
        date,
        payment_method
    ):
        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        expense.description = description
        expense.category = category
        expense.amount = float(amount)
        expense.date = date
        expense.payment_method = payment_method

        self.save()

        return True

    def delete_expense(self, expense_id):
        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        self.expenses.remove(expense)
        self.save()

        return True

    def save(self):
        data = [
            expense.to_dict()
            for expense in self.expenses
        ]

        return save_expenses(data)