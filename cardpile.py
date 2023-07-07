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

    def add_cards(self, pile):
        self.pile = self.pile + pile

    def remove_card(self, card):
        self.pile.remove(card)

    def draw(self):
        return self.pile.pop(0)

    def get_card_from_name(self, card_name: str):
        pile_card_names = [card.name for card in self.pile]
        card_index = pile_card_names.index(card_name)
        card = self.pile[card_index]
        return card

    def get_card_from_type(self, card_type: str):
        pile_card_types = [card.type for card in self.pile]
        card_index = pile_card_types.index(card_type)
        card = self.pile[card_index]
        return card
