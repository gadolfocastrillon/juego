#Programa que contiene las clases para un inventario en el juego


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


#Arma hereda la clase objeto y crea un nuevo objeto llamado arma 
#esta arma tendra un daño base y un costo para ser comprada
class Arma(Objeto): 
	def __init__(self,nombre, desc, dano,costo):
		Objeto.__init__(self,nombre,desc)
		self.dano = dano
		self.costo = costo 

	def atributos(self): 
		print(self.nombre)
		print(self.desc)
		print("Atributos: ")
		print(".Daño: ",self.dano)
		print(".Precio: ",self.costo)

	def dano_cuerpo(self): 
		return self.dano

#EL objeto comida el cual sera utilizado tanto para curarse
#como otros podran ser utilizados para aumentar estadisticas 
#con las chicas. 
#"propiedad" sera la que determinara para que servira el 
#objeto.
class Comida(Objeto): 
	def __init__(self,nombre, desc, propiedad,costo): 
		Objeto.__init__(self,nombre,desc)
		self.propiedad = propiedad
		self.costo = costo 
		
		self.battle_flag = False
		

	def atributos(self):
		print(self.nombre)
		print(self.desc)
		print(".Precio: ",self.costo)
		print(".Propiedad: ", self.propiedad)

class Clothes(Objeto): 
	def __init__(self, name, desc, place): 
		Objeto.__init__(self,nombre,desc)
		self.place = place 
		place = [] 

class Inventory: 
	def __init__(self, money = 10): 
		self.money = money
		self.items = []

	#Mensajes de confirmación
	def get_confirm_msg(self): 
		return "¿usar " + self.name + "?"

	def get_result_msg(self): 
		return self.name + " usado"

	#Añadir item
	def add_item(self,item): 
		self.item.append(item)

	#Remover item
	def remove_item(self,item): 
		self.item.remove(item)

	#Compra de items
	def buy(self,item): 
		if self.money >= item.cost: 
			self.money -=item.cost
			add_item(item)
			return True
		else: 
			return False



#Para realizar los intercambios dentro del juego
def trade(seller, buyer, item): 
	seller.remove(item)
	buyer.buy(item)