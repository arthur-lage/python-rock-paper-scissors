import random

print("="*33)
print("Let's play: Rock Paper Scissors!")
print("="*33)

print("""
[0] Rock
[1] Paper
[2] Scissors
[3] Quit
""")

pc_option = random.randint(0, 3)
player_option = int(input("Choose your option: "))

if pc_option == player_option:
    print("Tie!")

elif pc_option == 0 and player_option == 1:
    print("Rock VS Paper: Paper WINS! You won.")

elif pc_option == 0 and player_option == 2:
    print("Rock VS Scissors: Rock WINS! You lost.")

elif pc_option == 1 and player_option == 0:
    print("Paper VS Rock: Paper WINS! You lost.")

elif pc_option == 1 and player_option == 2:
    print("Paper VS Scissors: Scissors WINS! You won.")
    
elif pc_option == 2 and player_option == 0:
    print("Scissors VS Rock: Rock WINS! You won.")

elif pc_option == 2 and player_option == 1:
    print("Scissors VS Paper: Scissors WINS! You lost.")

elif player_option == 3:
    exit