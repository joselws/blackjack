from player import Player
from deck import Deck


BLACKJACK = 21


def print_player_stats(player: Player, dealer: Player) -> None:
    print(f"Dealer card is {dealer.hand[0]}")
    print(f"Your cards: {player.hand}")
    print(f"Your points: {player.total_hand_value()}\n")
    return


def print_dealer_stats(dealer: Player) -> None:
    print(f"Dealer cards: {dealer.hand}")
    print(f"Dealer points: {dealer.total_hand_value()}\n")
    return


def play_game() -> bool:
    """
    Play the blackjack game.
    Returns True if the player won, or False if the dealer won
    """
    NUMBER_OF_INITIAL_CARDS = 2

    player = Player()
    dealer = Player()
    deck = Deck()
    deck.shuffle_deck()
    for _ in range(NUMBER_OF_INITIAL_CARDS):
        player.add_card(deck.hand_card())
        dealer.add_card(deck.hand_card())

    print_player_stats(player, dealer)

    # Your plays
    while player.total_hand_value() < BLACKJACK:
        choice = input("Hit or Stand? (h/s): ")
        if choice != "h":
            break
        card = deck.hand_card()
        print(f"You got {card}")
        player.add_card(card)
        print_player_stats(player, dealer)

    if player.total_hand_value() == BLACKJACK:
        print("You got blackjack!\n")
    elif player.total_hand_value() > BLACKJACK:
        print("You lost!")
        return False
    
    # Dealer plays
    print_dealer_stats(dealer)
    while dealer.total_hand_value() < min(player.total_hand_value() + 1, BLACKJACK):
        input("dealer takes a card... (press Enter)")
        card = deck.hand_card()
        print(f"Dealer got {card}")
        dealer.add_card(card)
        print_dealer_stats(dealer)

    if dealer.total_hand_value() > BLACKJACK:
        print("Dealer lost! You Win!")
        return True
    elif dealer.total_hand_value() == BLACKJACK:
        print("Dealer got Blackjack. The Dealer won, you lost!")
        return False
    elif dealer.total_hand_value() > player.total_hand_value():
        print("The dealer got more points. Dealer won, you lost!")
        return False
    else:
        print("You got more points than the dealer. You won!")
        return True


def main():
    print("Welcome to Blackjack!")
    player_wins = 0
    dealer_wins = 0
    player_won = play_game()
    if player_won:
        player_wins += 1
    else:
        dealer_wins += 1

    while True:
        print(f"Results: Player ({player_wins}) Dealer ({dealer_wins})")
        again = input("Do you want to play again? (y/n): ")
        if again == "y":
            player_won = play_game()
            if player_won:
                player_wins += 1
            else:
                dealer_wins += 1
        else:
            break
    print("Thank you for playing!")
    return


if __name__ == "__main__":
    main()
