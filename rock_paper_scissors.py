import random

while True:
    # main program
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input('\033[96m' + "Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please try again.")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print('\033[94m' + f"The computer chose {computer_move}.")

    if player_move == computer_move:
        print('\033[93m' + "Draw!")
    elif (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('\033[0m' + "You win!")
    elif (player_move == scissors and computer_move == rock) or (player_move == rock and computer_move == paper) or \
            (player_move == paper and computer_move == scissors):
        print('\033[91m' + "You lose!")

    while True:
        answer = str(input('Do you wish to play again? (y/n): '))
        if answer == 'y':
            break
        elif answer == 'n':
            raise SystemExit("Goodbye")
        else:
            print("Invalid input.")
            continue
