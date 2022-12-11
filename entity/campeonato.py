from entity.luta import Luta


class Campeonato:

    def __init__(self, id: int, nome: str, dono: str):
        self.__id = id
        self.__nome = nome
        self.__dono = dono
        self.__lutas = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono: str):
        self.__dono = dono

    @property
    def lutas(self):
        return self.__lutas

    @lutas.setter
    def lutas(self, lutas: []):
        self.__lutas = lutas

    def adicionar_luta(self, luta: Luta):
        if luta is not None:
            self.__lutas.append(luta)
        else:
            raise ValueError

    def excluir_luta(self, id_luta: int):
        if id_luta is not None:
            self.__lutas.remove(id_luta)
        else:
            raise ValueError
