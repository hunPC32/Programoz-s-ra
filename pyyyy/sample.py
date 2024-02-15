# Írj egy függvényt, ami megkap egy listát (pl.: [1,2,3,4]) és visszaadja a kumulatív összeget (pl.: 1, 1+2, 1+2+3 ..., tehát az előző példa a [1, 3, 6, 10] listát kell hogy visszaadja). A függvény működjön tetszőleges, számokat tartalmazó listákkal!

#list = [1, 5, 6, 8]
#k = 0
#
#def kumulativ(li):
#	res = []
#	for i in len(li):
#		res.append(sum(li[:i + 1]))
#	return res
#
#print(kumulativ([1,5,6,8]))
#
#
# Írj függvényt, amely megfordít egy megkapott listát, és azt visszaadja!
#
#def reverse(li):
#	return li[::-1]
#
#print(reverse([1,5,7,8]))

# Írj függvényt, ami a következőt hajtja végre: 
# Ha az átadott sztring hossza legalább 3, akkor a végéhez adjuk hozzá az 'ing' ragot.
# Ha 'ing'-re végződik, akkor ehelyett az 'ly' ragot tegyük hozzá.
# Ha a sztring hossza rövidebb 3 karakternél, akkor hagyjuk változatlanul.
# Adjuk vissza az eredménysztringet.

def verbing(s):
	if len(s) < 3:
		return s
	if s[-3:] == "ing":
		return s + "ly"
	return s + "ing"

print(verbing("xd"))
print(verbing("fight"))
print(verbing("flying"))

# Egy adott sztringben keressük meg a 'not' és 'bad' szavak előfordulási helyét. Ha a 'bad' a 'not' szót követi, akkor cseréljük ki az egész 'not'...'bad' részsztringet a 'good' szóra.
# Adjuk vissza az eredmény sztringet.
# Példa: 'This dinner is not that bad!' ->
#        This dinner is good!

def not_bad(s):
	if s.find("not") == -1 or s.find("bad") == -1:
		return s
	if s.find("not") < s.find("bad"):
		return s[:s.find("not")] + "good" + s[s.find("bad")+3:]
	return s


print(not_bad("This dinner is not that bad!"))

# Írj függvényt, amely eldönti egy szóról, hogy az palindróm-e (visszafelé ugyan az, mint előre felé)! A függvény igaz-hamis értékkel térjen vissza!

def palindrom(szo):
	return szo == szo[::-1]

print(palindrom("indulagörögaludni"))
print(palindrom("alma"))

# Döntsük el egy magyar szóról, hogy milyen hangrendű (mély, magas, vegyes, vagy semmilyen hangrendű).
# Ha egy szóban vmennyi magánhangzó mély hangrendű, akkor a szó mély hangrendű. Ha egy szóban vmennyi magánhangzó magas hangrendű, akkor a szó magas hangrendű. Ha egy szóban mély és magas hangrendű magánhangzók is előfordulnak, akkor a szó vegyes hangrendű. Ha a szóban nincs egyetlen magánhangzó sem, akkor semmilyen hangrendű.

# Mély hangrendű magánhangzók: a, á, o, ó, u, ú.
# Magas hangrendű magánhangzók: e, é, i, í, ö, ő, ü, ű. 

def hangrend(szo:str):
	mely = "aáoóuú"
	magas = "eéiíöőüű"
	is_mely = False
	is_magas = False

	for hang in mely:
		if hang in szo:
			is_mely == True
			break

	for hang in magas:
		if hang in szo:
			is_magas == True
			break
	if is_mely and is_magas:
		return "vegyes"
	if is_mely:
		return "mely"
	if is_magas:
		return "magas"
	return "semmilyen"


print(hangrend("macska"))
print(hangrend("cica"))
print(hangrend("egér"))

