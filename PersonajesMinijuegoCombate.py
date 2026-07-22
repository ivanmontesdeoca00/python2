
### Creen una clase Personaje con los atributos: nombre, vida_actual, vida_maxima, ataque_base y clase_personaje ("guerrero", "mago" o "arquero").
### Creen las siguientes funciones externas:
### crear_personaje(...): Retorna la instancia del personaje.
### recibir_dano(personaje, cantidad): Resta la cantidad a la vida_actual.
### curar(personaje, cantidad): Aumenta la vida_actual.
### ejecutar_ataque(atacante, defensor): Calcula cuánto daño hace el atacante al defensor. Si la clase del atacante es "guerrero", suma +5 de daño físico. Si es "mago", duplica el ataque pero gasta maná. Si es "arquero", inflige daño normal.
### El problema que provocará: La vida_actual terminará siendo mayor que la vida_maxima o negativa (sin límites), y el cálculo de ataques requerirá condicionales anidados para evaluar las clases del atacante y defensor. 
##NOTA PERSONAL: LO QUE NO ANOTO NO ES QUE NO LO SEPA, AL CONTRARIO, ME PARECE MUY INTUITIVO Y ES AL CUETE ANOTARLO.

## Creo personaje con sus respectivos atributos

class Personaje:
    def __init__(self, nombre, vida_maxima, ataque_de_base, clase_pj, mana_actual=50):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima #Esto es para que comience con la vida al maximo
        self.ataque_de_base = ataque_de_base
        self.clase_pj = clase_pj.lower()
        self.mana_actual = mana_actual #aca añado esto para soportar la logica de la raza magica

##FUNCIONES EXTERNAS

def crear_pj(nombre, vida_maxima, ataque_de_base, clase_pj):
    #Aca retorno una nueva "forma" de personaje
    return Personaje(nombre, vida_maxima, ataque_de_base, clase_pj)

def recibir_dano(personaje, cantidad):
    personaje.vida_actual -= cantidad
    print(f"{personaje.nombre} recibe {cantidad} de daño de ataque. Su vida actual es: {personaje.vida_actual}/{personaje.vida_maxima}")

def curar(personaje, cantidad):
    personaje.vida_actual += cantidad
    
    print(f"{personaje.nombre} se cura {cantidad} de vida. Su vida actual es: {personaje.vida_actual}/{personaje.vida_maxima}")

def ejecutar_ataque(atacante, defensor):
    dano_final = 0
    ##Ataque del guerrero
    if atacante.clase_pj == "war":
        if defensor.clase_pj == "war":
            dano_final = atacante.ataque_de_base + 5
        elif defensor.clase_pj == "mage":
            dano_final = atacante.ataque_de_base + 5
        elif defensor.clase_pj == "archer":
            dano_final = atacante.ataque_de_base + 5
        else:
            dano_final = atacante.ataque_de_base + 5
    ## Ataque del mago
    elif atacante.clase_pj == "mage":
        if defensor.clase_pj == "war":
            dano_final = atacante.ataque_de_base * 2
        elif defensor.clase_pj == "mage":
            dano_final = atacante.ataque_de_base * 2
        elif defensor.clase_pj == "archer":
            dano_final = atacante.ataque_de_base * 2
        else:
            dano_final = atacante.ataque_de_base * 2

    ##Ataque del arquero
    elif atacante.clase_pj == "archer":
        if defensor.clase_pj == "war":
            dano_final = atacante.ataque_de_base
        elif defensor.clase_pj == "mage":
            dano_final = atacante.ataque_de_base
        elif defensor.clase_pj == "archer":
            dano_final = atacante.ataque_de_base
        else:
            dano_final = atacante.ataque_de_base
    else:
        dano_final = atacante.ataque_de_base
    
    print(f"{atacante.nombre} ({atacante.clase_pj}) ataca a {defensor.nombre} ({defensor.clase_pj}) e inflige {dano_final} de daño.")

    recibir_dano(defensor, dano_final)

    return dano_final

if __name__ == "__main__":
    print("--- INICIANDO EL JUEGO DE ROL ---")
    
    # Creo los personajes  con las funciones que me pide
    war = crear_pj("Ivan", 100, 15, "guerrero")
    mage = crear_pj("Fabio", 70, 20, "mago")
    archer = crear_pj("Patricio Estrella", 80, 18, "arquero")
    
    print(f"\nPersonajes listos: {war.nombre} (war), {mage.nombre} (mage), {archer.nombre} (archer)\n")
    
    # Aca voy a simular un par de rondas de combate bien figuradas

    print("--- Ronda 1 ---")
    ejecutar_ataque(war, mage)
    print("\n--- Ronda 2 ---")
    ejecutar_ataque(mage, war)
    print("\n--- Ronda 3 ---")
    ejecutar_ataque(archer, war)
    print("\n--- Curación de prueba ---")
    curar(mage, 25)