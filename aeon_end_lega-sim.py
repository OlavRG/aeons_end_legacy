from breach import Breach
from card import Card
from cards import Crystal, Spark
from player import Player
from deck import Deck
from hand import Hand
from game import Game

if __name__ == '__main__':
    #This is the main executable that imports all classes to run a game

    # Input
    inputs = []
    casting = [1, 1, 0, 0]
    main_phase = []
    inputs.append(casting)
    inputs.append(main_phase)

    test_game = Game(inputs)
    print(test_game)
    print(test_game.hand.pile[0].card_type)
    test_game.breaches[0].prepare_spell(test_game.hand.draw(Crystal))
    test_game.breaches[0].prepare_spell(test_game.hand.draw(Spark))
    print(test_game)




