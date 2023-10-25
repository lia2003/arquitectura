import socket

# Configura el servidor
host = '127.0.0.1'
port = 12345

# Crea un socket del servidor
# AF_INET: Indica que se utilizará el protocolo de Internet versión 4 (IPv4)
# SOCK_STREAM: se usa para crear sockets de flujo, los cuales proporcionan una 
# comunicación confiable y bidireccional (protocolo TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar (unir) el socket al host y puerto
server_socket.bind((host, port))

# Escucha hasta 5 conexiones entrantes
server_socket.listen(5)

print(f"Servidor de eco escuchando en {host}:{port}")

while True:
    # Espera a que un cliente se conecte
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    data = client_socket.recv(1024)  # Recibe datos del cliente. Como maximo 1024 bytes
    if not data:
        break

    print(f"Recibido: {data.decode()}")

    # Envia los mismos datos de vuelta al cliente
    client_socket.send(data)

    # Cierra la conexión con el cliente
    client_socket.close()

# Cierra el socket del servidor
server_socket.close()
