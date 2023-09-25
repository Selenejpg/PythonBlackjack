############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## This is the the version where i fixed recursion, repetition and logic flaws 
import random
import art
from art import logo

cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

def draw_card():
    return random.choice(cards)

def sum_cards(cards):
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def blackjack():
    player_cards.clear()
    dealer_cards.clear()

    player_cards.extend(random.sample(cards, 2))
    dealer_cards.extend(random.sample(cards, 2))

    print(logo)
    print("Welcome to Python Blackjack!")

    while True:
        player_score = sum_cards(player_cards)
        dealer_score = sum_cards(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or player_score > 21:
            break

        choice = input("Do you want to draw a new card? Type 'y' for yes or 'n' for no: ")
        if choice == 'y':
            player_cards.append(draw_card())
        else:
            break

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_card())
        dealer_score = sum_cards(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "Blackjack! You win!"
    elif dealer_score == 21:
        return "Dealer got blackjack. You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

result = blackjack()
print(result)
