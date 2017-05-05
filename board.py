
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
        [],\
        [],\
        []]
        # 25 is player 1's home, top right
        # 26 is player 1's hole
        # 27 is player 2's holw


    def move(self, player, markerLocation, diceRole, test = False):
        moveTo = self.isValidMove(player, markerLocation, diceRole)
        if (not moveTo is False):
            if(len(self.board[moveTo]) == 1 and (not self.board[moveTo][0].player == player)):
                self.board[27 if player==1 else 26].append(self.board[moveTo].pop())
            self.board[moveTo].append(self.board[markerLocation].pop()) # pops of list and appends to list.
            if not test:
                print("Marker: ", markerLocation, " move to: ", moveTo)
            return True
        if not test:
            print("Marker: ", markerLocation, " cant be move to: ", moveTo)
        return False
    def isValidMove(self, player, markerLocation, diceRole):
        #special cases
        boardState = self.getBoardState(player)
        if markerLocation == 25 or markerLocation == 0:
            return False
        if boardState == "knocked":
            if(markerLocation == 26):
                moveTo = diceRole
            elif markerLocation == 27:
                moveTo = 25 - diceRole
            else:
                return False
        else:
            if (player == 1):
                moveTo = markerLocation+diceRole
            elif (player == 2):
                moveTo = markerLocation-diceRole
            if (moveTo >= 25 or moveTo <= 0) and not boardState == "bearOff":
                return False
            elif boardState == "bearOff":
                if (moveTo >= 25):
                    moveTo = 25
                elif (moveTo <=0):
                    moveTo = 0

        #basic moving logic
        if (len(self.board[markerLocation]) > 0 and self.board[markerLocation][0].player == player):
            if ((len(self.board[moveTo]) <= 1) or (self.board[moveTo][0].player == player)):
                return moveTo
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
        def encodeSide(player):
            encode = []
            board = self.board[1:25]
            if player == 2:
                board = board[::-1]
            for spot in board:
                if len(spot) == 0 or not (spot[0].player == player):
                    encode+=[0,0,0,0]
                else:
                    if(len(spot) == 1):
                        encode+=[1,0,0,0]
                    elif(len(spot) == 2):
                        encode+=[1,1,0,0]
                    else:
                        encode+=[1,1,1,(len(spot)-3)/2]
            return encode

        encodeString = encodeSide(1) + encodeSide(2)
        encodeString.append(len(self.board[26]) / 2)  #player 1 knocked off
        encodeString.append(len(self.board[27]) / 2)   #plaer 2 knocked off
        encodeString.append(len(self.board[0]) / 15) #player 1 successfull removed
        encodeString.append(len(self.board[25]) / 15)#player 2 successfull removed
        if playerTurn == 1:
            encodeString+=[0,1]
        else:
            encodeString+=[1,0]
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
        for i in range(13,len(self.board)-2):
            printMarker(i)
        print("      2:", end="")
        print(len(self.board[27]), end="")
        print(":27")
        for i in range(12, -1, -1):
            printMarker(i)
        print("      1:", end="")
        print(len(self.board[26]), end ="")
        print(":26")


    def getBoardState(self, player):
        if  player == 1:
            if len(self.board[26]):
                return "knocked"
        elif player == 2:
            if len(self.board[27]):
                return "knocked"
        if self.isBearOff(player):
            return "bearOff"
        return "middle"
