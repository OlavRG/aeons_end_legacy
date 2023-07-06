# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:21:41 2023

@author: olavg
"""

from cards import *
from cardpile import CardPile

class Deck(CardPile):
    def __init__(self):
        self.pile =[]
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Spark())

    def __str__(self):
        return 'Cards in deck: ' + ', '.join([str(card) for card in self.pile])
