class Money:
    def __init__(self, amount, currency):
        if amount < 0:
            raise ValueError("金額には0以上を指定してください。")
        if not currency:
            raise ValueError("通貨単位を指定してください。")

        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.amount

    @property
    def currency(self):
        return self.currency

    def add(self, other):
        if self.currency != other.currency:
            raise ValueError("通貨単位が違います。")

        added = self.amount + other.amount
        return Money(added, self.currency)
