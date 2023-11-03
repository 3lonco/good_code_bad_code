import Currency


class Money:
    amount: int
    currency: Currency

    def __init__(self, amount, currency):
        if amount < 0:
            raise ValueError("金額には0以上を指定してください。")
        if not currency:
            raise ValueError("通貨単位を指定してください。")

        self.amount = amount
        self.currency = currency

    def add(self, other):
        self.amount += other


yen = Currency.Currency("yen")
money = Money(100, yen)
money.amount = 32
# 421
print(money.amount)
