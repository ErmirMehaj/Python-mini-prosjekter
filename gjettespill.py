import random

def gjettespill():
    print("Velkommen til gjettespill. Du skal gjette tallet jeg velger")

    hemmelig_tall = random.randint(1, 5)
    riktig = False

    while not riktig:
        gjett = int(input("Velg et tall mellom 1 og 4: "))
        if gjett == hemmelig_tall:
            print(f"Riktig! Det riktige tallet var: {hemmelig_tall}")
            riktig = True
        else:
            print("Feil. Prøv igjen: ")
gjettespill()            




          
          


      