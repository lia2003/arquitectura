import socket

# Configura el servidor
host = '127.0.0.1'
port = 12345

# Crea un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlaza el socket al host y puerto
server_socket.bind((host, port))

# Escucha hasta 5 conexiones entrantes
server_socket.listen(5)

print(f"Servidor de transferencia de archivos escuchando en {host}:{port}")

while True:
    # Espera a que un cliente se conecte
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    # Recibe el nombre del archivo
    file_name = client_socket.recv(1024).decode()

    # Abre el archivo para escritura
    with open(file_name, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"Archivo '{file_name}' recibido y guardado")

    # Cierra la conexión con el cliente
    client_socket.close()

# Cierra el socket del servidor
server_socket.close()
