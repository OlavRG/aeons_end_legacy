# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:04:54 2023

@author: olavg
"""

from breach import Breach
from card import Card
from cards import Crystal, Spark
from player import Player
from deck import Deck
from hand import Hand
from discardpile import DiscardPile
from playedcards import PlayedCards


# The Game class allows you to run through the sequence of
# a game of Aeons End Legacy with the following steps:
# - Setup
# - Rounds, subdivided in
#   - Casting phase
#   - Main phase
#   - Draw phase
# Currently no input from the player is programmed
class Game():
    # Setup
    def __init__(self, inputs):
        self.player = Player()
        self.deck = Deck()
        self.hand = Hand()
        self.played_cards = PlayedCards()
        self.discard_pile = DiscardPile()
        self.shop = []
        self.breach_1 = Breach(0, 0, 0, "1")
        self.breach_2 = Breach(4, 2, 3, "2")
        self.breach_3 = Breach(7, 3, 3, "3")
        self.breach_4 = Breach(13, 4, 4, "4")
        self.breaches = [self.breach_1, self.breach_2, self.breach_3, self.breach_4]
        self.turn = 0
        self.phase = ""

    def __str__(self):
        game_state = "Current game state:" \
        + "\n\tTurn: " + str(self.turn) \
        + "\n\tPhase: " + self.phase \
        + "\n\t" + str(self.hand) \
        + "\n\t" + str(self.deck) \
        + "\n\t" + str(self.played_cards) \
        + "\n\t" + str(self.discard_pile) \
        + "\n\t" + ',\n\t'.join([str(breach) for breach in self.breaches])
        return game_state

    def casting_phase(self, inputs):
    # Casting phase
        self.phase = "casting_phase"
        for breach in self.breaches:
            if len(breach.pile) == 1:
                if breach.focus_stage == 0 and inputs[0][self.breaches.index(breach)]:
                    breach.cast(self.discard_pile, self.player)
                if breach.focussed and not breach.focus_stage == 0:
                    breach.cast(self.discard_pile, self.player)

    def main_phase(self, inputs):
        # Main phase
        # Number of possible actions:
            # play any unique card:
                # Gems: 4, all passive
                # Neural wreath: 3, one for each breach to focus
                # Geophage: 5, one for each unique gem + one for none
                # Spells: 20, 5 spells over 4 breaches
            # gain a card: 9 shop
            # focus a breach: 3 breaches
            # open a breach: 3 breaches
            # buy a charge
            # activate charge power
            # end main phase: 1
            # Total: 48
        self.phase = "main phase"
        while len(self.hand):
            types_in_hand = [card.type for card in self.hand.pile]
            if "gem" in types_in_hand:
                self.hand.play(self.hand.get_card_from_type("gem"), self.played_cards)
            else:
                break
            # breach_focusses = [breach.focussed for breach in self.breaches]
            # breach_focus_stages = [breach.focus_stage for breach in self.breaches]
            # breaches_available = breach_focusses or (breach_focus_stages == 0)
            # if "spell" in types_in_hand and ():
            # self.hand.play()

    def draw_phase(self, inputs):
        # Draw phase
        # Place all the gems and relics that you have played this turn \
        # on the top of your discard pile in a order you choose.
        # Draw until you have 5 cards in hand
        self.phase = "draw phase"
        self.played_cards.pile.sort(key=lambda x: x.cost, reverse=True)
        self.discard_pile.add_cards(self.played_cards.pile)
        self.played_cards.pile.clear()
        while len(self.hand) < 5:
            if not len(self.deck):
                self.deck.add_card(self.played_cards)
            self.hand.add_card(self.deck.draw())