from dao.base_dao import BaseDAO
from entity.luta import Luta


class LutaDAO(BaseDAO):
    def __init__(self):
        super().__init__('lutas.pkl')

    def add(self, luta: Luta):
        if ((luta is not None) and isinstance(luta, Luta) and isinstance(luta.id, int)):
            super().add(luta.id, luta)

    def update(self, luta: Luta):
        if ((luta is not None) and isinstance(luta, Luta) and isinstance(luta.id, int)):
            super().update(luta.id, luta)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
