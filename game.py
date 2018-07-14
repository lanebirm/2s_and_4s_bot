#!/usr/bin/env python
#

# imports
import random
# from card import StandardCard
from card_list import CardList


def new_game():
    # reset all lists
    players_hand.cards.clear()
    bots_hand.cards.clear()
    deck.cards.clear()
    play_pile.cards.clear()

    deck.fill_standard_deck()
    deck.shuffle()

    draw_cards(players_hand, hand_size)
    draw_cards(bots_hand, hand_size)


def draw_cards(card_list, num_of_cards):
    # draws num_of_cards from the top of the deck to the input card_list
    for i in range(num_of_cards):
        card_list.cards.append(deck.cards.pop(0))


def display_current():
    print(players_hand)
    print(bots_hand)
    print(deck.cards)


if __name__ == '__main__':
    # script for playing 2s and 4s 1v1 vs a bot

    # Hardcoded default variables for the game
    hand_size = 5

    # init stuff
    players_hand = CardList()
    bots_hand = CardList()
    deck = CardList()
    play_pile = CardList()
    new_game()

