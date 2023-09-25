############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## This is the the version where i wrote the main logic!
# Main flaws: 
"""
Missing Initialization of new_score: 
In the original code, new_score was not initialized before being used. 
This would have caused errors during the game execution.

Recursive Call Issues: 
In the original code, the blackjack and compare_to_dealer functions contained 
recursive calls that were not handled properly. This would have led to unexpected behavior 
and potentially a high number of recursive calls.

Undeclared Variables: Some variables, like new_card and new_score, were used without being declared 
or initialized correctly, leading to undefined variable errors.

Confusing Ace Handling Logic: The logic for handling Aces (counting as 1 or 11) was confusing and not 
well-handled. User input was not taken into account appropriately.

Missing Main Game Structure: The original code lacked a main game structure that would have handled 
the game flow more orderly.

Inefficiency and Complexity: The original code contained unnecessary duplication and complexity, 
making it difficult to follow the flow and spot errors.
"""

import random
import art
from art import logo

cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = {}
dealer_cards = {}

player_choice = random.sample(cards, 2)
dealer_choice = random.sample(cards, 2)

def draw_card():
    new_card = random.sample(cards)

def sum_cards(n1, n2):
    return n1 + n2  

player_cards['cards'] = player_choice
player_card1 = int(player_cards["cards"][0])
player_card2 = int(player_cards["cards"][1])

dealer_cards['cards'] = dealer_choice
dealer_card1 = int(dealer_cards["cards"][0]) 
dealer_card2 = int(dealer_cards["cards"][1])

score_player = sum_cards(player_card1, player_card2)
score_dealer = sum_cards(dealer_card1, dealer_card2)

def compare_to_dealer():
    if score_dealer > 21:
        print(f"It's a bust! The score of the dealer is {score_dealer}")
    elif score_dealer == 21:
        print(f"Blackjack! The dealer scored exactly {21}")
    elif score_dealer < 21:
        while new_score < 21:
            new_card_input = input("Do you want to draw a new card? Type 'y' if you want to draw one or 'n' if you want to stay: ")
            if new_card_input == "y":
                new_score = 0
                new_card = draw_card()
                new_score += new_card  
                compare_to_dealer()
            else:
                return new_score
    elif score_dealer < 13:
        new_score = 0
        new_card = draw_card()
        new_score += new_card  
        compare_to_dealer()
        
    if dealer_card1 == 11 or dealer_card2 == 11 or new_card == 11:
        res = int(input("You got an Ace! Do you want your Ace to count as '11' or as '1'?: "))
        if res == 11:
            if dealer_card1 == 11:
                dealer_card1 = 11  
            if dealer_card2 == 11:
                dealer_card2 = 11  
            if new_card == 11:
                new_card = 11
            compare_to_dealer()      
        elif res == 1:
            if dealer_card1 == 11:
                dealer_card1 = 1   
            if dealer_card2 == 11:
                dealer_card2 = 1   
            if new_card == 11:
                new_card = 1    
            compare_to_dealer()

def blackjack():
    if score_player > 21:
        print(f"It's a bust! Your score is now {score_player}")
    elif score_player == 21:
        print(f"Blackjack! You scored exactly {21}")
    elif score_player < 21:
        while new_score < 21:
            new_card_input = input("Do you want to draw a new card? Type 'y' if you want to draw one or 'n' if you want to stay: ")
            if new_card_input == "y":
                new_score = 0
                new_card = draw_card()
                new_score += new_card  
                blackjack()
            else:
                return new_score
    elif score_player < 13:
        new_score = 0
        new_card = draw_card()
        new_score += new_card  
        blackjack()
        
    if dealer_card1 == 11 or player_card2 == 11 or new_card == 11:
        res = int(input("You got an Ace! Do you want your Ace to count as '11' or as '1'?: "))
        if res == 11:
            if player_card1 == 11:
                player_card1 = 11  
            if player_card2 == 11:
                player_card2 = 11  
            if new_card == 11:
                new_card = 11
            blackjack()      
        elif res == 1:
            if player_card1 == 11:
                player_card1 = 1   
            if player_card2 == 11:
                player_card2 = 1   
            if new_card == 11:
                new_card = 1    
            blackjack()
    

print(logo)
print("Welcome to PythonBlackjack!")
print(f"I shuffled the deck. These are your cards {player_card1} and {player_card2}")
print(f"The dealer has a score of {score_dealer}")
player = blackjack()
dealer = compare_to_dealer()

if player > dealer:
    print("You win!")
else:
    print("You lose.")