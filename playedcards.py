from cardpile import CardPile

class PlayedCards(CardPile):
    def __init__(self):
        self.pile =[]

    def __str__(self):
        return 'Cards played: ' + ', '.join([str(card) for card in self.pile])
