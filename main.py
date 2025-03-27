import random

class SnakeLadder:
    def __init__(self):
        self.position_player1 = 0

    @staticmethod
    def roll_dice():
        return random.randint(1,6)

    def play_turn(self):
        dice_value = self.roll_dice()
        option = random.choice(["No play", "Ladder", "Snake"])

        if option == "No Play":
            pass
        elif option == "Ladder":
            self.position_player1 += dice_value
        elif option == "Snake":
            self.position_player1 -= dice_value
            if self.position_player1 < 0:
                self.position_player1 = 0


        print(f"Dice rolled: {dice_value}, Option: {option}, New Position: {self.position_player1}")

game = SnakeLadder()

game.play_turn()