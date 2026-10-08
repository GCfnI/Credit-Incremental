import pygame as py
import Entity.Cards.Generic.Generic_Card as Generic_Card




class Generic_Credit_Card(Generic_Card):
    def __init__(self, tier, cost, surface, loading_dict, bank_details, points, ppp):
        super().__init__(tier, cost, surface, loading_dict, bank_details, points, ppp)


class Savings_Card(Generic_Card):
    def __init__(self, name, surface, loading_dict, bank_details,):
        super().__init__(tier = 'Savings',
                         cost = 60,
                         surface = surface,
                         loading_dict = loading_dict,
                         bank_details = bank_details)