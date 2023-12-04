import socket

host = "127.0.0.1"
port = 5000
size = 2048

if __name__ == '__main__':
	print("Conectandome a servidor....")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	print("¡Conectado!")

	while True:
		print("Tipee lo que quieres enviar:")
		cmd = input()
		if cmd == 'start':
			# Este es el comando para iniciar el juego.
			s.send(b'start')
			word_received = s.recv(1024)
			print("Mensaje recibido: ", word_received)
			print("Tienes 5 oportunidades!")
		elif cmd == 'stop':
			print("Desconectando del servidor. Terminamos el juego")
			s.close()
			break
		else:
			# Asumimos que tipeaste 1 caracter tratando de adivinar la palabra. Así que lo enviamos
			s.send(cmd.encode())
			word_received = s.recv(1024)
			print("Mensaje recibido: " + '*' * len(word_received.decode('utf-8')))