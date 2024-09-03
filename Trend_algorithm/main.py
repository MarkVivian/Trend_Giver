from random import Random

import Trend_Algorithm.Trend as Tr
import rock_paper_scissors.game as game

def Runner():
    print("running the main file.")
    Tr.TrendAlg().runner()

def resemble_user():
    items = ["paper", "rock", "scissors"]
    number = Random().randint(1,3)
    

if __name__ == "__main__":
    print("choose between rock, paper, scissors")
    number = 0
    while True:
        user = resemble_user()
        game.Game().play(user, number)
        number += 1

