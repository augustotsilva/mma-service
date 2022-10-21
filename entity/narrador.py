

class Narrador(Pessoa):
    def __init__(self, id: int, nome: str, idade: int, temperamento: str):
        super().__init__(nome, idade)
        self.__id = id
        self.__temperamento = temperamento


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def temperamento(self):
        return self.__temperamento

    @temperamento.setter
    def temperamento(self, temperamento: int):
        self.__temperamento = temperamento

