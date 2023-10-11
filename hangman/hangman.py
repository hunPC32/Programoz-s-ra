import random

words = ["ALMA", "KUTYA", "IDIÓTA", "ZOLI", "WOLFF", "EMBER"]

rnd = random.randint(0, len(words)-1)

word = words[rnd]

state = "_"*len(word)

while word != state:
    guess = input("Tipp: ")
    new_state = ""
    if guess in word:
        for i in range(len(word)):
            if(guess == word[i]):
                new_state += guess
            else:
                new_state += state[i]
        state = new_state
        print(state)
    else:
        print("Nincs benne")