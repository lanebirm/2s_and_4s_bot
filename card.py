#!/usr/bin/env python
#

# imports
import random


class StandardCard:
    def __init__(self):
        self.value = None
        self.suit = None

    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)

    def set_value(self, value, value_dict):
        if value in value_dict:
            self.value = value
        else:
            print(value + ' is not a valid card value. Must be one of the following: '
                  + '[%s]' % ', '.join(map(str, value_dict)))

    def set_suit(self, suit, suit_dict):
        if suit in suit_dict:
            self.suit = suit
        else:
            print(suit + ' is not a valid card suit. Must be one of the following: '
                  + '[%s]' % ', '.join(map(str, suit_dict)))


if __name__ == '__main__':
    print("This script is not meant to be run directly")

