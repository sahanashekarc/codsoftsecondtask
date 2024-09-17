import random

choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (yes/no): ").lower() != 'yes':
        break