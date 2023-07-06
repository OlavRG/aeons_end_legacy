# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:21:22 2023

@author: olavg
"""
from cardpile import CardPile
from player import Player

class Breach(CardPile):
    def __init__(self, cost_to_open: int, cost_to_focus: int, focus_stage: int, breach_number: str):
        self.cost_to_open = cost_to_open
        self.cost_to_focus = cost_to_focus
        self.focus_stage = focus_stage
        self.focussed = False
        self.pile = []
        self.breach_number = breach_number
        
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

    def prepare_spell(self, card):
        if not card.card_type == "spell":
            return print(f"Failed to prepare {card}: it is not a spell")
        if not self.focussed and not self.focus_stage == 0:
            return print("Breach " + self.breach_number + f": is not focussed nor open. Focus stage = {self.focus_stage}.")
        elif len(self.pile) > 1:
            raise Exception("Breach " + self.breach_number + ": illegal play, multiple spells prepared on the same breach.")
        elif self.pile:
            return print("Breach " + self.breach_number + f": cannot prepare {card.name}. Breach is already occupied by {self.pile[0].name}")
        else:
            self.add_card(card)
        
    def cast(self, deck, player: Player):
        spell_card = self.draw()
        deck.add_card(spell_card)
        spell_card.play(player)
        if self.breach_number == 4: player.damage_dealt += 1
        
        