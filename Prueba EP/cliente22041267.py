# @author: Ignacio Gil Garzón - 22041267

import threading
import sys
import socket
import pickle
import os

class Cliente():

    # 1. Que el todos los clientes que se instancien puedan ingresar mediante el teclado la dirección ip y el puerto, para poder conectarse
	def __init__(self, host= input("Escriba la IP: "), port= input("Escriba el puerto: ")):
		self.sock = socket.socket()
        
        # 2. Que cada vez que un cliente se conecte, este pueda y deba elegir un nickname, que será mostrado cada vez que escriba un texto
		nick = input("Elija un Nickname: ")
		self.sock.connect((str(host), int(port)))
		hilo_mensaje = threading.Thread(target=self.recibir)
		hilo_mensaje.daemon = True
		hilo_mensaje.start()
		print("Hilo con PID",os.getpid())
		print("Hilos activos", threading.active_count())

		self.enviar("Inicio de sesion - " + nick)
		while True:
			msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			if msg != 'Q' :
				self.enviar(nick + ": " + msg)
			else:
				print(" *SALIDA*")
				self.sock.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.sock.recv(32)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))
		data = pickle.dumps(msg)
		if data: 
			print(pickle.loads(data))
            
c = Cliente()