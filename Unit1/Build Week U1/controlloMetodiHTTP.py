import requests

# URL di phpMyAdmin su Metasploitable2
url = "http://192.168.1.180/phpMyAdmin"
print(f"Controllo il metodo HTTP per {url}...")

# Lista per memorizzare i metodi HTTP abilitati
metodi = [] 

# Definisci i metodi HTTP da testare
metodiHTTP = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']

response_get = requests.get(url)

for metodo in metodiHTTP:
    try:
        # Invia una richiesta per ciascun metodo
        if metodo == 'OPTIONS':
            # Utilizza il metodo OPTIONS per ottenere i metodi supportati
            response = requests.options(url)  
        else:
            response = requests.request(metodo, url)
        
        # Controlla se il metodo è supportato
        # Considera metodi supportati se la risposta non è un errore
        if response.status_code < 400:  
            metodi.append(metodo)
            print(f"{metodo}: {response_get.status_code} Supportato")
        else:
            print(f"{metodo}: {response_get.status_code} Non supportato")
    except requests.exceptions.RequestException as e:
        print(f"{metodo}: Error - {str(e)}")

print("\nMetodi HTTP supportati:")
print(metodi)
