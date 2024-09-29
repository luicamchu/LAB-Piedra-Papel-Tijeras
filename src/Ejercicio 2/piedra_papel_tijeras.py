#added ejercicio 1 apartado a
import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

#added ejercicio 2 apartado b
def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")    
    return eleccion_usuario

#added ejercicio 2 apartado b
def usuario_decide_jugada_2():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

#added ejercicio 1 apartado d
def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"

#added ejercicio 2 apartado a
def jugar():
    print("Bienvenido al Juego Piedra Papel y Tijera.")
    eleccion_ordenador:str = str(ordenador_decide_jugada())
    print("El Ordenador eligio: " + eleccion_ordenador)
    eleccion_usuario:str = str(usuario_decide_jugada_2())
    resultado:str = determina_ganador(eleccion_usuario, eleccion_ordenador)
    print("Resultado: " + str(resultado))



if __name__ == "__main__":
    jugar()