import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    range_str = f"[0, {len(Action) - 1}]"
    max_Action = len(Action) - 1
    while selection > max_Action:
        selection = int(input(f"Invalid selection. Enter a value in range {range_str}: "))
    else:
        action = Action(selection)
    return action

def get_computer_selection():
    possible_actions = ["Rock", "Paper", "Scissors"]
    choices = [f"{action.name}[{action.value}]" for action in Action]
    computer_action = random.choice(possible_actions)
    for action in Action:
        if computer_action == action.name:
            selection = action.value
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors!")
            print(f"\nPlayer wins!")
        else:
            print("Paper covers rock! You lose.")
            print(f"\nComputer wins!")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock!")
            print(f"\nPlayer wins!")
        else:
            print("Scissors cuts paper! You lose.")
            print(f"\nComputer wins!")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper!")
            print(f"\nPlayer wins!")
        else:
            print("Rock smashes scissors! You lose.")
            print(f"\nComputer wins!")


def playgame():
    user_action = get_user_selection()
    computer_action = get_computer_selection()
    print(f"\nYou chose {user_action.name} : Computer chose {computer_action.name}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
        restart = input("Play again? (y/n): ")
        if restart.lower() == "y":
            playgame()
        else:
            exit()

    determine_winner(user_action, computer_action)
    exit()

playgame()

