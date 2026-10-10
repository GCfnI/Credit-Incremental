from Typed_Dict import Banking_Details
class Generic_Credit:
    def __init__(self, ppd: float, banking_details: Banking_Details,  limit: int, cash_back: float, covered: bool, overdraft_fee: int):
        self.cashback = cash_back
        self.savings: float = 0
        self.covered =  covered
        self.balance: float = 0
        self.overdraft_fee = overdraft_fee

    def __sub__(self, price):
        if self.balance - price <= 0 and not self.covered:
            return False
        if self.balance - price <=0 and self.covered:
            self.balance -= self.overdraft_fee
        self.balance -= price * (1-self.cash_back)
        self.savings -= price * self.cash_back
        return True

    def __add__(self, price):
        self.balance += price * (1-self.cash_back)
        self.savings += price * self.cash_back
        