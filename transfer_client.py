import socket

# Configura el cliente
host = '127.0.0.1'
port = 12345

# Nombre del archivo a transferir
file_name = 'users.txt'

# Crea un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
client_socket.connect((host, port))

# Envía el nombre del archivo al servidor
client_socket.send(file_name.encode())

# Abre el archivo para lectura
with open(file_name, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print(f"Archivo '{file_name}' enviado al servidor")

# Cierra el socket del cliente
client_socket.close()
