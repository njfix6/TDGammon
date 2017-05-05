from player import Player
import diceSet
import json
import copy
from move import Move


class NetworkUnit():
    def __init__(self, value = 1, weights = []):
        self.value = value
        self.weights = weights
    def getValue(self):
        return self.value


class Network():
    def __init__(self):
        self.hidden =[[],[]]
        numberHiddenNodes = 40
        for i in range(numberHiddenNodes):
            self.hidden[0].append(NetworkUnit(1, [1]*198))
        for i in range(2):
            self.hidden[1].append(NetworkUnit(1, [1]*numberHiddenNodes))
        #need to initicalize neural network
    def getValue(self, boardEncoding, player):
        boardEncodingString = ''.join(str(e) for e in boardEncoding)
        with open('data.json') as data_file:
            data = json.load(data_file)
        output = data.get(boardEncodingString)
        if output is not None :
            return output
        else:
            return [0,0]

    def saveNetwork(self, boardEncoding):
        boardEncodingString = ''.join(str(e) for e in boardEncoding)
        with open('data.json') as data_file:
            data = json.load(data_file)
        data[boardEncodingString] = [self.hidden[1][0].value, self.hidden[1][1].value]

        with open("data.json", "w") as data_file:
            json.dump(data, data_file)
