from classfile import User

print("Welcome to the movie guessing game!")

hero = input("Choose the actor ('ranveer singh' or 'ranbir kapoor'): ")

if hero == "ranveer singh":
    heroine = input("Choose the actress ('alia bhat' or 'anushka sharma'): ")

    if heroine == "alia bhat":
        director = input("Choose the director ('karan johar' or 'zoya akhtar'): ")
    else:
        director = input("Choose the director ('aditya chopra' or 'zoya akhtar'): ")

elif hero == "ranbir kapoor":
    heroine = input("Choose the actress ('deepika padukone' or 'anushka sharma'): ")

    if heroine == "deepika padukone":
        director = input("Choose the director ('ayan mukerji' or 'imtiaz ali'): ")
    else:
        director = input("Choose the director ('anurag kashyap' or 'karan johar'): ")

my_movie = User(hero, heroine, director)

my_movie.moviecast()
