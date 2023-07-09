import random

# Lookup table mapping 0=Rock, 1=Paper, 2=Scissors
mapToChoice = ["Rock", "Paper", "Scissors"]


def generate_computers_choice():
    """ Create random choice for computer's go """
    rnd_ip = random.randint(0,2)
    c_choice = mapToChoice[rnd_ip]
    return c_choice


def get_players_choice():
    """ Read in players choice """
    while True:
        player_ip = int(input("(1) Rock  (2) Paper  (3) Scissors: "))
        if (player_ip < 1) or (player_ip > 3):
            print("Bad Choice - enter again")
        else:
            p_choice = mapToChoice[player_ip -1]   # note -1 as zero indexed
            break
    
    return p_choice


def determine_winner(computer_choice, player_choice):
    """Determine if computer or player won"""

    if computer_choice == player_choice:
        print(f"DRAW - both choose {computer_choice}")
    else:
        if computer_choice == "Rock" and player_choice == "Paper":
            did_player_win = True
        elif computer_choice == "Rock" and player_choice == "Scissors":
            did_player_win = False
        elif computer_choice == "Paper" and player_choice == "Rock":
            did_player_win = False
        elif computer_choice == "Paper" and player_choice == "Scissors":
            did_player_win = True
        elif computer_choice == "Scissors" and player_choice == "Rock":
            did_player_win = True
        elif computer_choice == "Scissors" and player_choice == "Paper":
            did_player_win = False
        else:
            print("ERROR - something wrong with game logic")
        
        if did_player_win == True:
            print(f"PLAYER WINS - computer={computer_choice} player={player_choice}")
        else:
            print(f"COMPUTER WINS - computer={computer_choice} player={player_choice}")


def run_game():
    """
    - Single game of rock-papers-scissors.
    - Player enters choice which is compared to randomly generated computer's choice
    """

    print("Starting Game Rock-Paper-Scissors")

    computer_choice = generate_computers_choice()
    player_choice = get_players_choice()

    determine_winner(computer_choice, player_choice)


# Main - code to call game
if __name__ == "__main__":

    while True:
        run_game()

        choice = input("Another Go (Y/N): ").upper()
        if choice != "Y":
            print("Exiting Game Rock-Paper_Scissors")
            break
