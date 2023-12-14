import random
from helper import rollDice

green = ['brain', 'brain', 'brain', 'flee', 'flee', 'shotgun']
yellow = ['brain', 'brain', 'flee', 'flee', 'shotgun', 'shotgun']
red = ['brain', 'flee', 'flee', 'shotgun', 'sotgun', 'shotgun']

cup = [red, red, red, yellow, yellow, yellow, green, green, green, green, green, green]

random.shuffle(cup)

d1 = cup.pop()
d2 = cup.pop()
d3 = cup.pop()

hand = []
hand.append(cup.pop())
hand.append(cup.pop())
hand.append(cup.pop())

temp_brains = 0
shotguns = 0

for dice in hand:
    res = rollDice(dice)
    print(res)
    if res == 'flee':
        cup.append(dice)
    elif res == 'brain':
        temp_brains += 1
    else:
        shotguns += 1



print(f"Brains: {temp_brains}, Shotguns: {shotguns}, cup: {len(cup)}")
