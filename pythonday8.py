def caesar(original_text,shift_number,direction):
    cipher_text = ""
    if direction == "decode":
        shift_number *= -1
    for letter in original_text:
        shifted_position = alphabets.index(letter) + shift_number
        shifted_position %= len(alphabets)
        cipher_text += alphabets[shifted_position]

    print(f"here is your {direction}d result: {cipher_text}")


game_over = False
while not game_over:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    type = input("What do you want to do encode or decode:\n").lower()
    text = input("PLease write the text:\n")
    shift = int(input("how many shifts you want?\n"))
    caesar(original_text=text,shift_number=shift,direction=type)

    if input("Are you done or if you want to type yes or no?\n").lower() == "yes":
        game_over = True
        print("Goodbye!")


