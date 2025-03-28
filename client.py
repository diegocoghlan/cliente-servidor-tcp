import socket

class Client:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port

    def start(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((self.host,self.port))
                print(f"[*] Conectado a {self.host}:{self.port}")
                while True:
                    message = input("Escribe un mensaje ('DESCONEXION' para salir): ").strip()
                    if not message:
                        print("[!] No puedes enviar mensaje vacio.")
                        continue
                    client.sendall(message.encode('utf-8'))

                    if message == "DESCONEXION":
                        print("[-] Desconectado de servidor...")
                        break
                    response = client.recv(1024).decode('utf-8')
                    print("[<] Servidor:", response)

        except ConnectionRefusedError:
            print("[!] Error: No se pudo conectar al servidor.")
        except Exception as e:
            print(f"[!] Ocurrio un error inesperado: {e}")

if __name__ == "__main__":
    try:
        client = Client()
        client.start()
    except KeyboardInterrupt:
        print("\n[!] Cliente detenido por el usuario. Adios.")
