import random

print("Are you ready to play?")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Choose Rock/Paper/Scissor or X to exit:").lower()
    if user_input == "x":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

    if user_wins == 2:
        break

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times. ")
print("Goodbye!")



