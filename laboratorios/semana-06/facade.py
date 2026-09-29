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


class TiendaFacade:
    def __init__(self):
        self.inventario = Inventario()
        self.pago = Pago()
        self.envio = Envio()

    def comprar(self, producto, precio):

        if not self.inventario.verificar(producto):
            print('No hay stock')
            return

        if not self.pago.procesar(precio):
            print('Fallo el pago')
            return

        self.envio.crear_envio(producto)

        print('Compra completada')


def main():
    tienda = TiendaFacade()

    tienda.comprar('Laptop', 1500)


if __name__ == "__main__":
    main()


#sistema de notificacion que tenga la funcion de enviar un mensaje y que se haga o se notifique luego de que se envia, simulando que se envia al gmail