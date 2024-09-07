import json
from random import Random
from time import sleep

import Trend_Algorithm.Trend as Tr
import rock_paper_scissors.game as game

def Runner():
    print("running the main file.")
    Tr.TrendAlg().runner()

def resemble_user(counter):
    items = ["paper", "rock", "scissors"]
    if (counter % 3) == 0:
        print(f"the value of counter % 3 is {counter}")
        value = 3
    else:
        value = Random().randint(1,2)
    return items[value - 1]

    

if __name__ == "__main__":
    # Runner()
    print("choose between rock, paper, scissors")
    # read the last item in the json file.
    with open('game_data.json', 'r') as f:
        data = json.load(f)
        last_item = data[-1]
        number = last_item['game_number'] + 1
    while number < 1000:
        user = resemble_user(number)
        game.Game().play(user, number)
        number += 1

