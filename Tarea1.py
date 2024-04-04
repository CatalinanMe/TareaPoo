#Importamos una libreria llamada Random para llamar numeros aleatorios para en este caso el ataque.
import random

#Creamos la clase principal del objeto que sería Personaje y definimos sus atributos.
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self._vida = vida
        self.ataque = ataque
        self.defensa = defensa

#con def creamos el metodo de ataque
    def atacar(self, enemigo):
        # Generamos un valor de ataque aleatorio entre 0 y 80
        ataque_realizado = random.randint(0, 80)
        # Calculamos el daño del ataque teniendo en cuenta la defensa del enemigo
        danio = max(0, ataque_realizado - enemigo.defensa)
        print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {danio} de daño.")
        enemigo._vida -= danio
        if enemigo._vida <= 0:
            print(f"{enemigo.nombre} ha sido derrotado.")
        else:
            print(f"{enemigo.nombre} ahora tiene {enemigo._vida} puntos de vida.")

#Creamos la clase Heroe y Enemigo que se hereda de su clase padre Personaje y hereda mismos atributos ademas de que ahorramos codigo.
class Heroe(Personaje):
 def __init__(self, nombre, vida, ataque, defensa):
    super().__init__(nombre, vida, ataque, defensa)

class Enemigo(Personaje):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)


#metodo de ataque del enemigo
    def atacar(self, personaje):
        # Generamos un valor de ataque aleatorio entre 0 y 80
        ataque_realizado = random.randint(0, 80)
        # Calculamos el daño del ataque teniendo en cuenta la defensa del personaje
        danio = max(0, ataque_realizado - personaje.defensa)
        print(f"{self.nombre} ataca a {personaje.nombre} y le causa {danio} de daño.")
        personaje._vida -= danio
        if personaje._vida <= 0:
            print(f"{personaje.nombre} ha sido derrotado.")
        else:
            print(f"{personaje.nombre} ahora tiene {personaje._vida} puntos de vida.")

# Denominamos el personaje y el enemigo entregando tambien sus atributos entreparentesis
Heroe = Personaje("Heroe", 100, 0-80, 50)
Enemigo = Personaje("Villano", 100, 0-80, 50)

# Simulamos una serie de ataques entre el Heroe y el Villano
while Heroe._vida > 0 and Enemigo._vida > 0:
    # El jugador ataca primero
    Heroe.atacar(Enemigo)
    if Enemigo._vida <= 0:
        break
    # El enemigo responde atacando al jugador
    Enemigo.atacar(Heroe)

#  Finalmente se imprimen los resultados de la pelea.
if Heroe._vida <= 0:
    print("Haz perdido la consciencia... el enemigo ha ganado.")
elif Enemigo._vida <= 0:
   print("Aciertas el ultimo ataque y el enemigo caé debilitado... ¡Ganaste!")