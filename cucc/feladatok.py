# 1. Írj egy logikai értékkel visszatérő Python függvényt, amely eldönti egy paraméterként kapott egész számról, hogy az maradék nélkül osztható-e 2-vel és 3-mal is egyszerre!


def divisible_2_3(num):
    if num % 6 == 0:
        return True
    else:
        return False
    
print(divisible_2_3(5))


# 2. Írj egy Python függvényt, amely paraméterként megkap két egész számot, és visszatér a két szám által meghatározott (zárt) intervallumban található egész számok összegével!

def intervalSum(num1, num2):
    szam = 0
    for i in range(num1, num2):
        szam += i
    print(szam - num1)
intervalSum(2, 5)

# 3. Írj egy Python programot, amely bekér két szót a felhasználótól, és kiírja a képernyőre, van-e olyan betű amelyik mindkét szóban előfordul!

def commonLetters(word1, word2):
    for l in word1:
        if l in word2:
            print(f"Van: {l}")
            return 0
        else:
            print("Nincs")
commonLetters("zoli", "buzi")

# 4. Írj egy Python programot, amely egy tetszőleges méretű listában tárolt számok mediánját határozza meg!

def listMedian(list):
    list.sort()
    if len(list) % 2 == 0:
        print((list[len(list) / 2] + list[len(list) / 2 - 1])) / 2
    else:
        pass