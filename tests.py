from card import Card, Suit
from deck import Deck
from player import Player

import unittest


class TestPlayer(unittest.TestCase):

    def test_add_card(self):
        player = Player()
        cards = [
            Card(3, Suit.CLUB),
            Card(4, Suit.CLUB),
            Card(1, Suit.CLUB),
            Card(13, Suit.CLUB),
            Card(6, Suit.CLUB),
            Card(1, Suit.CLUB),
            Card(12, Suit.CLUB),
        ]
        for card in cards:
            player.add_card(card)
        self.assertEqual(player.hand[0].number, "Q")
        self.assertEqual(player.hand[1].number, "6")
        self.assertEqual(player.hand[2].number, "K")
        self.assertEqual(player.hand[3].number, "4")
        self.assertEqual(player.hand[4].number, "3")
        self.assertEqual(player.hand[5].number, "A")
        self.assertEqual(player.hand[6].number, "A")

    def test_total_hand_1(self):
        player = Player()
        cards = [
            Card(1, Suit.CLUB),
            Card(13, Suit.CLUB)
        ]
        for card in cards:
            player.add_card(card)
        self.assertEqual(player.total_hand_value(), 21)

    def test_total_hand_2(self):
        player = Player()
        cards = [
            Card(1, Suit.CLUB),
            Card(1, Suit.CLUB),
            Card(13, Suit.CLUB),
        ]
        for card in cards:
            player.add_card(card)
        self.assertEqual(player.total_hand_value(), 12)

    def test_total_hand_3(self):
        player = Player()
        cards = [
            Card(1, Suit.CLUB),
            Card(1, Suit.CLUB),
            Card(9, Suit.CLUB),
        ]
        for card in cards:
            player.add_card(card)
        self.assertEqual(player.total_hand_value(), 21)

    def test_total_hand_4(self):
        player = Player()
        cards = [
            Card(2, Suit.CLUB),
            Card(7, Suit.CLUB),
            Card(12, Suit.CLUB),
            Card(1, Suit.CLUB),
            Card(1, Suit.CLUB),
        ]
        for card in cards:
            player.add_card(card)
        self.assertEqual(player.total_hand_value(), 21)


class TestDeck(unittest.TestCase):

    def test_deck_size(self):
        deck = Deck()
        deck.shuffle_deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_hand_card(self):
        deck = Deck()
        card = deck.hand_card()
        self.assertEqual(len(deck.cards), 51)
        self.assertEqual(card, Card(13, Suit.SPADE))

    def test_deck_integrity(self):
        deck = Deck()
        card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for card_value in card_values:
            matching_cards = []
            for card in deck.cards:
                if card.number == card_value:
                    matching_cards.append(card)
            self.assertEqual(len(matching_cards), 4)
        for suit in Suit:
            matching_cards = []
            for card in deck.cards:
                if card.suit == suit:
                    matching_cards.append(card)
            self.assertEqual(len(matching_cards), 13)

if __name__ == "__main__":
    unittest.main()
