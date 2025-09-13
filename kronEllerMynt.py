import random

def kronEllerMynt():
    total=0
    rekord=0
    while True:
     print("Velkommen til kron eller mynt spillet! Om å få 3 av 3 poeng")

     poeng = 0

     antallRunder = int(input("Hvor mange runder vil du spille denne gangen?"))
     

     for runde in range(antallRunder):
        fasit = random.choice(["kron", "mynt"]).lower()
        gjett = input("Kron eller Mynt: ")
        

        if gjett == fasit:
            print("Riktig!")
            poeng+=1
        else:
            print(f"Feil. Det riktige var {fasit}")
     if poeng == 0:
        print(f"Godt forsøk, men ikke bra nok, siden du fikk {poeng} av {antallRunder}.")
     elif poeng < antallRunder:
        print(f"Nesten, men prøv bedre neste gang, siden du fikk {poeng} av {antallRunder}")
     else:
        print(f"Wow, du er helt rå! Du fikk hele {poeng} av {antallRunder}")
     total+=poeng

     print(f"Total poeng hittil: {total}")  
     
     if poeng > rekord:
        rekord = poeng
        print("Ny rekord denne runden!") 
     print(f"Din personlige rekord er: {rekord}")      

     spillIgjen = input("Vil du spille igjen? (j/n)").lower()
     if spillIgjen != "j":
        print(f"Den er grei! Velkommen tilbake neste gang! Du fikk totalt {total} poeng på dine spillrunder.")
        break      

kronEllerMynt()        
                         

