lass Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class EquipoOficial:
    def __init__(self, nombre):
        self.nombre = nombre


class ReservaRegular:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante

    def confirmar(self):
        return "Reserva regular confirmada para " + self.solicitante.nombre


class ReservaPrioridad:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante

    def confirmar(self):
        return "Reserva prioritaria confirmada para " + self.solicitante.nombre


def reservar_desde_web(cancha, fecha, hora_inicio, hora_fin, solicitante):
    if isinstance(solicitante, EquipoOficial):
        reserva = ReservaPrioridad(
            cancha,
            fecha,
            hora_inicio,
            hora_fin,
            solicitante
        )
        print("Se creo la reserva prioritaria con exito")

    elif isinstance(solicitante, Estudiante):
        reserva = ReservaRegular(
            cancha,
            fecha,
            hora_inicio,
            hora_fin,
            solicitante
        )
        print("Se creo la reserva regular con exito")

    else:
        reserva = None

    if reserva is None:
        raise RuntimeError("No se creo con exito la reserva")

    return reserva

class CreadorDeReserva():
    def crear_reserva(self, cancha, fecha, hora_inicio, hora_fin, solicitante)
        raise NotImplementedError

class CreadorDeReservaRegular(CreadorDeReserva):
    def crear_reserva(self, cancha, fecha, hora_inicio, hora_fin, solicitante)
        return ReservaRegular(
            cancha, 
            fecha,
            hora_inicio,
            hora_fin,
            solicitante
        )

class CreadorDeReservaPrioritaria(CreadorDeReserva):
    def crear_reserva(self, cancha, fecha, hora_inicio, hora_fin, solicitante)
        return ReservaPrioridad(
            cancha, 
            fecha,
            hora_inicio,
            hora_fin,
            solicitante
        )

class FabricaDeReservas():
    @staticmethod
    def elegir_creador(solicitante)
        if insistance(solicitante, Estudiante):
            return CreadorDeReservaRegular()
        elif 
def reservar_desde_hall():
    pass


def main():
    # Reserva normal
    reserva_normal = reservar_desde_web(
        "Cancha de futbol",
        "2026-09-17",
        "18:00",
        "20:00",
        Estudiante("Erick")
    )
    print(reserva_normal.confirmar())

    # Reserva prioritaria
    reserva_prioritaria = reservar_desde_web(
        "Cancha de futbol",
        "2026-09-17",
        "20:00",
        "22:00",
        EquipoOficial("Equipo USFQ")
    )
    print(reserva_prioritaria.confirmar())


if __name__ == "__main__":
    main()
