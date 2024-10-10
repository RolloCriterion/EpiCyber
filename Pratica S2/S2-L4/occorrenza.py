#In questo programma calcoliamo le occorenze presenti all'interno di una frase data in input
frase = input("Inserisci frase: ")
parole=frase.split()
occorrenze= {}
for parola in parole:
    if parola in occorrenze:
        occorrenze[parola] +=1
    else:
        occorrenze[parola] = 1
print(f"Occorrenze nella frase \"{frase}\" sono:")
for parola, conteggio in occorrenze.items():
    print(f"{parola}: {conteggio}")