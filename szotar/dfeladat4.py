import random
import pprint
vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "    Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
diakok=[]
for i in range(8):
    diak={
        "név":vezeteknevek[random.randint(0,len(vezeteknevek)-1)]+" "+keresztnevek[random.randint(0,len(keresztnevek)-1)],
        "életkor":random.randint(14,19),
        "évfolyam":random.randint(9,12),
        "osztály":["A","B","C","D"][random.randint(0,3)],
        "cím":{
            "település":telepulesek[random.randint(0,len(telepulesek)-1)],
            "utca":utcak[random.randint(0,len(utcak)-1)],
            "házszám":random.randint(0,50)
        }
    }
    diakok.append(diak)
pprint.pprint(diakok)