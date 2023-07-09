import rock_paper_scissors

def top_menu():
    """Print top menu listing available games to play"""

    print(
"""Games List
(1) Number Guess Game
(2) Rock Paper Scissors
""")

    while True:
        user_choice = int(input("Enter Choice (1-2): "))                      
        if user_choice < 1 or user_choice > 2:              
            print("Bad Choice - pick again between 1 and 2")
        else:
            break

    if user_choice == 1:
        pass
    elif user_choice == 2:
        rock_paper_scissors.run_game()


 # Main - code to call menu
if __name__ == "__main__":
    top_menu()