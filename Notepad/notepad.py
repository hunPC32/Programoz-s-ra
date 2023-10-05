def addNewItem():
    f = open("notes.txt", "a")
    text = input("Note: ")
    f.write("\n" + text)
    f.close()

def showItems():
    f = open("notes.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        print(line)

def deleteItems():
    f = open("notes.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        print(str(i) + ". | " + lines[i].strip())

    deleteID = int(input("Delete number: "))
    f = open("notes.txt", "w")
    for i in range(len(lines)):
        if i != deleteID:
            f.write(lines[i])
    f.close

command = input("$: ")

while command != "X":
    if command == "A":
        addNewItem()
    elif command == "S":
        showItems()
    elif command == "D":
         deleteItems()
    command = input("$: ")