import random


class SnakeLadder:
    def __init__(self):
        self.position_player1 = 0
        self.dice_roll_count = 0

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def play_turn(self):
        dice_value = SnakeLadder.roll_dice()
        self.dice_roll_count += 1
        option = random.choice(["No Play", "Ladder", "Snake"])

        if option == "No Play":
            pass
        elif option == "Ladder":
            if self.position_player1 + dice_value <= 100:
                self.position_player1 += dice_value
        elif option == "Snake":
            self.position_player1 -= dice_value
            if self.position_player1 < 0:
                self.position_player1 = 0

        print(f"Dice rolled: {dice_value}, Option: {option}, New Position: {self.position_player1}")

    def play_game(self):
        while self.position_player1 < 100:
            self.play_turn()

        print(f"\nGame Over! Total dice rolls: {self.dice_roll_count}")


# Start the game
game = SnakeLadder()
game.play_game()
