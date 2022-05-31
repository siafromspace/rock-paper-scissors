import random

user = input("Enter name: ")
possible_choices = ["R", "P", "S"]
print(f"Hello {user}, welcome to the Rock, Paper, Scissors game. The options include 'R', 'P' and 'S' where 'R' represents 'rock', 'P' represents 'paper' and 'S' represents 'scissors'.")
comp_choice = random.choice(possible_choices)


def user_input():
    user_choice = input("Enter choice: ").upper().strip()
    if user_choice not in possible_choices:
        print("Error, wrong input. Try again.")
        user_input()
    else:
        check_win(user_choice, comp_choice)


def check_win(user_choice, comp_choice):
    print(f"{user} ({user_choice}) : Computer ({comp_choice})")
    if user_choice == comp_choice:
        print(f"Both players selected {user_choice}. It is a tie.")
    elif user_choice == "R":
        if comp_choice == "S":
            print("Rock smashes Scissors. You win!")
        elif comp_choice == "P":
            print("Paper covers Rock. You lose!")
    elif user_choice == "S":
        if comp_choice == "R":
            print("Rock smashes Scissors. You lose!")
        elif comp_choice == "P":
            print("Scissors cuts Paper. You win!")
    elif user_choice == "P":
        if comp_choice == "S":
            print("Scissors cuts Paper. You lose!")
        elif comp_choice == "R":
            print("Paper covers Rock. You win!")


while True:
    user_input()
    play_again = input('Do you want to play again? y/n: ')
    play_again = play_again.lower().strip()
    if play_again == 'n':
        print("Game ended.")
        break
