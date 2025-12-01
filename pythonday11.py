import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Draw."
    elif c_score == 0 and u_score != 21:
        return "Black Jack! Dealer Wins."
    elif c_score == 0 and u_score == 21:
        return "It's a Draw."
    elif u_score == 0:
        return "bLack Jack! You've Won."
    elif u_score > 21:
        return "Busted!, You loose."
    elif c_score > 21:
        return "Dealer Busted!, You Won."
    elif u_score > c_score:
        return "Hurry! You've Won."
    elif u_score < c_score:
        return "Sorry! You loose."

def play_game():
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, Current score : {user_score}")
        print(f"Dealer's first card: {computer_card[0]}")
        
        if user_score == 0 or user_score > 21:
            is_game_over = True
        else :
            user_should_deal = input("Type 'y' to get another card, type 'n' to stand: ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            elif user_should_deal == "n":
                is_game_over = True
            else:
                print("Invalid input. Please type 'y' or 'n'.")

    if user_score <= 21:
        computer_score = calculate_score(computer_card)
        print(f"Player Stands. Dealer cards: {computer_card}")
        print(f"Dealer's current score: {computer_score if computer_score != 0 else 21}")
        
        
        
        while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
        
        
    print(compare(user_score, computer_score))
    print(f"Your total cards: {user_card}, Your final score : {user_score}")
    print(f"Dealer's total cards: {computer_card}, Dealer's finalscore: {computer_score}")

    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()