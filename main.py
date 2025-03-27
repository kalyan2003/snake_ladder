import random

class SnakeLadder:
    def __init__(self):
        """
        Taking the positions of palyers and taking variables which count the dice roll count

        """
        self.positions = {"Player 1": 0, "Player 2": 0}
        self.dice_roll_count = {"Player 1": 0, "Player 2": 0}

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def play_turn(self, player):
        """
        Implements the die roll function based on the conditions of the given problems
        Arguments: player (string)

        """
        dice_value = SnakeLadder.roll_dice()
        self.dice_roll_count[player] += 1
        option = random.choice(["No Play", "Ladder", "Snake"])

        if option == "No Play":
            pass
        elif option == "Ladder":
            if self.positions[player] + dice_value <= 100:
                self.positions[player] += dice_value
        elif option == "Snake":
            self.positions[player] -= dice_value
            if self.positions[player] < 0:
                self.positions[player] = 0

        print(f"{player} rolled: {dice_value}, Option: {option}, New Position: {self.positions[player]}")

    def play_game(self):
        players = ["Player 1", "Player 2"]
        turn = 0  # Track player turns

        while True:
            current_player = players[turn % 2]
            self.play_turn(current_player)

            if self.positions[current_player] == 100:
                print(f"\n {current_player} wins the game in {self.dice_roll_count[current_player]} rolls! ")
                break

            turn += 1 

# Start the game
game = SnakeLadder()
game.play_game()
