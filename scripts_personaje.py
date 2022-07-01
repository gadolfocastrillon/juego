class Personaje:
	def __init__(self, nombre,fuerza,defensa,vida): 
		self.nombre = nombre 
		self.fuerza = fuerza 
		self.defensa = defensa
		self.vida = vida

	def atributos(self): 
		print(" ",self.nombre, ":", sep="")
		print(".Fuerza:",self.fuerza) 
		print(".Defensa:",self.defensa)
		print(".Vida:",self.vida)

	def subir_nivel(self,fuerza,defensa,vida): 
		self.fuerza = self.fuerza + fuerza 
		self.defensa = self.defensa + defensa 
		self.vida = self.vida + vida 

	def esta_vivo(self): 
		return self.vida>0 

	def morir(self): 
		self.vida = 0 
		print(self.nombre, "ha muerto") 

	def dano_cuerpo(self, enemigo): 
		if self.fuerza > enemigo.defensa: 
			return self.fuerza - enemigo.defensa
		else: 
			return 0

	def ataque_cuerpo(self,enemigo): 
		dano = self.dano_cuerpo(enemigo)
		enemigo.vida = enemigo.vida - dano 
		print(self.nombre, "ha realizado", dano, "puntos de daño a", enemigo.nombre)
		if enemigo.esta_vivo(): 
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.morir()


class Ninja(Personaje):

	def __init__(self, nombre, fuerza, defensa, vida): 
		super().__init__(nombre,fuerza,defensa,vida)
		self.inven= Inventario(0,4,3,2,1)
		#Le doy unos parametros al Ninja con unos valores por defecto
		#Para cambiar los parametros dentro de main se utiliza 
		#nombre.invent.cant_kunai o el arma que se desee cambiar

	def dano_cuerpo(self,enemigo): 
		#Verifica la cantidad de Kunais, si es mayor que cero ataca con esto
		#sino ataca solo con la fuerza del puño
		if self.inven.cant_kunai > 0: 
			ataque = self.fuerza + self.inven.ku.dano
		else: 
			ataque = self.fuerza

		if ataque > enemigo.defensa: 
			print(self.nombre)
			self.inven.cant_kunai = self.inven.cant_kunai - 1
			return ataque - enemigo.defensa
		else: 
			return 0

	def ataque_cuerpo(self,enemigo): 
		dano = self.dano_cuerpo(enemigo)
		enemigo.vida = enemigo.vida - dano 
		print(self.nombre, "ha realizado", dano, "puntos de daño a", enemigo.nombre)
		if enemigo.esta_vivo(): 
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else: 
			enemigo.morir()





'''
Esta clase se encarga de crear cada una de las habilidades definiendo: el nombre de
de la habilidad, el daño de esta y el consumo de mana que tiene.
'''
class Habilidad: 

	def __init__(self, h_nombre, h_dano, gasto): 
		self.h_nombre = nombre 
		self.h_dano = h_dano 
		self.gasto = gasto

	def atributos(self): 
		print(self.nombre)
		print(".Daño:",self.h_dano)
		print(".Gasto de mana:",self.gasto)

'''
Esta clase se encarga de identificar el tipo de arma con el daño que hace esta. 
'''
class Arma: 

	def __init__(self, nombre, dano): 
		self.nombre = nombre 
		self.dano = dano

	def atributos(self): 
		print(self.nombre) 
		print(".Daño:", self.dano)

	def daño_cuerpo(self): 
		return self.dano

