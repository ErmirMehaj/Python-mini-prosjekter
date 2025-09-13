import random

def navngenerator():
    print("Velkommen til navngenerator! Jeg skal generere et kult navn for deg!")

    ord = ["Dark", "Crazy", "Funny", "Silent", "Cool", "Mode"]
    fornavn = input("Skriv inn fornavnet ditt: ")
    generer = random.choice(ord)
    tallgenerator = random.randint(1, 2)
    resultat = f"{generer}{fornavn}{tallgenerator}"

    print(f"Navnet ditt nå: {resultat}")
navngenerator()    