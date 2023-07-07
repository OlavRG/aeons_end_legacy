# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:21:22 2023

@author: olavg
"""
from cardpile import CardPile
from player import Player
from card import Card
from hand import Hand
from discardpile import DiscardPile

class Breach(CardPile):
    def __init__(self, cost_to_open: int, cost_to_focus: int, focus_stage: int, breach_number: str):
        self.cost_to_open = cost_to_open
        self.cost_to_focus = cost_to_focus
        self.focus_stage = focus_stage
        self.focussed = False
        self.pile = []
        self.breach_number = breach_number

    def __str__(self):
        full_state = "Breach: " + str(self.breach_number) \
        + "\n\t\tPrepared spell: " + str(self.pile) \
        + "\n\t\tFocus stage: " + str(self.focus_stage)
        return full_state

    def focus(self, player: Player, cost_free=False):
        if self.focus_stage == 0:
            return print("Breach " + self.breach_number + ": already open, cannot be focussed")
        elif cost_free == True:
            self.focussed = True
            self.focus_stage -= 1
        elif self.cost_to_focus > player.energy:
            return print("Breach " + self.breach_number + ": cannot afford to focus breach")
        else:
            player.energy -= self.cost_to_focus
            self.focussed = True
            self.focus_stage -= 1
            self.cost_to_open -= (self.cost_to_focus - 1)

    def open_breach(self, player: Player):
        if self.focus_stage == 0:
            return print("Breach " + self.breach_number + ": already open, cannot be opened")
        elif self.cost_to_open > player.energy:
            return print("Breach " + self.breach_number + ": cannot afford to open")
        else:
            player.energy -= self.cost_to_open
            self.focus_stage = 0

    def prepare_spell(self, hand: Hand, card: Card):
        if not card.type == "spell":
            return print(f"Failed to prepare {card}: it is not a spell")
        if not self.focussed and not self.focus_stage == 0:
            return print("Breach " + self.breach_number + f": is not focussed nor open. Focus stage = {self.focus_stage}.")
        elif len(self.pile) > 1:
            raise Exception("Breach " + self.breach_number + ": illegal play, multiple spells prepared on the same breach.")
        elif self.pile:
            return print("Breach " + self.breach_number + f": cannot prepare {card.name}. Breach is already occupied by {self.pile[0].name}")
        else:
            self.add_card(card)
            hand.remove_card(card)
            print("Prepared " + card.name + " to breach " + self.breach_number)

    def cast(self, discard_pile: DiscardPile, player: Player):
        spell_card = self.draw()
        spell_card.play(player)
        discard_pile.add_card(spell_card)
        if self.breach_number == 4: player.damage_dealt += 1
        
        