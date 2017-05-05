
import diceSet


class Player:
    def __init__(self, playerNum):
        self.number = playerNum
        self.moves = []

    def takeTurn(self, board, markerLocation, diceNum):
        self.move(board, markerLocation, diceNum)

    def move(self, board, markerLocation, diceNum):
        if (len(self.moves) >= diceNum):
            diceNum = diceNum - 1
            if board.move(self.number, markerLocation, self.moves[diceNum]):
                self.moves[diceNum] = True #probably dont need this line !!!!!!!!!!!!!!!
                self.moves.pop(diceNum)
                return True
            else:
                return False
        else:
            print ("Move already completed")
            return False


    def rollDice(self):
        dice = diceSet.roleDiceSet()
        self.moves = dice
        print ("You rolled: ", dice[0], ", ", dice[1])
