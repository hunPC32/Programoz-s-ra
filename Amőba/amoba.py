board = [
    [" ", " "," "],
    [" ", " "," "],
    [" ", " "," "]
]

def drawBoard():
    for r in range(3):
        for c in range(3):
            print("[" + board[r][c] + "]", end="")
        print()

player = "X"

    
drawBoard()

def gameOver():
    drawBoard()
    print(player, "nyert sajnos")
    exit()

def winTest():
    for i in range(3):
        if board[i][0] == " ":
            continue
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            gameOver()

    for i in range(3):
        if board[0][i] == " ":
            continue
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            gameOver()

    if board[1][1] == " ":
        pass
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][2]):
        gameOver()

while True:
    print(player, "köre.")
    row = int(input("Sor: "))
    column = int(input("Oszlop: "))
    if (row < 0 or row > 2) or (column < 0 or column > 2):
        print("Mér vagy dióta")
        continue
    if board[row][column] != " ":
        print("NEM")
        continue
    board[row][column] = player

    winTest()

    if player == "X":
        player = "O"
    else: 
        player = "X"
    drawBoard()

    