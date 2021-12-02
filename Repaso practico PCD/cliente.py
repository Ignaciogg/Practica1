
import threading
import sys
import socket
import pickle
import os

class Cliente():

    # 1. AL INICIAR UN CLIENTE LE PEDIMOS LOS DATOS DEL SERVER COMO LA IP Y EL PUERTO Y QUE ESCOGA UN NICKNAME
	def __init__(self, host= input("Introduce la IP del server: "), port= input("Introduce el puerto del server: "),nickname = input("Introduce un Nickname: ")):
		self.sock = socket.socket()
        
    
    
	# 2. Establecemos conexión con el servidor	
		self.sock.connect((str(host), int(port)))
		hilo_mensaje = threading.Thread(target=self.recibir)
		hilo_mensaje.daemon = True
		hilo_mensaje.start()
		print("Hilo con PID",os.getpid())
		print("Hilos activos", threading.active_count())
        
    # Enviamos al servidor quien ha iniciado sesion    
		self.enviar("Inicio de sesion - " + nickname)
		while True:
            
            #Mandamos el texto del cliente
			msg = input('\nEscriba texto  ** Enviar = ENTER ** Abandonar Chat = Q \n')
			if msg != 'Q' :
				self.enviar(nickname + ": " + msg)
				#self.enviar_chat(msg)
			else:
             #Si el cliente pulsa Q, salimos
				print(" *SALIDA*")
				self.sock.close()
				sys.exit()

    # 3. Funcion para recibir mensajes
	def recibir(self):
		while True:
			try:
                #Recibimos mensajes
				data = self.sock.recv(32)
				if data:
                     #Los mostramos por pantalla
					print(pickle.loads(data))
			except:
				pass

    #Funcion para enviar mensajes
	def enviar(self, msg):
        #Enviamos mensaje
		self.sock.send(pickle.dumps(msg))
		data = pickle.dumps(msg)
		if data: 
			print(pickle.loads(data))
            
	'''def enviar_chat(self, msg):
		firebaseConfig ={
			"apiKey": "AIzaSyDaQumGn9B8RRO85Nrtiy6jSLV6vdyCVpA",
			"authDomain": "hola-mundo-7e708.firebaseapp.com",
			"databaseURL": "https://hola-mundo-7e708-default-rtdb.europe-west1.firebasedatabase.app",
			"projectId": "hola-mundo-7e708",
			"storageBucket": "hola-mundo-7e708.appspot.com",
			"messagingSenderId": "784229501997",
			"appId": "1:784229501997:web:a51511657da1d8aa377ca4",
			"measurementId": "G-FC3K278N6Z"
			}
		firebase = pb.initialize_app(firebaseConfig)
		auth = firebase.auth()
		mail = "feernandomemdez@gmail.com"
		passwd="nenuco"
		user = auth.create_user_with_email_and_password(mail,passwd)
		ddbb=firebase.database()
		ddbb.child('users/22033190/chat').push(msg)'''
start = Cliente()