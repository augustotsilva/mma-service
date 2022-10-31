from entity.lutador import Lutador


class Luta:
    def __init__(self, id: int, lutador1: Lutador, lutador2: Lutador, narradores: Narrador, data: str, vencedor: Lutador, card: int, local: int):
        if isinstance(id, int) and isinstance(lutador1, Lutador) and isinstance(lutador2, Lutador) and isinstance(narradores, Narrador) and\
           isinstance(data, str) and isinstance(vencedor, Lutador) and isinstance(card, int) and isinstance(local, str):
            self.__id = id
            self.__lutador1 = lutador1
            self.__lutador2 = lutador2
            self.__narradores = []
            self.__data = data
            self.__vencedor = vencedor
            self.__card = card
            self.__local = local

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id

    @property
    def lutador1(self):
        return self.__lutador1

    @lutador1.setter
    def lutador1(self, lutador1):
        if isinstance(lutador1, Lutador):
            self.__lutador1 = lutador1

    @property
    def lutador2(self):
        return self.__lutador2

    @lutador2.setter
    def lutador2(self, lutador2):
        if isinstance(lutador2, Lutador):
            self.__lutador2 = lutador2

    @property
    def narradores(self):
        return self.__narradores

    @narradores.setter
    def narradores(self, narradores):
        self.__narradores = narradores

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.__data = data

    @property
    def vencedor(self):
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        if isinstance(vencedor, Lutador):
            self.__vencedor = vencedor

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, card):
        if isinstance(card, int):
            self.__card = card

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local):
        if isinstance(local, str):
            self.__local = local
