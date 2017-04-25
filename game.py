from board import Board
from player import Player
from tdAgent import TDAgent
import diceSet

class Game:
    def __init__(self):
        self.players = [Player(0)]
        self.board = ""
        self.turn = -1
    def startGame(self):
        self.changeTurn()
        while (not self.gameComplete()):
            self.takeTurn()

    def addPlayer(self, player):
        self.players.append(player)
    def initBoard(self):
        self.board = Board()
    def changeTurn(self):
        if self.turn == -1:
            player1Roll = diceSet.roleDiceSet()
            player2Roll = diceSet.roleDiceSet()
            if ((player1Roll[0]+player1Roll[1]) > (player2Roll[0]+player2Roll[1])):
                self.turn = 1
            else:
                self.turn = 2
        elif self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
        else:
            self.turn = -1
    def checkTurn(self):
        return self.turn
    def takeTurn(self):
        exit = 1
        print("Player ",self.turn," starts their turn.")
        self.board.printBoard()
        self.players[self.turn].rollDice()
        while ((len(self.players[self.turn].moves) > 0) and exit):
            markerLocation = -1
            diceNumber = -1
            if (not type(self.players[self.turn]) is TDAgent):
                markerLocation = input('Enter the marker location: ')
                if markerLocation.lower() == "e":
                    exit = 0
                markerLocation = int(markerLocation)
                diceNumber = int(input('What dice u want to move (1 or 2): '))
            if not self.players[self.turn].takeTurn(self.board, markerLocation, diceNumber):
                exit = 0
        self.changeTurn()
    def gameComplete(self):
        if (self.board.winner()):
            print("Winner is player " + str(self.board.winner()))
        return self.board.winner()
