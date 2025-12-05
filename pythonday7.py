import random
words_list = [
    "algorithm", "adventure", "bicycle", "blizzard", "captain",
    "cascade", "digital", "dinosaur", "ecology", "elephant",
    "fantasy", "flamingos", "galaxy", "giraffe", "hurricane",
    "internet", "journey", "jungle", "kangaroo", "keyboard",
    "labyrinth", "lantern", "magnet", "mountain", "mystery",
    "navigate", "ocean", "octopus", "paradise", "penguin",
    "quarantine", "quantum", "rainbow", "robotics", "satellite",
    "science", "scorpion", "shadow", "spaceship", "spectrum",
    "thunder", "treasure", "umbrella", "universe", "viking",
    "volcano", "walrus", "whisper", "xylophone", "zeppelin"
]

lives = 6

word = (random.choice(words_list))
word_length = len(word)



place_holder = ""
for postion in range(word_length):
    place_holder += "_"

print(place_holder)

game_over = False
correct_words = []

while not game_over:
    guess = (input("Guess the Letter?").lower())
    display = ""
    for letter in word:
        if guess == letter:
          display += letter
          correct_words.append(guess)
        elif letter in correct_words:
           display += letter
        else:
          display += "_"
    print(display)

    if guess not in word:
      lives -= 1
      print(f"you have guessed the wrong letter and the remaing lives you have are {lives}")
      if lives == 0:
        game_over = True
        print("You lost!")

    if "_" not in display:
       game_over = True
       print("You win!")