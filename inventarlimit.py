import json
Acount = {
    "Inventar":[],
    "Coins": 1000
}
def items(auswahl):
    if len(Acount["Inventar"])< 5:
        if auswahl == "star":
            if Acount["Coins"] < 50:
                print(f"Du hast zu wenig münzen du brauchst noch {50 - Acount['Coins']} Münzen")
            else:
                menge = 50
                Acount["Inventar"].append(auswahl)
                Acount["Coins"]-=menge
                print(f"erfolgreich gekauft du hast jetzt {Acount['Coins']} Münzen")
        elif auswahl == "shell":
            if Acount["Coins"] < 30:
                print(f"Du hast zu wenig münzen du brauchst noch {30 - Acount['Coins']} Münzen")
            else:
                menge = 30
                Acount["Inventar"].append(auswahl)
                Acount["Coins"]-=menge
                print(f"erfolgreich gekauft du hast jetzt {Acount['Coins']} Münzen")
        elif auswahl == "block":
            if Acount["Coins"] < 10:
                print(f"Du hast zu wenig münzen du brauchst noch {30 - Acount['Coins']} Münzen")
            else:
                menge=10
                Acount["Inventar"].append(auswahl)
                Acount["Coins"]-=menge
                print(f"erfolgreich gekauft du hast jetzt {Acount['Coins']} Münzen")
        else:
            print("Dieses Item haben wir nicht")
    elif len(Acount["Inventar"]) == 5:
        print("Du hast zu schon zu viele items im inventar")

def verkaufen(sale):
        if sale=="star":
            if sale in Acount["Inventar"]:
                Acount["Inventar"].remove(sale)
                Acount["Coins"]+=40
                print(f"Dein Star wurde erfolgreich verkauft du hast jetzt {Acount['Coins']} Münzen")
        elif sale=="shell":
            if sale in Acount["Inventar"]:
                Acount["Inventar"].remove(sale)
                Acount["Coins"]+=20
                print(f"Deine shell wurde erfolgreich verkauft du hast jetzt {Acount['Coins']} Münzen")
        elif sale=="block":
            if sale in Acount["Inventar"]:
                Acount["Inventar"].remove(sale)
                Acount["Coins"]+=5
                print(f"Dein block wurde erfolgreich verkauft du hast jetzt {Acount['Coins']} Münzen")
        else:
            print("dieses item hast du nicht")
while True:
    print("Was willst du machen machen ein item kaufen, verkaufen, anzeigen")
    Auswahl=input("oder ausgeben? ").lower()
    if Auswahl == "kaufen":
        itemname=input("Welches Item willst du kaufen    star:50  |  shell:30  |  block:10  ").lower()
        items(itemname)
    elif Auswahl == "verkaufen":
        verkauf=input("welches item willst du verkaufen    star:40  |  shell:20  |  block:5  ").lower()
        verkaufen(verkauf)
    elif Auswahl == "anzeigen":
        print(Acount)
    elif Auswahl=="ausgeben":
        print(Acount)
        was=input("wirklich ausgeben j/n " )
        if was == "j":
            with open("savegame.json", "w") as datei:
                json.dump(Acount, datei, )
        else:
            print("dann wieder zum anfang")
    else:
        print("bitte gebe nur das ein was da steht")
