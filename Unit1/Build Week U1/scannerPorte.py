import socket

# Indirizzo IP della macchina Metasploitable2
ip = "192.168.1.180"  

# Richiede la porta di partenza
portaInizio = int(input("Inserisci la porta dal quale vuoi iniziare: "))  

# Richiede la porta di fine
portaFine = int(input("Inserisci la porta nel quale fermarsi: ")) 

# Crea un range di porte da scansionare
rangePorte = range(portaInizio, portaFine + 1)

# Lista per memorizzare le porte aperte
porteAperte = []  
print(f"Scan dell indirizzo {ip} da porta {portaInizio} a porta {portaFine}...")

for porta in rangePorte:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    	# Imposta il timeout per la connessione a 1 secondo
        sock.settimeout(1)  
        # Prova a connettersi alla porta
        result = sock.connect_ex((ip, porta)) 
        # Se la connessione ha successo, la porta è aperta 
        if result == 0:  
            porteAperte.append(porta)
            #print(f"Port {porta}: Open")
        # Se la connessione fallisce, la porta è chiusa
        #else:  
            #print(f"Port {porta}: Closed")

print("\nPorte aperte:")
print(porteAperte)
