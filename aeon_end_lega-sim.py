from breach import Breach
from card import Card
from cards import Crystal, Spark
from player import Player
from deck import Deck
from hand import Hand


if __name__ == '__main__':

    # Input
    inputs = []
    casting = [1, 1, 0, 0]
    main_phase = []
    inputs.append(casting)
    inputs.append(main_phase)

class Game():
    # Setup
    def __init__(self,inputs):
        self.player = Player()
        self.deck = Deck()
        self.hand = Hand()
        self.shop = []
        self.breach_1 = Breach(0, 0, 0, "1")
        self.breach_2 = Breach(4, 2, 3, "2")
        self.breach_3 = Breach(7, 3, 3, "3")
        self.breach_4 = Breach(13, 4, 4, "4")
        self.breaches = [self.breach_1, self.breach_2, self.breach_3, self.breach_4]

    print(hand)
    print(deck)

    # Test code
    player.energy = 5
    breach_2.focus(player)
    breach_2.open_breach(player)
    breach_2.prepare_spell(hand.draw())

    # Turn 1
    # Casting phase
    # number of possible actions: 
        # cast or not for each breach: 2**4 = 16
        # more in case of gravity node
        # end casting phase: 1
    for breach in breaches:
        if len(breach.pile) == 1:
            if breach.focus_stage == 0 and inputs[0][breaches.index(breach)]:
                breach.cast(deck, player)
            if breach.focussed and not breach.focus_stage == 0:
                breach.cast(deck, player)

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
        if inputs[1][0] == 0:
            a = 1  # perform action 1
        
        elif inputs[1][1]: 
            main_phase_ongoing = False


    # Draw phase
    # Place all the gems and relics that you have played this turn on the top of your discard pile in any order you choose
    while len(hand) < 5:
        hand.add_card(deck.draw())
    print(hand)
