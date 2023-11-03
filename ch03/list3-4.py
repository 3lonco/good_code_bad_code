class Money:
    def __init__(self, amount, currency):
        if amount < 0:
            raise ValueError("金額には0以上を指定してください。")
        if not currency:
            raise ValueError("通貨単位を指定してください。")

        self.amount = amount
        self.currency = currency


# ValueError: 金額には0以上を指定してください。と出力される
money = Money(-100, None)
