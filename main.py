import random

class SnakeLadder:
    def __init__(self):
        self.position = 0

    @staticmethod
    def roll_dice():
        return random.randint(1,6)

