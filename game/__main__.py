from .game import Game

def main():
    while True:
        game = Game()
        result = game.play()
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()