import random
from constants import SUITS, RANKS, VALUES


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        return VALUES[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            self.__init__()
        return self.cards.pop()

    def cards_remaining(self):
        return len(self.cards)