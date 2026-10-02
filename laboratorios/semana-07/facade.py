from factories import FantasyFactory, SciFiFactory
from strategies import AtaqueNormal, AtaqueFuerte
from config import GameConfig


class GameFacade:

    def __init__(self):
        self.config = GameConfig()
        self.jugador = None
        self.enemigo = None

    def crear_mundo(self):

        print("Seleccione el mundo:")
        print("1. Fantasia")
        print("2. Ciencia Ficcion")

        opcion = input("Opcion: ")

        if opcion == "1":
            factory = FantasyFactory()

        elif opcion == "2":
            factory = SciFiFactory()

        else:
            print("Opcion no valida")
            return False

        self.jugador = factory.crear_jugador()
        self.enemigo = factory.crear_enemigo()

        return True

    def elegir_ataque(self):

        print()
        print("Seleccione ataque:")
        print("1. Ataque normal")
        print("2. Ataque fuerte")

        opcion = input("Opcion: ")

        if opcion == "1":
            estrategia = AtaqueNormal()

        elif opcion == "2":
            estrategia = AtaqueFuerte()

        else:
            print("Opcion no valida")
            estrategia = AtaqueNormal()

        return estrategia

    def jugar(self):

        print("VIDEOJUEGO POR TURNOS")
        print()

        mundo_creado = self.crear_mundo()

        if not mundo_creado:
            return

        print()
        print("Jugador:")
        self.jugador.mostrar()

        print()
        print("Enemigo:")
        self.enemigo.mostrar()

        turno = 1

        while (
            self.jugador.esta_vivo()
            and self.enemigo.esta_vivo()
            and turno <= self.config.numero_maximo_turnos
        ):

            print()
            print("TURNO", turno)

            estrategia = self.elegir_ataque()

            dano = estrategia.atacar(self.jugador.ataque)

            print(
                self.jugador.nombre,
                "ataca a",
                self.enemigo.nombre
            )

            print("Dano realizado:", dano)

            self.enemigo.recibir_dano(dano)

            if not self.enemigo.esta_vivo():
                break

            print(
                self.enemigo.nombre,
                "ataca a",
                self.jugador.nombre
            )

            self.jugador.recibir_dano(
                self.enemigo.ataque
            )

            print()
            print("Estado del jugador:")
            self.jugador.mostrar()

            print()
            print("Estado del enemigo:")
            self.enemigo.mostrar()

            turno = turno + 1

        self.mostrar_ganador()

    def mostrar_ganador(self):

        print()
        print("RESULTADO FINAL")

        if not self.enemigo.esta_vivo():
            print("Ganador:", self.jugador.nombre)

        elif not self.jugador.esta_vivo():
            print("Ganador:", self.enemigo.nombre)

        else:
            print("Se alcanzo el numero maximo de turnos")