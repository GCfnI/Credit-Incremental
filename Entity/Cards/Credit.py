from Generic import Generic_Card
class Generic_Credit(Generic_Card):
    total_savings = 0
    def __init__(self,
                tier,
                cost,
                surface,
                loading_dict,
                bank_details,
                ppp,
                limit,
                cash_back:
                float,
                covered: bool):
        self.cashback: float = cash_back
        self.savings_with_card = 0
        self.limit = limit
        self.covered =  covered
        super.__init__( tier = tier,
                        cost = cost,
                        surface = surface,
                        loading_dict = loading_dict,
                        bank_details = bank_details,
                        ppp=ppp, limit=limit )
    def credit_purchase(self, price):
        if not self.limited():
            self.generic_purchase(price * self.cash_back/ 100)
            return True
        else:
            return False
    def credit_refund(self, price):
        self.generic_refund(price * self.cash_back / 100)
        self.savings_with_card += price * self.cash_back / 100
    def limited(self):
        maxed_out = self.balance >= self.limit
        if maxed_out and not self.covered:
            return True
        return False
    