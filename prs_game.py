import random
import time
import string

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock , scissors: paper }

player_score = 0
computer_score = 0

def start():
    print "let's play the game of rock, paper, scissor"
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input("Rock = 1\nPaper = 2\nscissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "oop's i didn't understand that, please enter 1, 2 , 3."


def result(player, computer):
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3"
    time.sleep(0.5)
    print "computer threw {0}!".format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "Tie game!"
    else:
        if rules[player] == computer:
            print "Your victory has been assured"
            palyer_score =+ 1
        else:
            print "As the computer laught as you realise that you have been defeated!"
            computer_score =+1


def play_again():
        answer = input("Would you like to play again? Y/N: ")
        if answer in("y", "Y", "Yes", "yes", "Of course"):
            return answer
        else:
            print "Thank You for playing our game, see you next time"
def scores():
    global player_score, computer_score
    print "High Score"
    print "Player", player_score
    print "computer", computer_score

        
if __name__ == '__main__':
    start()
    



    
























    








