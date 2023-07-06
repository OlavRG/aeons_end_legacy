# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 08:58:04 2023

@author: olavg
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:21:41 2023

@author: olavg
"""

class CardPile:
    def __init__(self):
        self.pile =[]

    def __str__(self):
        return 'Cards in pile: ' + ', '.join([str(card) for card in self.pile])

    def __len__(self):
        return len(self.pile)
    
    def add_card(self, card):
        self.pile.append(card)
        
    def draw(self):
        return self.pile.pop(0)
    