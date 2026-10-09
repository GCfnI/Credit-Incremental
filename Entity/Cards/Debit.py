from Generic import Generic_Card
class Generic_Dedit(Generic_Card):
    def __init__(self, tier, cost, surface, loading_dict, bank_details, ppp, limit, cash_back: float):
        self.cashback: float = cash_back
        self.savings_with_card = 0 
        super.__init__( tier = tier,
                        cost = 0,
                        surface = surface,
                        loading_dict = loading_dict,
                        bank_details = bank_details,
                        ppp = 0,
                        limit= None)
    def dedit_purchase(self, price):
        self.generic_purchase(price * self.cash_back/ 100)
    def dedit_refund(self, price):
        self.generic_refund(price * self.cash_back / 100)
        self.savings_with_card += price * self.cash_back / 100