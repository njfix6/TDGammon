from game import Game
from player import Player
from marker import Marker



game = Game()
game.addPlayer(Player(1))
game.addPlayer(Player(2))
game.initBoard()



def testSimpleMove():
    game.players[2].moves = [4, 5, 6]
    if not game.players[2].move(game.board, 24, 1):
        raise AssertionError()
    if game.players[2].move(game.board, 24, 1):
        raise AssertionError()




    game.board.board = \
    [[], \
    [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2), Marker(2), Marker(2), Marker(2),Marker(2), Marker(2), Marker(2),Marker(2), Marker(2), Marker(2), Marker(2), Marker(2),Marker(2), Marker(2)], \
    [], [], [], [], \
    [], \
    [], \
    [], \
    [], [], [], \
    [], \
    [], \
    [], [], [], \
    [Marker(1)], \
    [], \
    [], \
    [], [Marker(1), Marker(1)], [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)],
    [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)], \
    [], \
    [Marker(1), Marker(1)]]


    game.players[2].moves = [4, 5, 6]
    if not game.players[2].move(game.board, 1, 1):
        raise AssertionError()





    print("testSimpleMove() passed")





def testBearOff():
    game.board.board = \
    [[], \
    [], \
    [], [], [], [], \
    [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
    [], \
    [Marker(2), Marker(2), Marker(2)], \
    [], [], [], \
    [], \
    [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
    [], [], [], \
    [Marker(1)], \
    [], \
    [], \
    [], [Marker(1), Marker(1)], [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)],
    [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)], \
    [Marker(2), Marker(2)], \
    [Marker(1), Marker(1)]]
    game.players[1].moves = [4, 5, 6]
    if game.players[1].move(game.board, 24, 1):
        raise AssertionError()
    if not game.players[1].move(game.board, 17, 1):
        raise AssertionError()

    if not game.players[1].move(game.board, 23, 1):
        raise AssertionError()
    if not game.players[1].move(game.board, 23, 1):
        raise AssertionError()
    print("testBearOff() passed")



def testWin():
    game.board.board = \
    [[], \
    [], \
    [], [], [], [], \
    [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
    [], \
    [Marker(2), Marker(2), Marker(2)], \
    [], [], [], \
    [], \
    [Marker(2), Marker(2), Marker(2), Marker(2), Marker(2)], \
    [], [], [], \
    [], \
    [], \
    [], \
    [], [],
    [], \
    [Marker(2), Marker(2)], \
    [], [Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1), Marker(1)]]

    if (not (game.gameComplete() == 1)):
        raise AssertionError()
    print("testBearOff() passed")

testSimpleMove()
testBearOff()
testWin()
