import random

cricketers_and_networth = {
    "Virat Kohili": "1300",
    "M.S Dhoni": "989",
    "Sachin Tendulkar": "1390",
    "Hardik Pandya": "95",
    "Saurav Ganguly": "700",
    "Yuvraj Singh": "315",
    "Virender Sehwag": "405",
    "Dinesh Karthik": "96",
    "Jasprit Bumrah": "55",
    "Ravindra Jadeja": "123",
    "Shikar Dhawan": "120",
    "Gautham Gambhir": "250",
    "Rahul Dravid": "320",
    "VVS laxman": "160",
    "Kapil Dev": "270",
    "Mohammad Azharuddin": "44",
    "Ravi Shastri": "85",
    "Surya Kumar": "55",
    "Rohit Sharma": "214",
    "KL Rahul": "104",
    "Suresh Raina": "22"
}

# 1. Setup
cricketers_names = list(cricketers_and_networth.keys())

score = 0
# Start the game with a random first cricketer
first_cricketer_name = random.choice(cricketers_names) 

game_over = False
# 2. Start the Continuous Loop
# The game runs as long as the player keeps guessing correctly.
while not game_over:
    
    print(f"Current Score: {score}")
    
    # The first cricketer from the previous round (or the initial one)
    first_cricketer_networth = int(cricketers_and_networth[first_cricketer_name])

    # 3. Choose a UNIQUE Second Cricketer
    # We remove the first cricketer from the list to ensure a different choice
    available_cricketers = [name for name in cricketers_names if name != first_cricketer_name]
    
    if not available_cricketers:
        print("\n Congratulations! You ran out of unique cricketers and won the game! ")
        game_over = True
        
    # Choose the new second cricketer
    second_crieter_name = random.choice(available_cricketers)
    second_crieter_networth = int(cricketers_and_networth[second_crieter_name])
    
    # 4. Get User Guess
   
    print(f" A: {first_cricketer_name}\n B: {second_crieter_name}")

    try:
        user_guess = input(f"Who has the more NET WORTH in between these cricketers? Type 'A' or 'B' or Type 'S' for Same: ").upper()
    except ValueError:
        print("Invalid input. Please type 'A' or 'B' or 'Same' :")

    # 5. Determine Correct Answer
    if second_crieter_networth > first_cricketer_networth:
        correct_answer = "B"
    elif second_crieter_networth < first_cricketer_networth:
        correct_answer = "A"
    else:
        correct_answer = "S"

    # 6. Check Result
    if user_guess == correct_answer:
        # WINNING condition: Increase score and set up the next round
        score += 1
        print(f"\n Correct! {correct_answer} has a net worth.")
        
        # The key to the continuous game: The second cricketer becomes the first for the next round
        first_cricketer_name = second_crieter_name
        
    else:
        # LOSING condition: End the loop (and the game)
        print(f"\n Incorrect! {correct_answer} has a net worth.")
        print(f"\nGame Over! Your final score is **{score}**.")
        game_over = True

