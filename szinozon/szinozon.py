import random

def listToString(li):
    string = ""
    for w in li:
        string += w
    return string

colors = ["I", "R", "O", "Y", "L", "P", "V", "B", "S", "G"]

print("="*177)
print("Színözön")
print("="*177)

print("Írj be négy betűt az alábbiak közül")
print(colors)

random.shuffle(colors)
solution = colors[:4]

round = 1
history = []

while True:
    guess = input(f"{round}. Tipp: ")

    if guess == "H":
        print(history)
        for h in history:
            print(h)
        continue

    if len(guess) != 4:
        print("Hibás tipp")
        continue
    result = []

    for i in range(4):
        if guess[i] == solution[i]:
            result.append("X")
        elif guess[i] in solution:
            result.append("O")
    history.append(f"{guess} - {listToString(result)}")
    print(history[-1])

    if round == 10:
        break
    round += 1