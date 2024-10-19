class Personaje:

	def __init__(self, nombre, fuerza, inteligencia, defensa,res_magica,vida): 
		self.nombre = nombre 
		self.fuerza = fuerza
		self.inteligencia = inteligencia
		self.defensa = defensa
		self.res_magica = res_magica
		self.vida = vida 


	def atributos(self): 
		print(self.nombre, ":", sep="") 
		print(".Fuerza:" ,self.fuerza) 
		print(".Inteligencia:",self.inteligencia)
		print(".Defensa:",self.defensa)
		print(".Resistencia magica:",self.res_magica) 
		print(".Vida:",self.vida) 

	def subir_nivel(self,fuerza,inteligencia,defensa,res_magica): 
		self.fuerza = self.fuerza + fuerza
		self.inteligencia = self.inteligencia + inteligencia
		self.denfensa = self.defensa + defensa
		self.res_magica = self.res_magica + res_magica

	def esta_vivo(self): 
		return self.vida > 0 

	def morir(self): 
		self.vida = 0
		print(self.nombre, "ha muerto") 

	#Ataque cuerpo a cuerpo, este se basa en la fuerza del mismo 
	def daño(self,enemigo): 
		if self.fuerza >= enemigo.defensa:
			return self.fuerza - enemigo.defensa
		else: 
			return 0 

	def atacar_cuerpo(self, enemigo): 
		daño = self.daño(enemigo)
		enemigo.vida = enemigo.vida - daño 
		print(self.nombre, "ha realizado", daño, "puntos de daños a", enemigo.nombre) 
		if enemigo.esta_vivo(): 
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.morir()
	#------------------------------------------------------------------------------		
	#Ataque con daño magico, este equivale al 50% de la inteligencia del personaje 
	def daño_magico(self,enemigo): 
		if self.inteligencia*0.5 > enemigo.res_magica: 
			return self.inteligencia*0.5 - enemigo.res_magica
		else: 
			return 0

	def ataque_magico(self,enemigo): 
		daño = self.daño_magico(enemigo) 
		enemigo.vida = enemigo.vida - daño
		print(self.nombre, "ha realizado", daño , "puntos de daño magico a", enemigo.nombre) 
		if enemigo.esta_vivo(): 
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.morir()
	#------------------------------------------------------------------------------


class Vampiro(Personaje):
	
	def __init__(self, nombre, fuerza, inteligencia, defensa, vida, res_magica, antiguedad): 
		super().__init__(nombre, fuerza, inteligencia, defensa, vida, res_magica)
		self.antiguedad = antiguedad

	def atributos(self): 
		super().atributos()
		print(".Antiguedad:", self.antiguedad)

	def daño(self, enemigo): 
		plus = self.antiguedad * 0.1
		if (self.fuerza + plus) > enemigo.defensa: 
			return self.fuerza + plus - enemigo.defensa
		else: 
			return 0 

	def daño_magico(self,enemigo): 
		plus = self.antiguedad / 90
		if self.inteligencia*plus > enemigo.res_magica:
			return self.inteligencia*plus - enemigo.res_magica
		else:
			return 0 



def combate(jugador_1,jugador_2): 
	turno = 0 
	import random
	while jugador_1.esta_vivo() and jugador_2.esta_vivo():
		prob = random.randint(0,101)
		if prob <=80: 
			print("\nTurno", turno)
			print(">>> Acción de ", jugador_1.nombre,":", sep="")
			jugador_1.atacar_cuerpo(jugador_2)
			print(">>> Acción de ", jugador_2.nombre,":", sep="")
			jugador_2.atacar_cuerpo(jugador_1)
			turno = turno + 1
		else: 
			print("\nTurno", turno)
			print(">>> Acción de ", jugador_1.nombre,":", sep="")
			jugador_1.ataque_magico(jugador_2)
			print(">>> Acción de ", jugador_2.nombre,":", sep="")
			jugador_2.ataque_magico(jugador_1)
			turno = turno + 1
	if jugador_1.esta_vivo():
		print("\nHa ganado", jugador_1.nombre)
	elif jugador_2.esta_vivo():
		print("\nHa ganado", jugador_2.nombre)
	else:
		print("\nEmpate")
