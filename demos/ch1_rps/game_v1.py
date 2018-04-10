import random

# num = 7
# print(type(num), num)

print('-------------------------------------')
print('         ROCK PAPER SCISSORS')
print('-------------------------------------')
print()

player_wins = 0
computer_wins = 0

while player_wins + computer_wins < 3:
    player_throw = input("Welcome player, what do you throw? [r]ock, [p]aper, [s]cissors: ")
    computer_throw = random.choice(['r', 'p', 's'])
    print(f"It's on: player: {player_throw} vs computer: {computer_throw}.")

    if player_throw == 'r':
        if computer_throw == 'r':
            print("It's a tie!")
        elif computer_throw == 's':
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    if player_throw == 's':
        if computer_throw == 'r':
            print("Computer wins")
            computer_wins += 1
        elif computer_throw == 's':
            print("It's tie")
        else:
            print("Player wins!")
            player_wins += 1
    if player_throw == 'p':
        if computer_throw == 'r':
            print("Player wins")
            player_wins += 1
        elif computer_throw == 's':
            print("Computer wins")
            computer_wins += 1
        else:
            print("It's tie")

if player_wins > computer_wins:
    print(f"Player takes it {player_wins} to {computer_wins}!")
else:
    print(f"Computer takes it {computer_wins} to {player_wins}!")









