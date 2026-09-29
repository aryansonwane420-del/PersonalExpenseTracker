class Expense:
    def __init__(
        self,
        expense_id,
        description,
        category,
        amount,
        date,
        payment_method
    ):
        self.expense_id = expense_id
        self.description = description
        self.category = category
        self.amount = amount
        self.date = date
        self.payment_method = payment_method

    def to_dict(self):
        return {
            "id": self.expense_id,
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "payment_method": self.payment_method
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["id"],
            data["description"],
            data["category"],
            data["amount"],
            data["date"],
            data["payment_method"]
        )