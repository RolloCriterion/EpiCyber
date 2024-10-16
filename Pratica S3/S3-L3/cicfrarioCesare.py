
print("In questo programma utilizzeremo il \ncifrario di Cesare per criptare o decriptare\n una stringa inserita in input")
cryptUncrypt = int(input("Digita\n1 per criptare una stringa\n2 per decriptare la stringa\n>>>>"))
if(cryptUncrypt==1):
    print("Hai scelto di criptare")
    frase=input("Inserisci la stringa che vuoi criptare: ").lower()
    cripted=""
    for char in frase:
            cripted += chr((ord(char) + 3))
    print(f"La stringa criptata ora è uguale: {cripted}")
elif(cryptUncrypt==2):
    print("Hai scelto di decriptare")
    frase=input("Inserisci la stringa che vuoi decriptare: ").lower()
    decripted=""
    for char in frase:
        decripted += chr((ord(char) - 3))
    print(f"La stringa decriptata ora è uguale: {decripted}")
else:
    print("Input non valido")
    
    