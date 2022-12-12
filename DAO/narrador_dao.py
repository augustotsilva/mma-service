from DAO.base_dao import DAO
from entity.narrador import Narrador


class NarradorDAO(DAO):
    def __init__(self):
        super().__init__('narradores.pkl')

    def add(self, narrador: Narrador):
        if ((narrador is not None) and isinstance(narrador, Narrador) and isinstance(narrador.cpf, int)):
            super().add(narrador.cpf, narrador)

    def update(self, narrador: Narrador):
        if ((narrador is not None) and isinstance(narrador, Narrador) and isinstance(narrador.cpf, int)):
            super().update(narrador.cpf, narrador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
