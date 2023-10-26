li1 = ["Zoli""Idiota""Vagy""Alma""Körte""Banán""Banán""Szilva""Alma"]
li2 = ["Zsolti""Idiota""IS""Alma""Körte""Banán""Banán""Roland""Alma"]

set1 = set(li1)
set2 = set(li2)

print(set1.union(set2))
print(set1.intersection(set2))  #metszet
print(set1.difference(set2))