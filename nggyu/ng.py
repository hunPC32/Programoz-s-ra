file = open("nevergonna.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

betuk = 0
betuk_szokozzel = 0
maganangzok = "aeiouAEIOU"
msz = 0
szsz = 0



for line in lines:
    line = line.strip()
    line.replace("Never", "Always")
    print(line)



    for char in line:
        if char in maganangzok:
            msz += 1
        betuk_szokozzel += 1
        if char != " ":
            betuk += 1


    szsz += len(line.split(" "))

print(betuk)
print(betuk_szokozzel)
print(msz)
print(szsz)