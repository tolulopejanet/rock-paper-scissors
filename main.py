import random

while True:
    users_choice = input("Enter a choice (R, P, S): ")
    default_choices = ["R", "P", "S"]
    computer_choice = random.choice(default_choices)
    print(f"\nPlayer ({users_choice}): CPU ({computer_choice}).\n")

    if users_choice == computer_choice:
        print(f"Both players selected {users_choice}. It's a tie!")
    elif users_choice == "R":
        if computer_choice == "S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers R! You lose.")
    elif users_choice == "P":
        if computer_choice == "R":
            print("Paper covers R! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif users_choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break