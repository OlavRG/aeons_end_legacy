# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:44:27 2023

@author: olavg
"""

from player import Player
from card import Card


class Crystal(Card):
    def __init__(self):
        self.name = 'Crystal'
        self.type = 'gem'
        self.cost = 0

    def resolve_effect(self, player):
        player.energy += 1
        print(f"{player.name} plays a {self.name}")

class Spark(Card):
    def __init__(self):
        self.name = 'Spark'
        self.type = 'spell'
        self.cost = 0

    def cast(self, player):
        player.damage_dealt += 1
        print(f"{player.name} cast {self.name}")

#TO DO: spells: Force Transfusion, Bending beam, Fire Chakram, gravity node