from DAO.base_dao import DAO
from entity.luta import Luta


class LutaDAO(DAO):
    def __init__(self):
        super().__init__('lutas.pkl')

    def add(self, luta: Luta):
        if ((luta is not None) and isinstance(luta, Luta) and isinstance(luta.cpf, int)):
            super().add(luta.cpf, luta)

    def update(self, luta: Luta):
        if ((luta is not None) and isinstance(luta, Luta) and isinstance(luta.cpf, int)):
            super().update(luta.cpf, luta)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
