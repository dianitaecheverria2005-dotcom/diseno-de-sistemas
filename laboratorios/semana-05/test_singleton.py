from singleton import GestorDeConfiguracion


def test_rechaza_reserva():
    config = GestorDeConfiguracion.obtener_objeto()
    config.modo_mantenimiento = True

    assert GestorDeConfiguracion.reserva_permitida(config) is False


def test_reserva_aceptada():
    config = GestorDeConfiguracion.obtener_objeto()

 #El singleton comparte y conserva un mismo estado global entre diferentes partes del programa,
#entonces conserva los cambios de un test y afecta a los siguientes tests.
    config.modo_mantenimiento = False

    assert GestorDeConfiguracion.reserva_permitida(config) is True


       