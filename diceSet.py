import random


def roleDiceSet():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceSet = [dice1, dice2]
    if (dice1 == dice2):
        diceSet.append(dice1)
        diceSet.append(dice2)
    return diceSet
