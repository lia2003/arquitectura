import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    # socket() ---> nos permite crear un objeto de tipo socket
    # AF_INET ---> nos indica que se utilizarán direcciones IPv4
    # SOCK_STREAM ---> nos indica que se utilizará el protocolo TCP

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    # connect() ---> nos permite enviar una solicitud de conexión hacia el servidor
    socket_client.connect(server_address)

    # TX
 
    #El mensaje de entrada lo puse por input
    msg_TX = input ("Ingrese su perición, a) promedio edades, b)número pacientes enfermos, c) número de pacientes sanos\n")
    # encode('utf-8') ---> Nos permite enviar la información en formato de B
    data_TX = msg_TX.encode('utf-8')
    socket_client.sendall(data_TX)

    # RX
    data_RX = socket_client.recv(CLIENT_BUFFER)
    data=data_RX.decode('utf-8')
    #Acá imprimo para que se note que si devuelve lo esperado:
    print(data)
    #Dependiendo de qué solicitó imprime uno u otro
    match data:
        case "a":
            with open("datos.csv", "a") as f:
                f.write(f"Promedio de edades de los pacientes,{data}\n")
        case "b":
            with open("datos.csv", "a") as f:
                f.write(f"Número de pacientes enfermos,{data}\n")
        case "c":
            with open("datos.csv", "a") as f:
                f.write(f"Número de pacientes sanos,{data}\n")
        case _:
            ...


    print("Cliente cerrando la conexión...")
    socket_client.close()