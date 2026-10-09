import pygame as py
class Generic_Card:
    purchase_count = 0
    points = 0
    debt = 0
    spending = 0
    def __init__(self, tier, cost, surface, loading_dict, bank_details, ppp):
        self.tier: str = tier 
        self.cost: float = cost
        self.balance: float = 0
        self.purchase_count: int = 0 
        self.ppp: float = ppp
        self.loading_dict, self.surface, self.bank_details = loading_dict, surface, bank_details

    def generic_purchase(self, price):
        self.spending += price
        self.purchase_count += 1
        Generic_Card.purchase_count += 1
        Generic_Card.balance += price
        Generic_Card.points += self.ppp
    def generic_refund(self, price):
        self.purchase_count -= 1
        Generic_Card.purchase_count -= 1
        Generic_Card.points -= self.ppp
        self.balance -= price