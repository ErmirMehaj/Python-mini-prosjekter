import random

def steinSaksPapir():
    print("Velkommen til 🪨, ✂️, 📄!")

    total = 0
    poeng = 0


    while True:
     
     poeng = 0
     
     antallRunder = int(input("Velg antall runder du vil spille: "))
     

     for runde in range(antallRunder):
        velg = input("Velg stein eller saks eller papir: ").lower()
        generer = random.choice(["stein", "saks", "papir"]).lower()

        if (velg == generer):
           print("Ingen poeng, tie")
        elif (velg == "stein" and generer == "saks"):
          print("Poeng til deg! Stein tar saks")
          poeng+=1
        elif (velg == "stein" and generer == "papir"):
          print("Du tapte, papir tar stein")
        elif (velg == "saks" and generer == "papir"):
          print("Poeng til deg! Saks tar papir")
          poeng+=1
        elif (velg == "papir" and generer == "stein"):
          print("Poeng til deg! Papir tar stein")
          poeng+=1
        elif (velg == "papir" and generer == "saks"):
          print("Du tapte, saks tar papir")   
        else:
          print("Feil operator")
     print(f"Du fikk {poeng} poeng denne runden!")     

     total+=poeng

     spillIgjen = input("Vil du spille igjen? j/n ")
     if spillIgjen != "j":
            print(f"Den er grei, ses neste gang. Du fikk {total} poeng totalt!")
            break
    
steinSaksPapir()                    
         


