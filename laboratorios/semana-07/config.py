class GameConfig:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            cls._instancia.dificultad = "Normal"
            cls._instancia.numero_maximo_turnos = 10

        return cls._instancia