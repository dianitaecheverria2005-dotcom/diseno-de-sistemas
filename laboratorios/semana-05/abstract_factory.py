from abc import ABC, abstractmethod


# =========================
# PRODUCTOS ABSTRACTOS
# =========================

class Boton(ABC):
    @abstractmethod
    def renderizar(self):
        pass


class Menu(ABC):
    @abstractmethod
    def renderizar(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def renderizar(self):
        pass


# =========================
# PRODUCTOS WINDOWS
# =========================

class BotonWindows(Boton):
    def renderizar(self):
        print("Boton estilo windows")


class MenuWindows(Menu):
    def renderizar(self):
        print("Menu estilo windows")


class CheckboxWindows(Checkbox):
    def renderizar(self):
        print("Checkbox estilo windows")


# =========================
# PRODUCTOS MAC
# =========================

class BotonMac(Boton):
    def renderizar(self):
        print("Boton estilo mac")


class MenuMac(Menu):
    def renderizar(self):
        print("Menu estilo mac")


class CheckboxMac(Checkbox):
    def renderizar(self):
        print("Checkbox estilo mac")


# =========================
# ABSTRACT FACTORY
# =========================

class UIFactoryABC(ABC):

    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_menu(self):
        pass

    @abstractmethod
    def crear_checkbox(self):
        pass


# =========================
# FACTORY WINDOWS
# =========================

class WindowsFactory(UIFactoryABC):

    def crear_boton(self):
        return BotonWindows()

    def crear_menu(self):
        return MenuWindows()

    def crear_checkbox(self):
        return CheckboxWindows()


# =========================
# FACTORY MAC
# =========================

class MacFactory(UIFactoryABC):

    def crear_boton(self):
        return BotonMac()

    def crear_menu(self):
        return MenuMac()

    def crear_checkbox(self):
        return CheckboxMac()


# =========================
# CREAR INTERFAZ
# =========================

def crear_UI(factory):
    boton = factory.crear_boton()
    menu = factory.crear_menu()
    checkbox = factory.crear_checkbox()

    boton.renderizar()
    menu.renderizar()
    checkbox.renderizar()


# =========================
# MAIN
# =========================

def main():
    sistema = "Windows"

    if sistema == "Windows":
        factory = WindowsFactory()

    elif sistema == "Mac":
        factory = MacFactory()

    crear_UI(factory)


main()