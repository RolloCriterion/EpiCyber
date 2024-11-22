import bcrypt

# Leggi il file contenente gli hash
def load_hashes(file_path):
    with open(file_path, 'r') as file:
        hashes = [line.strip().encode() for line in file.readlines()]
    return hashes

# Leggi il file contenente la wordlist
def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        passwords = [line.strip().encode() for line in file.readlines()]
    return passwords

# Confronta ogni hash con tutte le password
def crack_hashes(hashes, wordlist, progress_interval=100):
    cracked = {}  # Dizionario per salvare hash -> password trovata
    attempt_counter = 0

    for hash in hashes:
        print(f"[!] Inizio cracking per hash: {hash.decode()}")
        for password in wordlist:
            attempt_counter += 1
            
            # Mostra i progressi ogni N tentativi
            if attempt_counter % progress_interval == 0:
                print(f"[INFO] Tentativi eseguiti finora: {attempt_counter}")

            if bcrypt.checkpw(password, hash):
                cracked[hash.decode()] = password.decode()
                print(f"[+] Password trovata per hash {hash.decode()}: {password.decode()}")
                break  # Passa al prossimo hash dopo aver trovato la password
        else:
            print(f"[-] Nessuna password trovata per hash {hash.decode()}")
    
    print(f"[!] Tentativi totali eseguiti: {attempt_counter}")
    return cracked

if __name__ == "__main__":
    # File con gli hash (uno per riga)
    hashes_file = "hashPass.txt"
    
    # File con la wordlist delle password
    wordlist_file = "/usr/share/seclists/Passwords/darkweb2017-top10000.txt"
    
    # Carica gli hash e la wordlist
    hashes = load_hashes(hashes_file)
    wordlist = load_wordlist(wordlist_file)
    
    # Cracka gli hash
    cracked_hashes = crack_hashes(hashes, wordlist, progress_interval=100)
    
    # Salva i risultati in un file
    with open("cracked_passwords.txt", "w") as output_file:
        for hash, password in cracked_hashes.items():
            output_file.write(f"{hash}: {password}\n")
    
    print("\n[!] Operazione completata. Risultati salvati in 'cracked_passwords.txt'.")
