from player import Player
import diceSet
import json
import copy

class Move():
    def __init__(self, markerPosition, diceNumber, boardEncoding, utility, output):
        self.markerPosition = markerPosition
        self.diceNumber = diceNumber
        self.boardEncoding = boardEncoding
        self.utility = utility
        self.output = output

    def __ge__(self,other):
        if self.utility >= other.utility:
            return True
        else:
            return False
