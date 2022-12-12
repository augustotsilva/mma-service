from dao.base_dao import BaseDAO
from entity.narrador import Narrador


class NarradorDAO(BaseDAO):
    def __init__(self):
        super().__init__('narradores.pkl')

    def add(self, narrador: Narrador):
        if ((narrador is not None) and isinstance(narrador, Narrador) and isinstance(narrador.id, int)):
            super().add(narrador.id, narrador)

    def update(self, narrador: Narrador):
        if ((narrador is not None) and isinstance(narrador, Narrador) and isinstance(narrador.id, int)):
            super().update(narrador.id, narrador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
