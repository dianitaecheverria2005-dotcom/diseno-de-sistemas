# vehiculo -> mueva -> mover

# Auto -> mueve por carretera 
# Bote -> mueve por mar 
# Avion -> mueve por cielo

class ComportamientoMovimiento:
    def mover(self):
        raise NotImplementedError


class MoverPorCarretera(ComportamientoMovimiento):
    def mover(self):
        print("Conduciendo por carretera")


class MoverPorMar(ComportamientoMovimiento):
    def mover(self):
        print("Navegando por mar")


class MoverPorCielo(ComportamientoMovimiento):
    def mover(self):
        print("Volando por cielo")


class Vehiculo:
    def __init__(self, movimiento):
        self.movimiento = movimiento

    def mover(self):
        self.movimiento.mover()


class Auto(Vehiculo):
    def __init__(self):
        mover_c = MoverPorCarretera()
        super().__init__(mover_c)


class Bote(Vehiculo):
    def __init__(self):
        mover_m = MoverPorMar()
        super().__init__(mover_m)


class Avion(Vehiculo):
    def __init__(self):
        mover_c = MoverPorCielo()
        super().__init__(mover_c)

if __name__ == "__main__":
    auto = Auto()
    auto.mover()

    bote = Bote()
    bote.mover()

    avion = Avion()
    avion.mover()