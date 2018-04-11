import random


def main():
    print_header()
    play_game()


def print_header():
    print('-------------------------------------')
    print('         ROCK PAPER SCISSORS')
    print('-------------------------------------')
    print()


def choose_winner(throw1, throw2):
    if throw1 == 'r':
        if throw2 == 'r':
            return 0
        elif throw2 == 's':
            return 1
        else:
            return 2
    if throw1 == 's':
        if throw2 == 'r':
            return 2
        elif throw2 == 's':
            return 0
        else:
            return 1
    if throw1 == 'p':
        if throw2 == 'r':
            return 1
        elif throw2 == 's':
            return 2
        else:
            return 0

    return -1


def get_throws():
    player_throw = input("Welcome player, what do you throw? [r]ock, [p]aper, [s]cissors: ")
    computer_throw = random.choice(['r', 'p', 's'])

    return player_throw, computer_throw


def play_game():
    result = RoundResult(0, 0)

    while result.player_wins + result.computer_wins < 3:
        player_throw, computer_throw = get_throws()
        print(f"It's on: player: {player_throw} vs computer: {computer_throw}.")

        outcome = choose_winner(player_throw, computer_throw)
        result = show_winner(result.computer_wins, outcome, result.player_wins)

    display_winner(result.computer_wins, result.player_wins)


def show_winner(computer_wins, outcome, player_wins):
    if outcome == 0:
        print("Tie!")
    elif outcome == 1:
        print("Player wins!")
        player_wins += 1
    elif outcome == 2:
        print("Computer wins!")
        computer_wins += 1
    return RoundResult(computer_wins, player_wins)


import collections

RoundResult = collections.namedtuple("RoundResult", "computer_wins player_wins")


def display_winner(computer_wins, player_wins):
    if player_wins > computer_wins:
        print(f"Player takes it {player_wins} to {computer_wins}!")
    else:
        print(f"Computer takes it {computer_wins} to {player_wins}!")


main()
