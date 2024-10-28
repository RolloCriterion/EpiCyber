import datetime

#Una possibile fonte di bug è non sapere che input dobbiamo dare per rendere lo script piu leggibile
print("Ciao sono AV puoi chiedermi una delle seguenti domande:\nQual è la data di oggi?\nChe ore sono?\nCome ti chiami?\nEsci < per chiudere il programma")

def assistente_virtuale(comando):
    if comando == "qual è la data di oggi?":
        #In questo bug non esiste la funzione datetoday() nella libreria datetime
        #oggi = datetime.datetoday()
        oggi = datetime.datetime.now()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        #Per una migliore leggibilità del programma, nel caso sia stata inserita una domanda sbagliata ristampiamo le domande 
        risposta = "Non ho capito la tua domanda.\nProva a scrivere una delle seguenti domande:\nQual è la data di oggi?\nChe ore sono?\nCome ti chiami?\nOppure Esci per chiudere il programma"
    return risposta
#In questo bug mancano i : che danno inizio al ciclo while
#while True
while True:
    #Possiamo considerare come prevenzione di eventuali bug di utilizzare .lower() per permettere di analizzare sempre una stringa nello stesso formato
    comando_utente = input("Cosa vuoi sapere? ").lower()
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))
        