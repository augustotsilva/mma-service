from dao.base_dao import BaseDAO
from entity.campeonato import Campeonato


class CampeonatoDAO(BaseDAO):
    def __init__(self):
        super().__init__('campeonatos.pkl')

    def add(self, campeonato: Campeonato):
        if ((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.id, int)):
            super().add(campeonato.id, campeonato)

    def update(self, campeonato: Campeonato):
        if ((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.id, int)):
            super().update(campeonato.id, campeonato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if isinstance(key, int):
            return super().remove(key)
