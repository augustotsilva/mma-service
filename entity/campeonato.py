class Campeonato:

    def __init__(self, id: int, nome: str, dono: str):
        self.__id = id
        self.__nome = nome
        self.__dono = dono

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
