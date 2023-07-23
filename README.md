# aeons_end_legacy
Run aeons_end_lega-sim.py. Game phases are described in game.py.

TO DO:
    - add rounds
    - fix player input for casting phase
        - and remove discard_pile from breaches so it fits in class hierarchy
    - Add other relevant cards


To structure our logic (and prevent circular imports) we structure our classes in hierarchy:

Game
    action_result
        Deck
        Hand
        DiscardPile
        PlayedCards
        Breach
            CardPile
            Cards
                Card
                Player


Explanation:
    During gameplay cards move between the following piles: 
        - Deck, Hand, DiscardPile, PlayedCards, Breach.
    Actions during gameplay also alter the player
        - energy, life, and damage dealt.
    Hence we use Game class to describe the interactions between 
    these piles. Now we separate the interactions in two parts:
        - Game class handles the default flow of every round
        - action_result function handles all interactions based on player
        choices.
    Player class is not dependent on any of the card piles, so we can let cards
    directly alter the player.