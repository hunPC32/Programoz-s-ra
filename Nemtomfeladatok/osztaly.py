hossz = int(input("Hossz: "))

for szam in range(hossz):
    szam = int(input("Pont: "))
    if szam >= 80:
        print("jeles")
    elif szam >= 70:
        print("jo")
    elif szam >= 60:
        print("kozepes")
    elif szam >= 50:
        print("elegseges")
    else:
        print("elegtelen")