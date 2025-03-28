import socket

class Server:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.server.settimeout(1.0)
        print(f"[*] Servidor escuchando en {self.host}:{self.port}")

    def start(self):
        try:
            while True:
                try:
                    conn, addr = self.server.accept()
                    print(f"[+] Conexion aceptada desde {addr}")
                    self.handle_client(conn, addr)
                except KeyboardInterrupt:
                    print("\n[!] Servidor detenido manualmente")
                    break
                except socket.timeout:
                    continue
        except Exception as e:
            print(f"\n[!] Error: {e}")
        finally:
            self.server.close()
            print("[*] Socket cerrado.")

    def handle_client(self, conn, addr):
        conn.settimeout(1.0)
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"[!] Cliente {addr} desconectado.")
                    break
                message = data.decode('utf-8').strip()
                print(f"[>] Cliente: {message}")

                if message == "DESCONEXION":
                    print(f"[-] Cliente {addr} cerro sesion.")
                    break
                else:
                    response = message.upper()
                    conn.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"[!] Error con cliente {addr}: {e}")
        finally:
            conn.close()
            print(f"[*] Conexión con {addr} cerrada.")


if __name__ == "__main__":
    try:
        server = Server()
        server.start()
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido por el usuario. Adios.")
