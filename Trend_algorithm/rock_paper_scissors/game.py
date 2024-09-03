from random import Random
import json

class Game:
    def __init__(self):
        self.pieces = ["rock", "paper", "scissors"]


    def randomization(self):
        # Get a random value between 1 and 3.
        random_number = Random().randint(1, 3)
        print(random_number)

        # Return the corresponding piece.
        return self.pieces[random_number - 1]

    def play(self, player_choice, game_number):
        computer_choice = self.randomization()
        player_choice = player_choice.lower()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            outcome = "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            outcome = "player wins"
        else:
            outcome = "computer wins"
        self.store_data(player_choice, computer_choice, outcome, game_number)
        print(f"Outcome: {outcome}")

    @staticmethod
    def store_data(player, computer, outcome, game_number):
        # Data to be added to the JSON file
        new_data = {
            "player_choice": player,
            "computer_choice": computer,
            "outcome": outcome,
            "game_number": game_number
        }

        # Attempt to read existing data from game_data.json
        try:
            with open("game_data.json", "r") as f:
                # Load existing data
                existing_data = json.load(f)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty list
            existing_data = []

        # Append the new data to the existing data list
        existing_data.append(new_data)

        # Write the updated data back to game_data.json
        with open("game_data.json", "w") as f:
            json.dump(existing_data, f, indent=4)
