
from marker import Marker

class Board:
    def __init__(self):
        # 0 is the bottom part home and is player 2s home of the board. 25 is the top home and is player 1's
        # this is player 2's home, bottom right
        self.board = \
        [[], \
        [Marker(1), Marker(1)], \
        [], [], [], [], \
        [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
        [], \
        [Marker(2), Marker(2), Marker(2)], \
        [], [], [], \
        [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)], \
        [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
        [], [], [], \
        [Marker(1), Marker(1), Marker(1)], \
        [], \
        [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)], \
        [], [], [], [], \
        [Marker(2), Marker(2)], \
        []] # this is player 1's home, top right

        self.playerHole =[[], []]

    def move(self, player, markerLocation, diceRole, test = False):
        moveTo = self.isValidMove(player, markerLocation, diceRole)
        print("move is valid? : ", moveTo)
        if (moveTo):
            if (markerLocation == 26):
                currentMarker = self.playerHole[0][0]
            elif(markerLocation == 27):
                currentMarker = self.playerHole[1][0]
            else:
                currentMarker = self.board[markerLocation]
            if(len(self.board[moveTo]) == 1 and (not self.board[moveTo][0].player == player)):
                self.playerHole[1 if player==1 else 0].append(self.board[moveTo].pop())
            if (moveTo >= 25):
                moveTo = 25
            elif (moveTo <=0):
                moveTo = 0
            if not test:
                print("Marker: ", markerLocation, " move to: ", moveTo)

            self.board[moveTo].append(self.board[markerLocation].pop()) # pops of list and appends to list.
            return True
        return False
    def isValidMove(self, player, markerLocation, diceRole):

        if (len(self.playerHole[0]) and player == 1):
            if(markerLocation == 26 and diceRole in range(6)):
                moveTo = diceRole
            else:
                return False
        elif(len(self.playerHole[1]) and player == 2):
            if(markerLocation == 27 and diceRole in range(18,24)):
                moveTo = diceRole
            else:
                return False
        else:
            if (player == 1):
                moveTo = markerLocation+diceRole
            if (player == 2):
                moveTo = markerLocation-diceRole
        if (moveTo >= 25):
            moveTo = 25
        elif (moveTo <=0):
            moveTo = 0
        print("the final move to is : ", moveTo)
        #this is the base of checking a move, the above are special cases
        if (len(self.board[markerLocation]) > 0 and self.board[markerLocation][0].player == player):
            if ((len(self.board[moveTo]) <= 1) or (self.board[moveTo][0].player == player)):
                # check if in bear off

                if (moveTo == 0 and player == 2):
                    if (not self.isBearOff(2)):

                        return False
                elif (moveTo == 25 and player == 1):
                    if (not self.isBearOff(1)):
                        return False
                return moveTo
        print("it got to here")
        return False

    def winner(self):
        if (len(self.board[0]) == 15):
            return 2
        elif (len(self.board[25]) == 15):
            return 1
        else:
            return 0

    def isBearOff(self, player):
        count = 0
        if(player == 2):
            for i in range(6):
                for j in range(len(self.board[i])):
                    if (self.board[i][j].player == player):
                        count+=1
        else:
            for i in range(19, 26):
                for j in range(len(self.board[i])):
                    if (self.board[i][j].player == player):
                        count+=1
        if (count == 15):
            return True
        else:
            return False


    # https://www.gnu.org/software/gnubg/manual/html_node/A-technical-description-of-the-Position-ID.html
    # encoded by the obove algorithm with a few changes
    def encodeBoard(self, playerTurn):
        def encodeSide(playerTurn):
            encodeString = ""
            board = self.board
            if playerTurn == 2:
                board = board[::-1]
            for spot in board:
                if len(spot) == 0:
                    encodeString += "0"
                else:
                    for marker in spot:
                        if (marker.player == playerTurn):
                            encodeString += "1"
                    encodeString += "0"
            for marker in self.playerHole[playerTurn - 1]:
                encodeString += "1"
            encodeString += "0"
            return encodeString
        encodeString = encodeSide(playerTurn) + encodeSide(2 if playerTurn==1 else 1)
        return encodeString


    def printBoard(self):
        def printMarker(i):
            if (len(self.board[i])):
                print(self.board[i][0].player, end="")
                print(":", end="")
                print(len(self.board[i]), end=':')
            else:
                print ("0:0", end=':')
            print(i, end="")
            if(i<10):
                print(" ",end="")
            print(" ", end="")
        for i in range(13,len(self.board)):
            printMarker(i)
        print("      2:", end="")
        print(len(self.playerHole[1]), end="")
        print(":27")
        for i in range(12, -1, -1):
            printMarker(i)
        print("      1:", end="")
        print(len(self.playerHole[0]), end ="")
        print(":26")
