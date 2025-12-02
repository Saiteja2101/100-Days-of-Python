import random

def get_difficulty():
    while True:
        G = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if G == "easy":
            return 10
        elif G == "hard":
            return 5
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def game_simplified():
    print("Welcome to the Number Guessing Game!")

    random_number = random.randint(1, 100) 
    
    
    lives = get_difficulty()
    
    
    
    while lives > 0:
        print(f"\nYou have {lives} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        if guess == random_number:
            print(f"🥳 Hurray! You won. The answer was {random_number}.")
            return # Exit the function/game immediately upon winning
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
            
        lives -= 1
        
        if lives == 0:
            print("\nYou've run out of guesses, you lose. 😥")
            print(f"The number was {random_number}.")
        else:
            print("Guess again.")


game_simplified()