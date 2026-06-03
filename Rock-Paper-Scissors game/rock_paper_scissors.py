import random
print()
print("Welcome to Rock-Paper-Scissors Game!")
options = ("rock", "paper", "scissors")
score = {"Player": 0, "Computer": 0}

while True:
    computer = random.choice(options)
    player = input("Enter (rock, paper, scissors) or (q) to quit: ").lower()

    if player == "q":
        print("Thanks for playing!")
        break
    elif player not in options:
        print("Invalid input, please try again.")
        continue
    else:
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            score["Player"] += 1
        else:
            print("You lose!")
            score["Computer"] += 1

print(f"Score - Player: {score['Player']}, Computer: {score['Computer']}")