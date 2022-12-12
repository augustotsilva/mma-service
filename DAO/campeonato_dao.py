from DAO.base_dao import DAO
from entity.campeonato import Campeonato


class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonatos.pkl')

    def add(self, campeonato: Campeonato):
        if ((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.cpf, int)):
            super().add(campeonato.cpf, campeonato)

    def update(self, campeonato: Campeonato):
        if ((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.cpf, int)):
            super().update(campeonato.cpf, campeonato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
