from player import Player
import diceSet
import json
import copy

class Move():
    def __init__(self, markerPosition, diceNumber, boardEncoding):
        self.markerPosition = markerPosition
        self.diceNumber = diceNumber
        self.boardEncoding = boardEncoding
        with open('data.json') as data_file:
            data = json.load(data_file)
        self.moveValue = data.get(self.boardEncoding)
        if not self.moveValue:
            data[self.boardEncoding] = 0
            with open("data.json", "w") as data_file:
                json.dump(data, data_file)
            self.moveValue = 0

    def __ge__(self,other):
        if self.moveValue >= other.moveValue:
            return True
        else:
            return False
