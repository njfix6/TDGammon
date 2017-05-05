from player import Player
import diceSet
import json
from pprint import pprint
import copy
from move import Move
from network import Network

class TDAgent(Player):
    def __init__(self, playerNum):
        Player.__init__(self, playerNum)
        self.delta = 0
        self.epsilon = 0
    def takeTurn(self, board, markerLocation, diceNum, learning = False, net = None):


        if board.winner():
            if board.winner() == self.number:
                self.win(board, net)

            else:
                self.lost(board, net)
            net.saveNetwork(board.encodeBoard())
            print("network output: ",net.hidden[1][0].value, net.hidden[1][1].value)
            return False
        else:
            bestMove = self.getBestMove(board, self.getValidMoves(board, net), net)
            if bestMove:
                if learning:
                    self.learn(bestMove, board, net)
                    net.saveNetwork(board.encodeBoard(self.number))

                markerLocation = bestMove.markerPosition
                diceNum =  bestMove.diceNumber
                # print("trying to move the board with :", markerLocation ," with dice :", diceNum)

                self.move(board, markerLocation, diceNum)
                print("network output: ",net.hidden[1][0].value, net.hidden[1][1].value)
            else:
                print("no possible moves left")
                return False
        test = input('continue??? ')




    def move(self, board, markerLocation, diceNum, test = False):
        if (len(self.moves) > diceNum):
            if board.move(self.number, markerLocation, self.moves[diceNum], test):
                if not test:
                    self.moves.pop(diceNum)
                return True
            else:
                if not test:
                    print ("Cant move ", markerLocation, " with dice :", diceNum)
                return False
        else:
            print ("Move already completed")
            return False
    def getValidMoves(self, board, net):
        validMoves = []
        for movePosition in range(len(self.moves)):
            for markerPosition in range(len(board.board)):
                if len(board.board[markerPosition]) > 0 and board.board[markerPosition][0].player == self.number:
                    testBoard = copy.deepcopy(board)
                    if testBoard.move(self.number, markerPosition, self.moves[movePosition], test = True):

                        oppositePlayer = 1 if self.number==1 else 2
                        boardEncoding = testBoard.encodeBoard(oppositePlayer)

                        networkOutput = net.getValue(boardEncoding, oppositePlayer)
                        move = Move(markerPosition, movePosition, boardEncoding, self.computeUtility(networkOutput), networkOutput)


                        validMoves.append(move)
        return validMoves

    def getBestMove(self, board, validMoves, net):

        with open('data.json') as data_file:
            data = json.load(data_file)
        validMoves = self.getValidMoves(board, net)
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


    def learn(self, bestMove, board, net):
        if not bestMove:
            return False
        currentInput = board.encodeBoard(self.number)
        currentOutput = net.getValue(board.encodeBoard(self.number), self.number)
        self.backProp(currentInput, currentOutput, bestMove.output, net)#get next ouput from best move






    def gradient(self, hiddenUnit):
        return hiddenUnit.getValue() * (1-hiddenUnit.getValue())

    def backProp(self, In, out, expected, net):
        #!!!! need to load network
        # net = Network()
        print("bin: ", In)
        print("bout: ", out)
        print("bexprected: ", expected)
        lambd = 0.7
        alpha = 0.1
        beta = 0.1
        Ew = [[1 for k in range(2)] for j in range(40)]
        Ev = [[[1 for k in range(2)] for j in range(40)] for i in range(198)]
        for j in range(len(net.hidden[0])):
            for k in range(len(out)):
                Ew[j][k] = (lambd * Ew[j][k]) + (self.gradient(net.hidden[1][k]) * net.hidden[0][j].getValue())
                for i in range(len(In)):
                    Ev[i][j][k] = ( (lambd * Ev[i][j][k] ) + (self.gradient(net.hidden[1][k]) * net.hidden[1][k].weights[j] * self.gradient(net.hidden[0][j]) * In[i]))
        error = [1 for k in range(2)]
        for k in range(len(out)):
            error[k] = expected[k] - out[k]
        for j in range(len(net.hidden[0])):
            for k in range(len(out)):
                net.hidden[1][k].weights[j] += beta * error[k] * Ew[j][k]
                for i in range(len(In)):
                    net.hidden[0][j].weights[i] += alpha * error[k] * Ev[i][j][k]
        print("in: ", In)
        print("out: ", out)
        print("exprected: ", expected)


    def lost(self, board, net):
        if (learning):
            if(self.number == 1):
                actual[0] = 0
                actual[1] = 1
            else:
                actual[0] = 1
                actual[1] = 0
            In = board.encodeBoard(self.number)
            out = net.getValue(In)

            self.backProp(In, out, actual, net)
    def win(self, board, net):
        if (learning):
            if(self.number == 1):
                actual[0] = 1
                actual[1] = 0
            else:
                actual[0] = 0
                actual[1] = 1
            In = board.encodeBoard(self.number)
            out = net.getValue(In)
            self.backProp(In, out, actual, net)

    def computeUtility(self, output):
        oppositePlayer = 1 if self.number== 1 else 2
        return output[int(oppositePlayer- 1)]










    def updateFile(self):
        print("todo")
