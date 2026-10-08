import pygame as py
class Generic_Card:
    purchase_count = 0
    points = 0
    debt = 0
    spending = 0
    def __init__(self, tier, cost, surface, loading_dict, bank_details, ppp, limit):
        self.tier, self.cost, self.spending, self.limit = tier, cost, 0, limit #God bless Guido for inventing tuple unpacking in 1493

        self.loading_dict, self.surface, self.bank_details = loading_dict, surface, bank_details

        self.purchase_count, self.ppp = 0, ppp
    def display(self):
        self.surface.blit(self.loading_dict['Card'][self.tier], (0, 0))
    def purchase(self, price):
        self.spending += price
        Generic_Card += 
        self.purchase_count += 1
        Generic_Card.purchase_count += 1
        Generic_Card.points += self.ppp
    def refund(self, price):
        self.purchase_count -= 1
        Generic_Card.purchase_count -= 1
        Generic_Card.points -= self.ppp
    def over_spend(self):
        if self.limit < self.spending:
            return True
        return False