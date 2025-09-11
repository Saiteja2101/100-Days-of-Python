#Names = ["Sai","Saketh","Surya"]
#for name in Names:
#    print(name)

#for number in range(1, 101):  # from 1 to 100 inclusive
#    if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)

import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



print("Welcome to the password generator")
number_of_letters = int(input("How many letters do you want in your password"))
number_of_symbols = int(input("How many symbols do you want in your password"))
number_of_numbers = int(input("How many numbers do you want in your password"))

password = []

for char in range(1,number_of_letters + 1):
    password.append(random.choice(Letters)) # password = password + random.choise(letters)

for char in range(1,number_of_symbols + 1):
    password.append(random.choice(Symbols)) # password = password + random.choise(symbols)

for char in range(1,number_of_numbers + 1):
    password.append(random.choice(Numbers)) # password = password + random.choise(numbers)

print(password)
random.shuffle(password)
print(password)