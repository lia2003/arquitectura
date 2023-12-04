#cliente

import socket

# Configura el cliente
host = '127.0.0.1'
port = 12345

# Crea un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
client_socket.connect((host, port))

while True:
    numero = input("Numero del que se requiere calcular el factorial: ")
    if numero:
        client_socket.send(numero.encode('utf-8'))  # Envía numero al servidor
        factorial = client_socket.recv(1024)  # Recibe factorial del servidor
        print(f"El factorial de {numero} es : {factorial.decode('utf-8')}")
    else:
        break

# Cierra el socket del cliente
client_socket.close()