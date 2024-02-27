import random
from .player import Player
from .computer import Computer

class Game:
    HIGH_STRING = 'higher'
    LOW_STRING = 'lower'

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.player = Player()
        self.computer = Computer()

    def give_hint(self, guess):
        if guess < self.secret_number:
            self.player.receive_hint(self.HIGH_STRING, guess)
            self.computer.receive_hint(self.HIGH_STRING, guess)
        elif guess > self.secret_number:
            self.player.receive_hint(self.LOW_STRING, guess)
            self.computer.receive_hint(self.LOW_STRING, guess)

    def play(self):
        while True:
            user_guess = self.player.guess()
            if user_guess == self.secret_number:
                return 'Player wins!'
            else:
                self.give_hint(user_guess)

            computer_guess = self.computer.guess()

            if computer_guess == self.secret_number:
                return 'Computer wins!'
            else:
                self.give_hint(computer_guess)