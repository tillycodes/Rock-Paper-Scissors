import random

print("Welcome to Rock, Paper, Scissors!")

rps = ["rock", "paper", "scissors"]
random_move = random.choice(rps)
print(random_move)

while True:
    attempt = input("Enter your attempt: ")
    if (attempt == random_move):
        print("We have a tie!")
        continue
    elif (attempt == "rock"):
        if (random_move == "scissors"):
            print("You smashed the computer's scissors with a rock!")
            break
        elif(random_move == "paper"):
            print("The computer wrapped your rock up in paper!")
            break
    elif (attempt == "paper"):
        if (random_move == "scissors"):
            print("The computer cut your paper in half with its scissors!")
            break
        elif (random_move == "rock"):
            print("You wrapped the computer's rock up in paper!")
            break
    elif(attempt == "scissors"):
        if (random_move == "paper"):
            print("You cut the computer's paper in half with your scissors!")
            break
        elif (random_move == "rock"):
            print("The computer smashed your scissors with its rock!")
            break