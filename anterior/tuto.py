class Personaje: 

	def __init__(self, nombre, fuerza, inteligencia, defensa, vida): 
		self.nombre = nombre
		self.__fuerza = fuerza
		self.inteligencia = inteligencia
		self.defensa = defensa
		self.vida = vida

	def atributos(self): 
		print(self.nombre, ":", sep="")
		print(".Fuerza:" , self.__fuerza)
		print(".Inteligencia:", self.inteligencia)
		print(".Defensa:",self.defensa)
		print(".Vida:",self.vida)

	def subir_nivel(self,fuerza,inteligencia,defensa): 
		self.__fuerza = self.__fuerza + fuerza
		self.inteligencia = self.inteligencia + inteligencia
		self.defensa = self.defensa + defensa

	def esta_vivo(self): 
		return self.vida > 0

	def __morir(self): 
		self.vida = 0 
		print(self.nombre, "ha muerto")

	def daño(self,enemigo): 
		return self.__fuerza - enemigo.defensa

	#Calcula el daño hecho a un enemigo y lo modifica en su vida
	def atacar(self,enemigo):  
		daño = self.daño(enemigo)
		enemigo.vida = enemigo.vida - daño 
		print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
		#Analiza la vida del enemigo si esta vivo continua, sino muestra un mensaje
		if enemigo.esta_vivo(): 
			print("La vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.__morir()
	def get_fuerza(self): 
		return self.__fuerza

	def set_fuerza(self,fuerza): 
		if fuerza < 0: 
			print("Error, has introducido un valor negativo") 
		else: 
			self.__fuerza = fuerza 
"""
Para volver los metodos o las variables privadas debemos añadir
__ a cada una, esto hara que el objeto con __ no pueda ser obtenido 
por fuera de la clase
""" 
mi_personaje = Personaje("Gus",10,1,5,100)
mi_enemigo = Personaje("Enemigo",8,5,3,5)
mi_personaje.atacar(mi_enemigo)


#mi_enemigo.atributos()
#print(mi_personaje.daño(mi_enemigo)) #muestra el daño que se le hace a un enemigo
#mi_personaje.atributos()
#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
#mi_personaje.atributos()
#print("El nombre del jugador es", mi_personaje.nombre)
#print("La fuerza del jugador es", mi_personaje.fuerza)
