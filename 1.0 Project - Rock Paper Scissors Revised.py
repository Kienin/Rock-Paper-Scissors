import random


# INPUT - get name and rounds user wants to play for
name = str(input("Hi there! What is your name? ")).capitalize()
print(f"Hello {name}! Let's play Rock, Paper, Scissors!\n")


# rounds need to be an odd number, so it'll  be best of N rounds
while True:
      try:
        best_of = int(input("How many rounds do you want to play? (Please enter an odd number): "))
        if best_of % 2 != 0:
            break
        else:
            print("Invalid! Please enter an odd number")
      except ValueError:
          print("Invalid! Please enter an odd number")

choices = ["r", "p", "s", "rock", "paper", "scissors"]
player_score = 0
computer_score = 0

winning_score = (best_of + 1)//2

print(f"\nThis game is best of {best_of}. Good luck {name}!\n")

'''
we add 1 to the winning score then dividing it by 2:
for example: 
    if player wants to play 5 rounds, and they win 3 rounds; they win
    5 + 1 = 6  ->  6 / 2 = 3
    if player wins 3 rounds, they win. They don't have to play till 5 rounds
'''

while player_score < winning_score and computer_score < winning_score:
    print('________________________________________')
    print(f"{name} score: {player_score} - Computer score: {computer_score}\n")

# Get player and computer choice
    player_choice = input("Pick [R]ock, [P]aper, or [S]cissors: ").lower()
    if player_choice not in choices:
        print("Invalid! Please enter [R]ock, [P]aper, or [S]cissors")
        continue
    computer_choice = random.choice(choices)

# reassign choices into more readable choice:
    if player_choice == "r":
        player_choice = "Rock"
    elif player_choice == "p":
        player_choice = "Paper"
    elif player_choice == "s":
        player_choice = "Scissors"

    if computer_choice == "r":
        computer_choice = "Rock"
    elif computer_choice == "p":
        computer_choice = "Paper"
    elif computer_choice == "s":
        computer_choice = "Scissors"

    if player_choice == "rock":
        player_choice = "Rock"
    elif player_choice == "paper":
        player_choice = "Paper"
    elif player_choice == "scissors":
        player_choice = "Scissors"

    if computer_choice == "rock":
        computer_choice = "Rock"
    elif computer_choice == "paper":
        computer_choice = "Paper"
    elif computer_choice == "scissors":
        computer_choice = "Scissors"
# PROCESS - determine who wins the round
    print(f"\nYou chose {player_choice} : The Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        print(f"{name} Wins!")
        player_score += 1
    else:
        computer_score += 1
        print("Computer Wins!")


print('________________________________________')
print(f"FINAL SCORE - {name}: {player_score} | Computer: {computer_score}")
if player_score > computer_score:
    print("Congratulations! You won!!!")
else:
    print("Better luck next time! Computer Won!!!")


