#!/usr/bin/env python
#

# import
import random
from copy import deepcopy
from card import StandardCard


class CardList:
    def __init__(self):
        self.cards = []
        self.value_dict = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self.suit_dict = ["diamonds", "hearts", "clubs", "spades"]

    def __repr__(self):
        return '[%s]' % ', '.join(map(str, self.cards))

    def shuffle(self):
        random.shuffle(self.cards)

    def fill_standard_deck(self):
        card = StandardCard()

        for i in self.suit_dict:
            for j in self.value_dict:
                card.set_suit(i, self.suit_dict)
                card.set_value(j, self.value_dict)
                self.cards.append(deepcopy(card))



if __name__ == '__main__':
    # test code
    # standard_deck = Deck()
    # standard_deck.shuffle()
    # print('[%s]' % ', '.join(map(str, standard_deck.deck)))
    print("Not to be run directly")

