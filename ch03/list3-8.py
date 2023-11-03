import Currency

# PEP591で追加
# https://peps.python.org/pep-0591/
from typing import Final


class Money:
    amount: Final[int]
    currency: Final[Currency.Currency]

    def __init__(self, amount, currency):
        if amount < 0:
            raise ValueError("金額には0以上を指定してください。")
        if not currency:
            raise ValueError("通貨単位を指定してください。")

        self.amount = amount
        self.currency = currency


yen = Currency.Currency("yen")
money = Money(100, yen)
money.amount = 32
print(money.amount)


