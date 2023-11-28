def hello():
    print("hello! have a nice day.")
def bye():
    print("bye! have a wonderful time.")


import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors? ")
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
    play_again = input("play again? (yes/no): ")
    if play_again != "yes":
        break
print("bye you idiot!")