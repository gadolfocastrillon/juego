#Crea un nuevo objeto llamado objeto que tiene un nombre y una descripción
class Objeto: 
	def __init__(self,nombre,desc): 
		self.nombre = nombre
		self.desc = desc
		self.marketable_flag = True
		#Si es falso no se puede vender 
		self.usable_falg = True 
		#Si es falso, no puede ser usado normalmente 
		self.battle_flag = True
		#Si es falso, no puede ser usado en batalla 
		self.icon_image = "No cargado"

	def cargar_imagen(self,ruta): 
		self.icon_image = ruta

class Comida(Objeto): 
	def __init__(self,nombre,desc,curacion,costo):
		Objeto.__init__(self,nombre,desc)
		self.curacion = curacion
		self.costo = costo

	def usar_comida(self,personaje):
		if personaje.vida < personaje.vida_maxima: 
			if personaje.vida + self.curacion <= personaje.vida_maxima: 
				personaje.vida = personaje.vida + self.curacion
				return "elemento usado"
			else: 
				personaje.vida = personaje.vida_maxima
				return "elemento usado"
		else: 
			print("Tienes toda la vida al maximo")
			return "elemento no usado"




class Personaje:
	
	def __init__(self, nombre, fuerza,vida): 
		self.nombre = nombre 
		self.fuerza = fuerza
		self.vida = vida
		self.vida_maxima = 100
	"""
	def __init__(self,carac = ["Default",10,10,100]):
		self.nombre = carac[0]
		self.fuerza = carac[1]
		self.defensa = carac[2]
		self.vida = carac[3]
	"""

	def esta_vivo(self): 
		return self.vida > 0 

	def morir(self): 
		self.vida = 0
		print(self.nombre, "ha muerto")

	#Ataque cuerpo a cuerpo, este se basa en la fuerza del mismo 
	def dano(self,enemigo): 
		if self.fuerza >= enemigo.defensa:
			return self.fuerza - enemigo.defensa
		else: 
			return 0 

	def atacar_cuerpo(self, enemigo): 
		dano = self.dano(enemigo)
		enemigo.vida = enemigo.vida - dano 
		print(self.nombre, "ha realizado", dano, "puntos de daños a", enemigo.nombre) 
		if enemigo.esta_vivo(): 
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.morir()
#Arma hereda la clase objeto y crea un nuevo objeto llamado arma 
#esta arma tendra un daño base y un costo para ser comprada
class Arma(Objeto): 
	"""
	def __init__(self,nombre, desc, dano,costo):
		Objeto.__init__(self,nombre,desc)
		self.dano = dano
		self.costo = costo 
	"""
	def __init__(self,carac = ["Default","None",10,100]):
		Objeto.__init__(self,carac[0],carac[1])
		self.dano = carac[2]
		self.costo = carac[3]

	def atributos(self): 
		print(self.nombre)
		print(self.desc)
		print("Atributos: ")
		print(".Daño: ",self.dano)
		print(".Precio: ",self.costo)

	def dano_cuerpo(self): 
		return self.dano

class Personaje_1(Personaje,Arma):
	"""
	def __init__(self,nombre_pj,fuerza,vida,nombre_arma,desc,dano,costo):
		Personaje.__init__(self,nombre_pj,fuerza,vida)
		Arma.__init__(self,nombre_arma,desc,dano,costo)
"""
	#def __init__(self,carac_pj =["Default",10,10,100], carac_arma=["Default","None",10,100]):
	def __init__(self,carac_pj,carac_arma):
		print(carac_pj)
		#Personaje.__init__(["Default",10,10,100])
		#Arma.__init__(carac_arma)
		Personaje.__init__(carac_pj[0],carac_pj[1],100)

	def esta_vivo(self): 
		return self.vida > 0 

	def morir(self): 
		self.vida = 0
		print(self.nombre, "ha muerto")


	def dano(self,enemigo):
		if (self.fuerza + self.dano_cuerpo >= enemigo.defensa):
			return self.fuerza + self.dano_cuerpo - enemigo.defensa
		else: 
			return 0

	def atacar_cuerpo(self,enemigo): 
		dano = self.dano(enemigo)
		enemigo.vida = enemigo.vida - dano 
		print(self.nombre_pj, " ha realizado ", dano, " puntos de daño a ",enemigo.nombre)
		if enemigo.esta_vivo(): 
			print("Vida de ", enemigo.nombre, " es ", enemigo.vida)
		else: 
			enemigo.morir()



class Inventario:
	def __init__(self,elemento): 
		self.elemento = elemento
		self.inventario = []

	def buy(self,elemento): 
		for i in range(len(self.inventario)): 
			if self.inventario[i] == 0: 
				self.inventario[i] = elemento
				break
		return 0

	def busqueda_objeto(self,elemento):
		for x in range(len(self.inventario)):
			if lista[x] == elemento:
				return True
			else: 
				return False

