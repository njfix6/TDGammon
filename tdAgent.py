from player import Player
import diceSet
import json
from pprint import pprint
import copy
from move import Move

class TDAgent(Player):
    def __init__(self, playerNum):
        Player.__init__(self, playerNum)
        self.delta = 0
        self.epsilon = 0
    def takeTurn(self, board, markerLocation, diceNum):
        bestMove = self.getBestMove(board, self.getValidMoves(board))
        if bestMove:
            self.learn(bestMove, board)
            markerLocation = bestMove.markerPosition
            diceNum =  bestMove.diceNumber
            print("trying to move the board with :", markerLocation ," with dice :", diceNum)
            self.move(board, markerLocation, diceNum)

        else:
            print("no possible moves left")
            return False
        test = input('continue??? ')




    def move(self, board, markerLocation, diceNum, test = False):
        if (len(self.moves) > diceNum):
            if board.move(self.number, markerLocation, self.moves[diceNum], test):
                if not test:
                    self.moves.pop(diceNum)
                    print ("Marker moved")
                return True
            else:
                if not test:
                    print ("Cant move ", markerLocation, " with dice :", diceNum)
                return False
        else:
            print ("Move already completed")
            return False
    def getValidMoves(self, board):
        validMoves = []
        for movePosition in range(len(self.moves)):
            for markerPosition in range(len(board.board)):
                if len(board.board[markerPosition]) > 0 and board.board[markerPosition][0].player == self.number:
                    testBoard = copy.deepcopy(board)
                    if testBoard.move(self.number, markerPosition, self.moves[movePosition], test = True):
                        validMoves.append(Move(markerPosition, movePosition, testBoard.encodeBoard(self.number)))
        # n
        return validMoves

    def getBestMove(self, board, validMoves):

        with open('data.json') as data_file:
            data = json.load(data_file)
        validMoves = self.getValidMoves(board)
         #best move value, and the move
        if len(validMoves) >=1:
            bestMove = validMoves[0]
            for move in validMoves:
                if move >= bestMove:
                    bestMove = move
            return bestMove
        else:
            print("no valid moves")
            return False


    def learn(self, bestMove, board):
        if not bestMove:
            return False

        nextMoveValue = bestMove.moveValue
        VTPlus1 = int(nextMoveValue)
        winner = board.winner()
        if (winner):
            if (self.number == winner):
                VTPlus1 = 1
            else:
                VTPlus1 = 0

        VT = board.encodeBoard(self.number)
        alpha = 0.1
        lambd = 0.7
        delta = self.delta

        if delta == 0:
            delta = 1
        self.epsilon = lambd * self.epsilon + VTPlus1 / delta
        print("delta: ", self.delta)
        #update file with delta
        with open('data.json', "r") as data_file:
            data = json.load(data_file)
            value = data.get(VT)
            if value is None:
                value = 0
            data[VT] = value + self.delta
        with open("data.json", "w") as data_file:
            json.dump(data, data_file)
        # end update

        deltaTPlus1 = self.delta + alpha * (VTPlus1 - data[VT]) * self.epsilon

        self.delta = deltaTPlus1


    def updateFile(self):
        print("todo")
