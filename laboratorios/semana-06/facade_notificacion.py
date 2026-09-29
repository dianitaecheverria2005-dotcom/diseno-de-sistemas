class Inventario:
    def verificar(self, producto):
        print(f'Verificando el stock del {producto}')
        return True


class Pago:
    def procesar(self, monto):
        print(f'Procesando pago: ${monto}')
        return True


class Envio:
    def crear_envio(self, producto):
        print(f'Preparando el envio del: {producto}')


class Notificacion:
    def enviar_mensaje(self, correo, mensaje):
        print(f'Enviando mensaje a Gmail: {correo}')
        print(f'Mensaje: {mensaje}')
        print('Notificacion enviada correctamente')


class TiendaFacade:
    def __init__(self):
        self.inventario = Inventario()
        self.pago = Pago()
        self.envio = Envio()
        self.notificacion = Notificacion()

    def comprar(self, producto, precio, correo):

        if not self.inventario.verificar(producto):
            print('No hay stock')
            return

        if not self.pago.procesar(precio):
            print('Fallo el pago')
            return

        self.envio.crear_envio(producto)

        print('Compra completada')

        self.notificacion.enviar_mensaje(
            correo,
            f'Tu compra de {producto} por ${precio} fue realizada correctamente.'
        )


def main():
    tienda = TiendaFacade()

    tienda.comprar(
        'Laptop',
        1500,
        'cliente@gmail.com'
    )


if __name__ == "__main__":
    main()