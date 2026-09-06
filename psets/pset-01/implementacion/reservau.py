from datetime import timedelta


class ReglaPrioridad:
    def aplica_prioridad(self, hora):
        raise NotImplementedError


class PrioridadAntes18(ReglaPrioridad):
    def aplica_prioridad(self, hora):
        return hora < 18


class SinPrioridad(ReglaPrioridad):
    def aplica_prioridad(self, hora):
        return False


class Solicitante:
    def __init__(self, nombre, regla_prioridad):
        self.nombre = nombre
        self.regla_prioridad = regla_prioridad

    def tiene_prioridad(self, hora):
        return self.regla_prioridad.aplica_prioridad(hora)


class Estudiante(Solicitante):
    def __init__(self, nombre):
        sin_prioridad = SinPrioridad()
        super().__init__(nombre, sin_prioridad)


class Capitan(Solicitante):
    def __init__(self, nombre):
        prioridad_antes_18 = PrioridadAntes18()
        super().__init__(nombre, prioridad_antes_18)


class Cancha:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def esta_disponible(self):
        return self.disponible

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


class Reserva:
    def __init__(self, solicitante, cancha, fecha_hora_inicio):
        self.solicitante = solicitante
        self.cancha = cancha
        self.fecha_hora_inicio = fecha_hora_inicio
        self.estado = "ACTIVA"

    def cancelar(self, solicitante, momento_actual):
        if solicitante != self.solicitante:
            print("La reserva no pertenece al solicitante.")
            return

        tiempo_restante = self.fecha_hora_inicio - momento_actual

        if tiempo_restante >= timedelta(hours=2):
            self.estado = "CANCELADA"
            self.cancha.liberar()
        else:
            self.estado = "NO_SHOW"


class Administrador:
    def __init__(self, nombre):
        self.nombre = nombre

    def gestionar_cancha(self, cancha, disponible):
        cancha.disponible = disponible

    def intervenir_conflicto(self, reserva):
        print("El Administrador esta interviniendo en el conflicto relacionado con la reserva.")