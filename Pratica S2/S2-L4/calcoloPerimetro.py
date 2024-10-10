import math

print("In questo programma possiamo calcolare il perimetro del\nQuadrato\nCerchio\nRettangolo\n")
scelta = int(input("Scrivi per calcolare il perimetro\n1 Quadrato\n2 Cerchio\n3 Rettangolo\n>>>>>"))
if scelta == 1:
    print("Hai scelto di calcolare il perimetro del Quadrato\n")
    lato=int(input("Inserisci quanto e' lungo il lato: "))
    perimetro=lato*4
    print(f"Il perimetro del Quadrato con lato {lato} e' {perimetro}")
elif scelta == 2:
    print("Hai scelto di calcolare il perimetro del Cerchio\n")
    raggio=float(input("Inserisci quanto e' lungo il raggio: "))
    perimetro=2*math.pi*raggio
    print(f"Il perimetro del Cerchio con raggio {raggio} e' {perimetro}")
elif scelta == 3:
    print("Hai scelto di calcolare il perimetro del Rettangolo\n")
    lato=float(input("Inserisci quanto e' lungo il lato: "))
    altezza=float(input("Inserisci quanto e' lungo l'altezza: "))
    perimetro=(lato*2)+(altezza*2)
    print(f"Il perimetro del Rettangolo con lato {lato} e altezza{altezza} e' {perimetro}")
else:
    print("Non hai inserito il carattere corretto")
    