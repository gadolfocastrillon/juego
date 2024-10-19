import scripts_personaje as sp 
'''
Nota: 
Kunai
El Kunai es una cuchilla muy utilizada por ser pequeña, es tanto arrojadiza como 
usada en el combate cuerpo a cuerpo, se le podía atar una cuerda. Además servía para 
ferentes fines por su diseño aerodinámico y su facilidad de agarre.

Shuriken
El Shuriken u hoja arrojadiza (popularmente estrella ninja) se utilizaba normalmente, 
no como arma mortal (al menos directamente), sino como arma disuasoria que podía ser 
rojada durante persecuciones, en combate el arma infringía pequeñas cortadas para 
inutilizar al oponente y así dejarle a merced del ninja. Consiste en una hoja de 
metal que podía tener diferentes formas.

Jutte
Es un arma similar a un pequeño tridente que fue utilizada durante muchos siglos por 
la policía japonesa, y aunque no lo parezca es muy peligrosa. Se sujeta con una mano
su saliente se podía usar para trabar la hoja de una espada pero su uso más habitual
era enganchar la ropa del agresor para dominarlo.

Fukiya
Es una cerbatana de bambú , usada para lanzar dardos envenenados.

Kemuridama
Bombas de humo hechas con un huevo,talco y una navaja, que al tener contacto con el 
suelo estallan revelando una cortina de humo dando tiempo al ninja de escapar.

'''
def main(): 
	gus = sp.Ninja("Gus",5,30,100)
	enemigo = sp.Personaje("Guts",5,9,100)
	#gus_inven= sp.Inventario(5,4,3,2,1)
	
	#ataque = gus.fuerza + gus_inven.ku.daño #Comando para realizar ataque con un arma
	gus.inven.atributos() 
	gus.inven.cant_kunai = 10 #agrego 10 kunais al inventario de Gus
	print("")
	gus.ataque_cuerpo(enemigo)
	print("")
	gus.inven.atributos()
	




if __name__ == '__main__':
	main() 


