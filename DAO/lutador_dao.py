from DAO.base_dao import DAO
from entity.lutador import Lutador


class LutadorDAO(DAO):
    def __init__(self):
        super().__init__('lutadores.pkl')

    def add(self, lutador: Lutador):
        if ((lutador is not None) and isinstance(lutador, Lutador) and isinstance(lutador.cpf, int)):
            super().add(lutador.cpf, lutador)

    def update(self, lutador: Lutador):
        if ((lutador is not None) and isinstance(lutador, Lutador) and isinstance(lutador.cpf, int)):
            super().update(lutador.cpf, lutador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
