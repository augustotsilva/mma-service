from entity.pessoa import Pessoa


class Lutador(Pessoa):
    def __init__(self, nome: str, idade: int, id: int, altura: float, peso: float, envergadura: float):
        super().__init__(nome, idade)
        if isinstance(id, int) and isinstance(altura, float) and isinstance(peso, float) and\
           isinstance(envergadura, float):
            self.__id = id
            self.__altura = altura
            self.__peso = peso
            self.__envergadura = envergadura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        if isinstance(altura, float):
            self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        if isinstance(peso, float):
            self.__peso = peso
    @property
    def envergadura(self):
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, envergadura):
        if isinstance(envergadura, float):
            self.__envergadura = envergadura
