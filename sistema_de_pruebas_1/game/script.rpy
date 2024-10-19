# Declara los personajes usados en el juego como en el ejemplo:
define e = Character("Eileen")

init python: 
    from gestion_recursos import PlayerResources # Importo la clase PlayerResources
    player_resources = PlayerResources()
    a = 1 

label start:

    scene bg room

    "Welcome to the game!"

    # Ejemplo de ganar dinero
    $ result = player_resources.add_money(50)  # Cambia a 'player_resources'
    "[result]"  # Muestra el mensaje en el juego
    # Ejemplo de gastar dinero
    $ result = player_resources.spend_money(20)
    "[result]"
    # Ejemplo de usar energía
    $ result = player_resources.use_energy(10)
    "[result]"
    # Ejemplo de ganar reputación
    $ result = player_resources.change_reputation(5)
    "[result]"

    # Presenta las líneas del diálogo.
    e "Has creado un nuevo juego Ren'Py."

    # Finaliza el juego:
    return
