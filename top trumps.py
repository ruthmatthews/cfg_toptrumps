import random
import csv
import pandas as pd

#Choose n rounds in the game
#Programme will loop n times
print("\nWelcome to Harry Potter Top Trumps!\n")
rounds = input("How many rounds would you like to play? ")
print("\n")
x = 1

#set starting scores to zero
player_wins = 0
computer_wins = 0

#loop programme to repeat n times
while x <= int(rounds):
    print("Round ", x)
    input("Press any key to draw!")

    df = pd.read_csv ('toptrumpsdata.csv', usecols= ['Individual','Magic', 'Cunning', 'Courage', 'Wisdom', 'Temper'])

    #choose a random character
    #print character and details
    hp_number = random.randint(0, 29)
    player_card = df.iloc[hp_number, 1:6]
    print("\nYou have chosen:", df.iat[hp_number,0], "\n")
    print(player_card.to_string(), "\n")

    #choose a category and check user input
    category = input("Pick a category! \nMagic, cunning, courage, wisdom or temper?\n").capitalize()
    category_list = list(df.columns)
    while category not in category_list:
        category = input("Please choose from magic, cunning, courage, wisdom or temper.\n").capitalize()

    #save player score in category as variable
    player_score = df[category][hp_number]

    #choose a random character for the computer
    computer_number = random.randint(0, 29)
    while computer_number == hp_number:
        computer_number = random.randint(0,29)
    computer_card = df.iloc[computer_number, 1:6]

    #save computer score in category as variable 
    computer_score = df[category][computer_number]

    #print computer character and details
    print("\nThe computer has chosen:", df.iat[computer_number, 0], "\nTheir ", category, " score is ", computer_score)

    #compare scores and print who wins round
    if player_score < computer_score:
        print("Computer wins!\n")
        computer_wins = computer_wins + 1
    if computer_score < player_score:
        print("You win!\n")
        player_wins = player_wins + 1
    if computer_score == player_score:
        print("Draw!\n")

    x = x + 1

#print final results
input("\nGame over...Press any key to reveal your scores!")
print("\nYour score: ", player_wins, "\nComputer score: ", computer_wins)

if player_wins < computer_wins:
    print("Computer wins this game... unlucky!")
if player_wins > computer_wins:
    print("You win this game! Well done!")
if player_wins == computer_wins:
    print("It's a draw!")