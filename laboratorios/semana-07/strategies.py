class EstrategiaAtaque:

    def atacar(self, ataque):
        raise NotImplementedError


class AtaqueNormal(EstrategiaAtaque):

    def atacar(self, ataque):
        return ataque


class AtaqueFuerte(EstrategiaAtaque):

    def atacar(self, ataque):
        return ataque * 2