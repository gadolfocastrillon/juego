import inventario as i

#Descripciones de los objetos
k_desc='''
Arma ninja...
'''
s_desc='''
Sin descripción
'''
#Creación de los objetos
k_obj = i.Item("kunai",k_desc,12)
s_obj = i.Item("Shuriken",s_desc,15)

k_obj.cargar_imagen("/imagenes/kunai.png")
s_obj.cargar_imagen("/imagenes/shuriken.png")

#--------------------------------------------

