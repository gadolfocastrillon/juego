class Item:
	def __init__(self,codigo_:int,nombre_:str,cantidad_:int, precio_:float):
        """
        Inicializa la clase Objeto con los valores dados.

        Args: 
            codigo(int): identificador único del elemento.
            nombre(str): Nombre del objeto.
            cantidad(int): Cantidad del elemento en el inventario.
            precio(float): Precio del elemento.
            direccion(str)(opcional): Dirección de la imagen del elemento.
        """
        self.codigo = codigo_ 
        self.nombre = nombre_ 
        
        self.cantidad_maxima = 20
        
        if cantidad_<0:
            raise ValueError("La cantidad no puede ser negativa")
        if cantidad_ >self.cantidad_maxima:
        	raise ValueError("La cantidad no puede exceder la cantidad máxima")
        self.cantidad = cantidad_
        if precio_<0:
        	raise ValueError("El precio no puede ser negativo")
		self.precio = precio_
        
       	self.active_to_sell = True #Se puede vender en la tienda
        self.active_to_eat = True  #Se puede comer fuera de combate
        self.active_to_use = True  #Se puede usar en combate.

   	def set_active_to_sell(self,valor):
        """
        Modifica si el objeto se puede vender o no.
        
        Args: 
            valor(bool) : true si el elemento se puede vender, False en caso contrario
        
        """
        if(type(valor) != bool):
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_sell = valor
            
    def set_active_to_eat(self,valor):
        """
        Modifica si el objeto se puede comer o no.
        
        Args: 
            valor(bool) : true si el elemento se puede comer, False en caso contrario
        """
        if(type(valor)!= bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_eat = valor
        
    def set_active_to_use(self,valor): 
        """
        Modifica si el objeto se puede usar o no.

        Args: 
            valor(bool) : true si el elemento se puede usar, False en caso contrario
        """
        if(type(valor) != bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_use = valor

    def mod_car(self,val1,val2,val3):
        if(type(val1)!= bool or type(val2)!=bool or type(val3)!= bool):
            raise ValueError("Los valores ingresados no son validos")
        self.set_active_to_use(val1)
        self.set_active_to_eat(val2)
        self.set_active_to_sell(val3)

    def __iadd__(self,valor):
    	if not isintance(valor,int) or valor <0: 
    		raise ValueError("El valor a aumentar debe ser un entero positivo.")
    	self.cantidad += valor
    	return self
    def __isub__(self,valor):
    	if not isintance(valor,int) or valor <0:
    		raise ValueError("El valor a disminuir debe ser un entero positivo.")
    	self.cantidad = max(0,self.cantidad - valor)
    	return self

    def particionar_cantidad(self,cantidad): #PENDIENTE A REVISIÓN SI DEJAR O NO.
        """
        Convierte la cantidad ingresada en una relacionada a oros platas y bronces.
        

        Args: 
            Cantidad(int): Cantidad a convertir
        returns: 
            Vector(int): Retorna un vector de 3 componentes enteras. 
                         La primer componente es la cantidad de oros.
                         La segunda componente es la cantidad de platas.
                         La tercera componente es la cantidad de bronces.  
        """ 
        valor_oro = 10000
        valor_plata = 100
        oro = cantidad // valor_oro 
        residuo = cantidad % valor_oro 
        plata = residuo // valor_plata
        bronce = residuo % valor_plata
        return [oro,plata,bronce]

    def __str__(self):
    	precios = self.particionar_cantidad(self.precio)
    return (f"{self.nombre}\n"
            f"\tCantidad: {self.cantidad}\n"
            f"\tPrecio: {precios[0]} oros, {precios[1]} platas, {precios[2]} bronces\n")

   def consumir(self):
   	if self.cantidad <=0: 
   		return "No tengo más elementos de eso"

   	self.cantidad -=1
   	return f"La cantidad actual es: {self.cantidad}"


class Inventario:
	def __init__(self):
		self.items = []

	def add_item(self,item):
		self.items.append(item)

	def del_item(self,codigo):
		self.items = [item for item in self.items if item.codigo !=codigo]

	def search_item(self, codigo):
		for item in self.items:
			if item.codigo == codigo:
				return item
		return None

	def show_inventory(self):
		for item in self.items:
			print(item)

if __name__ == '__main__':
	print("HOLA")