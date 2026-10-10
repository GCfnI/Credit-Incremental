from Typed_Dict import Banking_Details
class Generic_Credit:
    def __init__(self, ppd: float, banking_details: Banking_Details,  limit: int, cash_back: float, covered: bool, overdraft_fee: int):
        self.cashback = cash_back
        self.savings: float = 0
        self.limit = limit
        self.covered =  covered
        self.balance: float = 0
        self.banking_details = banking_details
        self.ppd = ppd
        self.overdraft_fee = overdraft_fee

    def __add__(self, price):
        if self.balance + price >= self.limit and not self.covered:
            return False
        if self.balance + price >= self.limit and self.covered:
            self.balance += self.overdraft_fee
            self.banking_details['credit_score'] -= 10
        self.balance += price * (1-self.cash_back)
        self.banking_details['points'] += price * self.ppd
        self.savings += price * self.cash_back
        return True

    def __sub__(self, price):
        self.balance -= price * self.cash_back
        self.banking_details['points'] -= price * self.ppd
        self.savings -= price * self.cash_back