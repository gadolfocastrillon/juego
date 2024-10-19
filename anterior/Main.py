
from habilidades import *
from clases import *
manzana_desc= "Cura al personaje una cantidad de 5 puntos de vida"

def main(): 

	manzana = Comida("Manzana",manzana_desc,5,10)
	p1 = Personaje("Gus",10,100)
	print(p1.vida)
	print(manzana.usar_comida(p1))
	print(p1.vida)
	#nombre, fuerza, inteligencia, defensa,res_magica,vida
	#personaje_1 = Personaje("Gus", 10, 50, 40, 30, 100)
	#personaje_2 = Vampiro("Dracula",6, 40, 40, 50, 100, 90)
	#personaje_1.atributos()
	#personaje_2.atributos()
	#combate(personaje_1, personaje_2)
	
if __name__=='__main__':
	main()

''' 
Probabilidad de ataque 
Cada personaje va a tener una presición, esto es algo intrinseco de cada uno
para esto escoges un valor aleatorio entre 0 y 100. 
Si el personaje tiene una presicion de 60%, entonces si el numero
esta por debajo de 60, ataca, sino no ataca
''' 