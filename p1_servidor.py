# Servidor
import socket

# Configura el servidor
host = '127.0.0.1'
port = 12345

# Crea un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar (unir) el socket al host y puerto
server_socket.bind((host, port))

# Escucha hasta 5 conexiones entrantes
server_socket.listen(5)

print(f"Servidor escuchando en {host}:{port}")

while True:
    # Espera a que un cliente se conecte
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")
    while True:
        n = client_socket.recv(1024)  #recibe el numero n, como maximo 1024 bytes
        if n:
            #decodificamos el numero enviado por el cliente y lo guardamos en la variable numero
            numero = int (n.decode('utf-8'))

            #factorial de un numero n
            def factorial(numero):
                resultado = 1
                for i in range(1, numero + 1):
                    resultado= resultado*i
                return resultado

            f_numero= factorial(numero)

            #convertimos el resultado a un string
            resultado1= str(f_numero)

            # codifica el resultado
            rfactorial= resultado1.encode('utf-8')

            # envia el resultado
            client_socket.send(rfactorial)
        else:
            break

