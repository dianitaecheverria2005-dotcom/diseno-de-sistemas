from datetime import datetime, timedelta

from reservau import Estudiante, Capitan, Cancha, Reserva, Administrador


print("SIMULACION RESERVAU")
print()


#..............................................................................

print("=== Caso 1: Estudiante reserva una cancha ===")

estudiante = Estudiante("Diana")
cancha_1 = Cancha("Cancha 1")

print("1. El estudiante solicita reservar una cancha.")

print("2. El sistema verifica la disponibilidad de la cancha.")
if cancha_1.esta_disponible():

    print("3. El sistema determina la regla de prioridad.")
    
    prioridad = estudiante.tiene_prioridad(15)

    print("4. El sistema aplica la regla de prioridad.")
    if prioridad:
        print("El estudiante tiene prioridad.")
    else:
        print("El estudiante no tiene prioridad.")

    print("5. El sistema crea la reserva.")

    fecha_reserva = datetime.now() + timedelta(hours=5)

    reserva_1 = Reserva(
        estudiante,
        cancha_1,
        fecha_reserva
    )

    cancha_1.reservar()

    print("6. La reserva es confirmada.")

else:
    print("La cancha no está disponible.")
    print("No se crea la reserva.")

print()


#..............................................................................

print("=== Caso 2: El Capitan reserva una cancha antes de las 18:00 ===")

capitan = Capitan("Carlos")
cancha_2 = Cancha("Cancha 2")

print("1. El capitan solicita reservar una cancha.")

print("2. El sistema verifica la disponibilidad de la cancha.")

if cancha_2.esta_disponible():

    print("3. El sistema determina la regla de prioridad.")

    prioridad = capitan.tiene_prioridad(17)

    print("4. El sistema aplica la regla de prioridad.")

    if prioridad:
        print("El equipo oficial tiene prioridad.")
    else:
        print("El equipo oficial no tiene prioridad.")

    print("5. El sistema crea la reserva.")

    fecha_reserva_2 = datetime.now() + timedelta(hours=6)

    reserva_2 = Reserva(
        capitan,
        cancha_2,
        fecha_reserva_2
    )

    cancha_2.reservar()

    print("6. La reserva es confirmada.")

else:
    print("La cancha no esta disponible.")

print()


#.........................................................................................

print("=== Caso 3: Cancelacion normal antes de las 2 horas ===")

cancha_3 = Cancha("Cancha 3")

fecha_reserva_3 = datetime.now() + timedelta(hours=5)

reserva_3 = Reserva(
    estudiante,
    cancha_3,
    fecha_reserva_3
)

cancha_3.reservar()

print("1. El estudiante solicita cancelar su reserva.")

print("2. El sistema verifica que la reserva pertenezca al estudiante.")

print("3. El sistema determina cuanto tiempo falta para la reserva.")

momento_actual = datetime.now()

print("4. El sistema determina el tipo de cancelacion.")

reserva_3.cancelar(estudiante, momento_actual)

print("5. El sistema registra la cancelacion.")

print("6. El sistema actualiza el estado de la reserva:", reserva_3.estado)

print()


#.......................................................................................

print("=== Caso 4: Cancelacion despues de las 2 horas ===")

cancha_4 = Cancha("Cancha 4")

fecha_reserva_4 = datetime.now() + timedelta(hours=1)

reserva_4 = Reserva(
    estudiante,
    cancha_4,
    fecha_reserva_4
)

cancha_4.reservar()

print("1. El estudiante solicita cancelar su reserva.")

print("2. El sistema verifica que la reserva pertenezca al estudiante.")

print("3. El sistema determina cuanto tiempo falta para la reserva.")

momento_actual = datetime.now()

print("4. El sistema determina el tipo de cancelacion.")

reserva_4.cancelar(estudiante, momento_actual)

print("5. El sistema registra el resultado.")

print("6. El sistema registra el estado de la reserva:", reserva_4.estado)

print()


#.........................................................................................

print("=== Caso 5: Intento de cancelar una reserva ajena ===")

otro_estudiante = Estudiante("Pedro")

print("1. Pedro solicita cancelar una reserva.")

print("2. El sistema verifica que la reserva pertenezca a Pedro.")

reserva_1.cancelar(otro_estudiante, datetime.now())

print()


#..........................................................................................

print("=== Caso 6: Administrador gestiona una cancha ===")

administrador = Administrador("Laura")

print("1. El administrador solicita gestionar una cancha.")

print("2. El sistema presenta la cancha.")

print("3. El administrador cambia la disponibilidad.")

administrador.gestionar_cancha(cancha_1, True)

print("4. El sistema registra el cambio.")

print("5. Disponibilidad de la cancha:", cancha_1.disponible)

print()


#..........................................................................................

print("=== Caso 7: Administrador interviene en un conflicto ===")

print("1. El administrador solicita intervenir en un conflicto.")

print("2. El sistema identifica la reserva.")

print("3. El administrador interviene.")

administrador.intervenir_conflicto(reserva_1)

print("4. El sistema registra el resultado.")

print()


print("=== Fin, gracias! ===")