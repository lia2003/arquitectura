import socket

# Configura el cliente
host = '127.0.0.1'
port = 12345

# Crea un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
client_socket.connect((host, port))

while True:
    message = input("Escribe un mensaje para el servidor: ")
    if message == 'exit':
        break
    client_socket.send(message.encode())  # Envía datos al servidor
    data = client_socket.recv(1024)  # Recibe datos del servidor
    print(f"Respuesta del servidor: {data.decode()}")

# Cierra el socket del cliente
client_socket.close()
