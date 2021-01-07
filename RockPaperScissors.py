import random
i = 'y'
#The Game and Outcomes. P.S. Don't forget elif...
def RockPaperScissors():
        playerChoice = input("rock, paper or scissors?")
        botChoice = random.choice(["rock","paper","scissors"])
        if playerChoice == "rock" and botChoice == "rock":
            print("You both chose",botChoice,"TRY AGAIN.")
        elif playerChoice == "rock" and botChoice == "paper":
            print("The bot chose",botChoice,"YOU LOSE!")
        elif playerChoice == "rock" and botChoice == "scissors":
            print("The bot chose", botChoice,"YOU WIN!")
        elif playerChoice == "paper" and botChoice == "rock":
            print("The bot chose",botChoice,"YOU WIN!")
        elif playerChoice == "paper" and botChoice == "paper":
            print("You both chose",botChoice,"TRY AGAIN.")
        elif playerChoice == "paper" and botChoice == "scissors":
            print("The bot chose", botChoice,"YOU LOSE!")
        elif playerChoice == "scissors" and botChoice == "rock":
            print("The bot chose", botChoice,"YOU LOSE!")
        elif playerChoice == "scissors" and botChoice == "paper":
            print("The bot chose",botChoice,"YOU WIN!")
        elif playerChoice == "scissors" and botChoice == "scissors":
            print("You both chose",botChoice,"TRY AGAIN.")
        else:
            print("Invalid Choice. TRY AGAIN.")

RockPaperScissors()

#Looping Mechanism
while i != 'n':
    i = input("Continue? y or n")
    if i == 'n':
        break
    RockPaperScissors()