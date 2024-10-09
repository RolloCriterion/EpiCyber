print("In questo programma inserendo la data della tua nascita ti dirò il tuo segno zodiacale")
data=int(input("Inserisci il giorno in cui sei nato: "))
mese=input("Inserisci il mese in cui sei nato: ")

if (21 <= data <= 31 and mese == "gennaio") or (1 <= data <= 19 and mese == "febbraio"):
    print("Sei nato il "+str(data)+" "+mese+" e sei del segno dell'Acquario")
elif (20 <= data <= 28 and mese == "febbraio") or (1 <= data <= 20 and mese == "marzo"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Pesci")
elif (21 <= data <= 31 and mese == "marzo") or (1 <= data <= 20 and mese == "aprile"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dell'Ariete")
elif (21 <= data <= 30 and mese == "apile") or (1 <= data <= 20 and mese == "maggio"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Toro")
elif (21 <= data <= 31 and mese == "maggio") or (1 <= data <= 21 and mese == "giugno"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Gemelli")
elif (22 <= data <= 30 and mese == "giugno") or (1 <= data <= 22 and mese == "luglio"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Cancro")
elif (23 <= data <= 31 and mese == "luglio") or (1 <= data <= 23 and mese == "agosto"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Leone")
elif (24 <= data <= 31 and mese == "agosto") or (1 <= data <= 22 and mese == "settembre"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Vergine")
elif (23 <= data <= 30 and mese == "settembre") or (1 <= data <= 22 and mese == "ottobre"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Bilancia")
elif (23 <= data <= 31 and mese == "ottobre") or (1 <= data <= 22 and mese == "novembre"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Scorpione")
elif (23 <= data <= 30 and mese == "novembre") or (1 <= data <= 21 and mese == "dicembre"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Saggittario")
elif (22 <= data <= 31 and mese == "dicembre") or (1 <= data <= 20 and mese == "gennaio"):
    print("Sei nato il "+str(data)+" "+mese+" e sei dei Capricorno")
else:
    print("Sei nato il "+str(data)+" "+mese+"\nLa data inserita non è corretta\nScrivi un numero compreso tra 1 e 31\nScrivi il mese tutto in minuscolo")