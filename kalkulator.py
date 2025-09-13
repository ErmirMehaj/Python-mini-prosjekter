def kalkulator():
    print("Velkommen til kalkulator-program!")

    tall1 = float(input("Skriv inn første tall:"))
    operator = input("Velg operator (+, -, *, /)")
    tall2 = float(input("Velg ditt neste tall: "))

    if operator == "+":
        resultat = tall1 + tall2
    elif operator == "-":
        resultat = tall1 - tall2
    elif operator == "*":
        resultat = tall1 * tall2
    elif operator == "/":
        if tall2 != 0:
            resultat = tall1 / tall2
        else:
           print("Feil: kan ikke deles på 0")
           return
    else:
        print("Ugyldig operator")
        return
    
    print(f"Resultat: {resultat}")

kalkulator()    

       
 
