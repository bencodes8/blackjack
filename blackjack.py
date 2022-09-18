from locale import windows_locale
import random

win = 21

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def blackjack():
    # tracks cards for each player in a list
    your_cards = []
    dealer_cards = []

    def you_hit():
        your_cards.append(deal_card())
    
    def dealer_hit():
        dealer_cards.append(deal_card())
    
    def winner():
        print(f"    Your final hand: {your_cards}, final score: {your_score}")
        print(f"    Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    # dealing first two cards
    for i in range(2):
        you_hit()
        dealer_hit()
    your_score = sum(your_cards)
    dealer_score = sum(dealer_cards)
    while dealer_score < 17:
        dealer_hit()
        dealer_score = sum(dealer_cards)
    if dealer_score == win:
        winner()
        return print("Blackjack! Dealer wins!")
    elif your_score == win:
        winner()
        return print("Lucky Blackjack! You win!")
        

    # bool for on-going game
    game_continue = True

    while game_continue:
        print(f"    Your cards: {your_cards}, current score: {your_score}")
        print(f"    Dealer's first card: {dealer_cards[0]}")

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            you_hit()
            your_score = sum(your_cards)
            if your_score > win and 11 in your_cards:
                your_cards.pop(11)
                your_cards.append(1)
                your_score = sum(your_cards)
            if your_score == win:
                winner()
                return print("You hit Blackjack! You win!")
            elif your_score > win:
                winner()
                return print("You went over. You lose!")
        else:
            winner()
            if your_score > dealer_score and your_score < win:
                print("You win! Your score is greater than Dealers!")
            elif your_score < dealer_score and dealer_score < win:
                print("You lose! Dealer's score is higher than yours")
            elif dealer_score > win:
                print("Dealer went over. You win!")
            else:
                print("Draw!")
            game_continue = False

    # recursive call to play another game of blackjack
    if input("Do you want to play another game of blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()

# start game of blackjack
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()
else:
    exit

