class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

    def mostrar(self):
        print(f"{self.nombre} - Vida: {self.vida}")

class Guerrero(Personaje):
    def __init__(self):
        super().__init__("Guerrero", 100, 20)


class Dragon(Personaje):
    def __init__(self):
        super().__init__("Dragon", 120, 15)


class Soldado(Personaje):
    def __init__(self):
        super().__init__("Soldado", 100, 20)


class Alien(Personaje):
    def __init__(self):
        super().__init__("Alien", 110, 18)