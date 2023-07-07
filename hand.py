# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:45:39 2023

@author: olavg
"""
from card import Card
from cards import Crystal, Spark
from cardpile import CardPile
from playedcards import PlayedCards

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

    def play(self, card: Card, played_cards: PlayedCards):
        self.remove_card(card)
        card.play
        played_cards.add_card(card)