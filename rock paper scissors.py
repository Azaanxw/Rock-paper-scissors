import random
logo = '''

█▀█ █▀█ █▀▀ █▄▀   ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█   ▄▀█ █▄░█ █▀▄   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
█▀▄ █▄█ █▄▄ █░█   █   █▀▀ █▀█ █▀▀ ██▄ █▀▄   █▀█ █░▀█ █▄▀   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█   █▄█ █▀█ █░▀░█ ██▄

'''
options = ["r","p","s"]
dict_for_game = {"r":"rock",
            "p":"paper",
            "s":"scissors"}

player_input = input("Pick r for rock, p for paper or s for scissors:  ").lower()
computer_choice = options[random.randint(0,2)]
if player_input == computer_choice:
    print(f"Computer picked {dict_for_game[computer_choice]}!")
    print("Its a draw!")
elif player_input == "r" and computer_choice == "p":
    print(f"Computer picked {dict_for_game[computer_choice]}!")
    print("A computer just beat you.")
elif player_input == "p" and computer_choice == "r":
    print(f"Computer picked {dict_for_game[computer_choice]}!")
    print("You win!")
elif player_input == "s" and computer_choice == "p":
    print(f"Computer picked {dict_for_game[computer_choice]}!")
    print("You win!")
elif computer_choice == "s" and player_input == "p" :
    print(f"Computer picked {dict_for_game[computer_choice]}!")
    print("A computer just beat you.")

