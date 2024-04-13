from enum import StrEnum
from typing import Self


class Suit(StrEnum):
    DIAMOND = "diamond"
    CLUB = "club"
    HEART = "heart"
    SPADE = "spade"


class Card:
    def __init__(self, number: int, suit: Suit):
        self.number = self.find_number_representation(number)
        self.suit = suit

    @staticmethod
    def find_number_representation(number: int) -> str:
        if number == 1:
            return "A"
        elif number <= 10:
            return str(number)
        elif number == 11:
            return "J"
        elif number == 12:
            return "Q"
        else:   # Number = 13
            return "K"
        
    def __repr__(self) -> str:
        return f"({self.number} {self.suit})"
    
    def __eq__(self, card: Self) -> bool:
        if card.number == self.number and card.suit == self.suit:
            return True
        return False
    