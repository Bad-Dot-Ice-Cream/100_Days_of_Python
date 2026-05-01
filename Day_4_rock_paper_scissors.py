import random

options = ["rock", "paper", "scissors"]

userChoice = int(input("What do you choose?\nType '0' for Rock, '1' for Paper, '2' for Scissors\n>  "))
# 0, 1, 2

computerChoice = random.randint(0, 2)
print(f"Computer chose {computerChoice}")

if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number. You lose!\n\n\n")
    print("\033[31mHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHA NOOB NOTHING BUT A NOOB!\033[0m")
elif userChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and userChoice == 2:
    print("You lose!")
elif computerChoice > userChoice:
    print("You lose!")
elif userChoice > computerChoice:
    print("You win!")
elif computerChoice == userChoice:
    print("It's a draw!")
