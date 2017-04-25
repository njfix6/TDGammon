

from game import Game
from player import Player
from tdAgent import TDAgent
import json


def main():

    with open("data.json", "w") as data_file:
        json.dump({}, data_file)

    game = Game()
    game.addPlayer(TDAgent(1))
    game.addPlayer(TDAgent(2))
    # game.addPlayer(Player(1))
    # game.addPlayer(Player(2))
    game.initBoard()
    game.startGame()



if __name__ == "__main__": main()
