import random

def play():
    user = input(f"What is your choice?\n 'r' for Rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'its a tie!'.upper()
    if is_win(user, computer):
        return 'You Won!'
    return "You Lost!"


def is_win(player, opponent):
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())