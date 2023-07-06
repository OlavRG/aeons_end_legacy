# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:44:27 2023

@author: olavg
"""

from card import Card


class Crystal(Card):
    def __init__(self):
        self.name = 'Crystal'
        self.card_type = 'gem'
        self.cost = 0
    
    def play(self, player):
        player.energy += 1
        print(f"{player.name} cast {self.name}")
        
class Spark(Card):
    def __init__(self):
        self.name = 'Spark'
        self.card_type = 'spell'
        self.cost = 0
    
    def play(self, player):
        player.damage_dealt += 1
        print(f"{player.name} cast {self.name}")
        
#TO DO: spells: Force Transfusion, Bending beam, Fire Chakram, gravity node