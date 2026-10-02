from personajes import Guerrero, Dragon, Soldado, Alien


class PersonajeFactory:

    @staticmethod
    def crear(tipo):

        if tipo == "guerrero":
            return Guerrero()

        elif tipo == "dragon":
            return Dragon()

        elif tipo == "soldado":
            return Soldado()

        elif tipo == "alien":
            return Alien()

        else:
            raise ValueError("Personaje no valido")


class MundoFactory:

    def crear_jugador(self):
        raise NotImplementedError

    def crear_enemigo(self):
        raise NotImplementedError


class FantasyFactory(MundoFactory):

    def crear_jugador(self):
        return PersonajeFactory.crear("guerrero")

    def crear_enemigo(self):
        return PersonajeFactory.crear("dragon")


class SciFiFactory(MundoFactory):

    def crear_jugador(self):
        return PersonajeFactory.crear("soldado")

    def crear_enemigo(self):
        return PersonajeFactory.crear("alien")