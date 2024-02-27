class Player:
    def guess(self):
        return int(input('Enter your guess: '))

    def receive_hint(self, hint, guess):
        print(f'The secret number is {hint} than {guess}.')