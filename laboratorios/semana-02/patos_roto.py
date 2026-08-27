# Semana 2 - sesion 1
# Diana Echeverria (00335927)

# Semana 2 - sesion 1
# Diana Echeverria (00335927)

class ComportamientoVuelo():
    def volar(self):
        raise NotImplementedError


class VuelaConAlas(ComportamientoVuelo):
    def volar(self):
        print("Vuela con alas")


class NoVuela(ComportamientoVuelo):
    def volar(self):
        print("No vuela.")


class ComportamientoGraznar:
    def graznar(self):
        raise NotImplementedError


class GraznidoNormal(ComportamientoGraznar):
    def graznar(self):
        print("Cuack!")


class GraznidoDeGoma(ComportamientoGraznar):
    def graznar(self):
        print("Chirrido de goma")


class Pato:
    def __init__(self, comportamiento_vuelo, comportamiento_graznido):
        self.comportamiento_graznido = comportamiento_graznido
        self.comportamiento_vuelo = comportamiento_vuelo

    def nadar(self):
        print("Nadando.")

    def graznar(self):
        self.comportamiento_graznido.graznar()

    def volar(self):
        self.comportamiento_vuelo.volar()


class PatoSalvaje(Pato):
    def __init__(self):
        vuela_alas = VuelaConAlas()
        graznido_n = GraznidoNormal()
        super().__init__(vuela_alas, graznido_n)


class PatoDeGoma(Pato):
    def __init__(self):
        no_vuela = NoVuela()
        graznido_g = GraznidoDeGoma()
        super().__init__(no_vuela, graznido_g)


if __name__ == "__main__":
    salvaje = PatoSalvaje()
    salvaje.nadar()
    salvaje.graznar()
    salvaje.volar()

    print()

    goma = PatoDeGoma()
    goma.nadar()
    goma.graznar()
    goma.volar()