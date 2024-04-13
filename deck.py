import random
from card import Card, Suit


NUMBER_OF_CARD_VALUES = 13


class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        for suit in Suit:
            for card_value in range(1, NUMBER_OF_CARD_VALUES + 1):
                self.cards.append(Card(card_value, suit))
    
    def shuffle_deck(self) -> None:
        random.shuffle(self.cards)

    def hand_card(self) -> Card:
        return self.cards.pop()
    