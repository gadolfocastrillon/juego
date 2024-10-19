class Jugador: 
	def __init__(self):
		self.dinero = 100 #Dinero inicial
		self.energia = 100 #Energía inicial
		self.reputacion = 50 #Reputación inicial

	def trabajar(self):
		self.dinero += 50 #Gana dinero trabajando
		self.energia -= 20 #Gasta energía trabajando

	def explorar(self):
		self.energia -= 30 #Gasta energía al explorar
		self.reputacion += 10 #Aumenta su reputación al explorar