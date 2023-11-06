# import random

# options = ["rock", "paper", "scissors"]

# random_computer_choice =random.choice(options)

# def checkWin(playerChoice, computerChoice):
#    print(f"You Chose: {playerChoice}")
#    print(f"Computer Chose: {computerChoice}")
#    if playerChoice == computerChoice:
#        return "It's a tie!"
#    elif playerChoice == "rock" and computerChoice == "scissors":
#        return "Player Wins!"
#    elif playerChoice == "rock" and computerChoice == "paper" :
#        return "Computer Wins!"
#    elif playerChoice == "paper" and computerChoice == "rock" :
#        return "Player Wins!"
#    elif playerChoice == "paper" and computerChoice == "scissors" :
#        return "Computer Wins!"
#    elif playerChoice == "scissors" and computerChoice == "rock" :
#        return "Computer Wins!"
#    elif playerChoice == "scissors" and computerChoice == "paper" :
#        return "Player Wins!"

# def getChoices():
#     player_choice = input("Enter a choice (rock, paper or scissors): ")
#     computer_choice = random_computer_choice
#     choices= {"playerChoice" : player_choice, "computerChoice" : computer_choice}
#     outcome= checkWin(player_choice, computer_choice)
#     return print(outcome)

# getChoices()


# age = 64
# print(age.bit_length())

# items = ["test", 3, 44, 52, 12]
# for  index, item in enumerate(items):
#     print(item, index)

count = 0
while count < 10:
    print(count)
    count= count + 1