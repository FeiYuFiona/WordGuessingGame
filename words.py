import argparse
from Game import Game


word = Game()

def play():
    word.play_report()

def test():
    word.test_report()

if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description = "Game mode")
    parser.add_argument("mode", choices = ["play", "test"], help = "Run with 2 modes")
    args = parser.parse_args()

    if args.mode == "play":
        word.play_report()
    elif args.mode == "test":
        word.test_report()
    else:
        print("Invalid game mode. Choose again")




