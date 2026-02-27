import random

print("=== RPS Game ===")

# taking input
choice = input("Enter your move (rock/paper/scissors): ")
choice = choice.lower()

# computer move
computer = random.choice(["rock", "paper", "scissors"])

if choice == "rock" or choice == "paper" or choice == "scissors":

    print("Computer move is:", computer)

    if choice == computer:
        print("Draw game")

    else:
        if choice == "rock":
            if computer == "paper":
                print("Computer wins")
            else:
                print("You win")

        elif choice == "paper":
            if computer == "scissors":
                print("Computer wins")
            else:
                print("You win")

        elif choice == "scissors":
            if computer == "rock":
                print("Computer wins")
            else:
                print("You win")

else:
    print("Invalid choice entered")

print("Game finished")