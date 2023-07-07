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
        self.shop = []
        self.breach_1 = Breach(0, 0, 0, "1")
        self.breach_2 = Breach(4, 2, 3, "2")
        self.breach_3 = Breach(7, 3, 3, "3")
        self.breach_4 = Breach(13, 4, 4, "4")
        self.breaches = [self.breach_1, self.breach_2, self.breach_3, self.breach_4]
        self.turn = 0
        self.phase = "casting phase"

    def __str__(self):
        game_state = "Current game state:" \
        + "\n\tTurn: " + str(self.turn) \
        + "\n\tPhase: " + self.phase \
        + "\n\t" + str(self.hand) \
        + "\n\t" + str(self.deck) \
        + "\n\t" + ',\n\t'.join([str(breach) for breach in self.breaches])
        return game_state

    def casting_phase(self, inputs):
    # Casting phase
        for breach in self.breaches:
            if len(self.breach.pile) == 1:
                if self.breach.focus_stage == 0 and inputs[0][self.breaches.index(breach)]:
                    self.breach.cast(self.deck, self.player)
                if self.breach.focussed and not self.breach.focus_stage == 0:
                    self.breach.cast(self.deck, self.player)

    def main_phase(self):
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
            # end main phase: 1
            # Total: 48
        main_phase_ongoing = True
        while main_phase_ongoing:
            if action[1][0] == 0:
                a = 1  # perform action 1

            elif action[1][48]:
                main_phase_ongoing = False
            else: print()



            # Draw phase
            # Place all the gems and relics that you have played this turn on the top of your discard pile in any order you choose
            while len(self.hand) < 5:
                self.hand.add_card(self.deck.draw())
        print(self.hand)
