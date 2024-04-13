from card import Card


class Player:
    def __init__(self):
        self.hand: list[Card] = []

    def add_card(self, card: Card):
        """
        Aces go to the end of the hand, 
        while any other card to the beginning
        """
        if card.number == "A":
            self.hand.append(card)
        else:
            self.hand.insert(0, card)

    def total_hand_value(self) -> int:
        total: int = 0
        count: int = 0
        ACE_BIG_VALUE = 11
        cards_in_hand = len(self.hand)
        for card in self.hand:
            count += 1
            if card.number.isdigit():
                total += int(card.number)
            elif card.number in ["J", "Q", "K"]:
                total += 10
            else:
                # processing Aces
                cards_remaining = cards_in_hand - count
                if total < ACE_BIG_VALUE - cards_remaining:
                    total += ACE_BIG_VALUE
                else:
                    total += 1
        return total
    