from dao.base_dao import BaseDAO
from entity.lutador import Lutador


class LutadorDAO(BaseDAO):
    def __init__(self):
        super().__init__('lutadores.pkl')

    def add(self, lutador: Lutador):
        if ((lutador is not None) and isinstance(lutador, Lutador) and isinstance(lutador.id, int)):
            super().add(lutador.id, lutador)

    def update(self, lutador: Lutador):
        if ((lutador is not None) and isinstance(lutador, Lutador) and isinstance(lutador.id, int)):
            super().update(lutador.id, lutador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
