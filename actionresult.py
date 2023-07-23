# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:18:05 2023

@author: olavg

action_result(action):
    Resolves actions according to:
            action = input("Please enter the next move: \
                            \nPlay a card: \
                            \n\t1. Player card \
                            \n\t2. Crystal \
                            \n\t3. Spark \
                            \n\t4. - 40. for gems (10), spells (16), and relics (10) in order seen at https://aeonsend.fandom.com/wiki/Legacy#Supply_Card_Gallery \
                            \nBuy cards from the shop \
                            \n\t41. - 77., same order. \
                            \nFocus a breach: \
                            \n\t 78 - 80\
                            \nOpen a breach: \
                            \n\t 81-83 \
                            \n84. Buy a charge\
                            \n85. Activate charge power \
                            \n86. End main phase \
                            \n")
"""
from player import Player
from deck import Deck
from hand import Hand
from playedcards import PlayedCards
from discardpile import DiscardPile

def action_result(player: Player, deck: Deck, hand: Hand, played_cards: PlayedCards, discard_pile: DiscardPile, shop, breaches, action: str):
    if action == '1':
        card = hand.get_card_from_name("Crystal")
        action_allowed = True
        if action_allowed:
            card.resolve_effect(player)
            hand.remove_card(card)
            played_cards.add_card(card)
    elif action == '2':
        card = hand.get_card_from_name("Crystal")
        action_allowed = True
        if action_allowed:
            card.resolve_effect(player)
            hand.remove_card(card)
            played_cards.add_card(card)
    elif action == '3':
        card = hand.get_card_from_name("Spark")
        action_allowed = breaches[0].prepare_spell(card)
        if action_allowed:
            hand.remove_card(card)
            breaches[0].add_card(card)
    elif action == '86': return
    else:
        return print("Action " + action + " is not a legal action. Only legal actions are integers 1 - 86.")
