class Currency:
    def __init__(self, currency_code):
        self.currency_code = currency_code

    def __eq__(self, other):
        if isinstance(other, Currency):
            return self.currency_code == other.currency_code
        return False

    def __repr__(self):
        return self.currency_code