'''
La clase inventario se encarga de almacenar la cantidad de armas en el inventario 
del persojane y a su vez tiene atributos que permites indenficar y mostrar cuanta
cantidad de estas tiene en su inventario
'''
class Inventario: 

	def __init__(self, cant_kunai, cant_shuriken, cant_jutte, cant_fukiya, cant_kemuridama): 
		self.cant_kunai = cant_kunai
		self.cant_shuriken = cant_shuriken
		self.cant_jutte = cant_jutte
		self.cant_fukiya = cant_fukiya
		self.cant_kemuridama = cant_kemuridama
		"""
		Definición de las armas: se definen las 5 tipos de armas con la clase Armas, 
		su nombre y la cantidad de daño
		"""
		self.ku = Arma("Kunai",5)
		self.shu = Arma("Shuriken",7)
		self.ju = Arma("Jutte",9)
		self.fu = Arma("Fukiya",8)
		self.ke = Arma("Kemuridama",6)

	#Imprime el inventario en general
	def atributos(self): 
		print("Inventario armas cuerpo a cuerpo") 
		print(".Kunais:",self.cant_kunai)
		print(".Shurikens:",self.cant_shuriken)
		print(".Juttes:",self.cant_jutte)
		print(".Fukiyas:",self.cant_fukiya)
		print(".Kemuridamas:",self.cant_kemuridama)

	#Retorna un arreglo con varios mayores o iguales a cero 
	#Cuando es cero implica que tenemos 0 cantidad de este
	def i_arreglo(self): 
		return [int(self.cant_kunai), int(self.cant_shuriken), int(self.cant_jutte), int(self.cant_fukiya), int(self.cant_kemuridama)]

	#Genera un menú de opciones para imprimir el inventario 
	def print_invent_pj(self): 
		invent = self.i_arreglo()
		
		salir = True
		#Bucle para seguir mostrando las opciones del inventario
		while salir == True: 

			#Para que el usuario pueda observar cuanta cantidad tiene en su inventario
			a = int(input("""
							 Presione 1 para kunais \n 
							 Presione 2 para shurikens \n
							 Presione 3 para juttes \n 
							 Presione 4 para fukiyas \n 
							 Presione 5 para kemuridamas\n"""))

			if a == 1:	
				if invent[0] > 0: 
					print("Tienes:" ,invent[0]," kunais")
					b = input("¿mostrar info de kunai? (y/n)")
					if b == 'y' or b == 'Y': 	
						self.ku.atributos()
					else:
						pass

				elif invent[0] == 0: 
					print("No tienes kunais")
				else: 
					print("Error, valor númerico no valido")
			if a==2: 
				if invent[1] > 0: 
					print("Tienes:" ,invent[1]," shurikens")
					b = input("¿mostrar info de shuriken? (y/n)")
					if b == 'y' or b == 'Y': 
						self.shu.atributos()
					else:
						pass
									 
				elif invent[1] == 0: 
					print("No tienes shurikens")
				else: 
					print("Error, valor númerico no valido")

			if a==3: 
				if invent[2] > 0: 
					print("Tienes:" ,invent[2]," juttes")
					b = input("¿mostrar info de jutte? (y/n)")
					if b == 'y' or b == 'Y': 
						self.ju.atributos()
					else:
						pass
									 
				elif invent[2] == 0: 
					print("No tienes juttes")
				else: 
					print("Error, valor númerico no valido")

			if a==4: 
				if invent[3] > 0: 
					print("Tienes:" ,invent[3]," fukiyas")
					b = input("¿mostrar info de fukiya? (y/n)")
					if b == 'y' or b == 'Y': 
						self.fu.atributos()
					else:
						pass
									 
				elif invent[3] == 0: 
					print("No tienes fukiyas")
				else: 
					print("Error, valor númerico no valido")

			if a==5: 
				if invent[4] > 0: 
					print("Tienes:" ,invent[4]," kemuridamas")
					b = input("¿mostrar info de kemuridamas? (y/n)")
					if b == 'y' or b == 'Y':
						self.ke.atributos()
					else:
						pass 
									 
				elif invent[4] == 0: 
					print("No tienes kemuridamas")
				else: 
					print("Error, valor númerico no valido")
			sal = input("¿Desea salir? (y/n)")
			if sal == "y" or sal == "Y": 
				salir = False 