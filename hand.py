# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:45:39 2023

@author: olavg
"""
from cards import Crystal, Spark
from cardpile import CardPile

class Hand(CardPile):
    def __init__(self):
        self.pile =[]
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Crystal())
        self.pile.append(Spark())

    def __str__(self):
        return 'Cards in hand: ' + ', '.join([str(card) for card in self.pile])
