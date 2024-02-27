import math

class Computer:
    def __init__(self):
        self.min = 1
        self.max = 100

    def guess(self):
        current_guess = math.floor((self.min + self.max) / 2)
        print(f"Computer's guess: {current_guess}")
        return current_guess

    def receive_hint(self, hint, guess):
        if hint == 'higher' and guess > self.min:
            self.min = guess
        if hint == 'lower' and guess < self.max:
            self.max = guess