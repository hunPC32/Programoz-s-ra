import random

def rollDice(dice):
    rnd = random.randint(0,len(dice)-1)
    return(dice[rnd])
