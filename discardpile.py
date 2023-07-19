from cardpile import CardPile

class DiscardPile(CardPile):
    def __init__(self):
        self.pile =[]

    def __str__(self):
        return 'Cards in discard pile: ' + ', '.join([str(card) for card in self.pile])
