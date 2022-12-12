from dao.campeonato_dao import CampeonatoDAO
from entity.campeonato import Campeonato
from view.view_campeonato import *


class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatoDAO = CampeonatoDAO()

    def lista_por_id(self, id: int = None):
        return self.__campeonatoDAO.get(id)

    def lista_por_dono(self, dono: str = None):
        campeonatos_por_dono = []
        campeonatos = self.__campeonatoDAO.get_all()
        for campeonato in campeonatos:
            if dono.upper() == campeonato.dono.upper():
                campeonatos_por_dono.append(campeonato)
        return campeonatos_por_dono

    def lista_campeonato_por_id(self):
        campeonatos = self.__campeonatoDAO.get_all()
        if not campeonatos:
            return self.__tela_campeonato.mostra_mensagem("Não há campeonatos registrados")
        campeonato = self.lista_por_id(self.__tela_campeonato.seleciona_campeonato())
        return self.__tela_campeonato.mostra_campeonato(self.convert_to_view_object(campeonato))

    def lista_campeonatos_por_dono(self):
        campeonatos = self.__campeonatoDAO.get_all()
        if not campeonatos:
            return self.__tela_campeonato.mostra_mensagem("Não há campeonatos registrados")
        dono = self.__tela_campeonato.seleciona_dono()
        campeonatos = self.convert_to_view_object_list(self.lista_por_dono(dono))
        for campeonato in campeonatos:
            return self.__tela_campeonato.mostra_campeonato(campeonato)

    def lista_campeonatos(self):
        campeonatos = self.__campeonatoDAO.get_all()
        if campeonatos:
            for campeonato in campeonatos:
                self.__tela_campeonato.mostra_campeonato(self.convert_to_view_object(campeonato))
        else:
            self.__tela_campeonato.mostra_mensagem("Não há campeonatos cadastrados")

    def incluir_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        try:
            if self.lista_por_id(dados_campeonato['id']) is not None:
                raise ValueError
            campeonato = Campeonato(dados_campeonato["id"], dados_campeonato["nome"], dados_campeonato["dono"])
            self.__campeonatoDAO.add(campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato inserido com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def alterar_campeonato(self):
        try:
            self.lista_campeonatos()
            campeonatos = self.__campeonatoDAO.get_all()
            if campeonatos:
                id_campeonato = self.__tela_campeonato.seleciona_campeonato()
                campeonato = self.lista_por_id(id_campeonato)
                if campeonato is not None:
                    novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
                    campeonato.id = novos_dados_campeonato["id"]
                    campeonato.nome = novos_dados_campeonato["nome"]
                    campeonato.dono = novos_dados_campeonato["dono"]
                    self.__campeonatoDAO.update(campeonato)
                    self.lista_campeonatos()
                    self.__tela_campeonato.mostra_mensagem("Campeonato alterado com sucesso")
                else:
                    raise ValueError
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def excluir_campeonato(self):
        try:
            self.lista_campeonatos()
            campeonatos = self.__campeonatoDAO.get_all()
            if campeonatos:
                id_campeonato = self.__tela_campeonato.seleciona_campeonato()
                campeonato = self.lista_por_id(id_campeonato)
                if campeonato is not None:
                    self.__campeonatoDAO.remove(campeonato.id)
                    self.__tela_campeonato.mostra_mensagem("Campeonato excluído com sucesso")
                else:
                    raise ValueError
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def incluir_luta_ao_campeonato(self):
        id_campeonato = self.__tela_campeonato.seleciona_campeonato()
        id_luta = self.__tela_campeonato.seleciona_luta()
        try:
            campeonato = self.lista_por_id(id_campeonato)
            luta = self.__controlador_sistema.controlador_luta.pega_luta_por_id(id_luta)
            campeonato.adicionar_luta(luta)
            self.__campeonatoDAO.update(campeonato)
            self.__tela_campeonato.mostra_mensagem("Luta ligada ao campeonato com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Luta não existente")

    def remover_luta_do_campeonato(self):
        id_campeonato = self.__tela_campeonato.seleciona_campeonato()
        id_luta = self.__tela_campeonato.seleciona_luta()
        try:
            campeonato = self.lista_por_id(id_campeonato)
            luta = self.__controlador_sistema.controlador_luta.pega_luta_por_id(id_luta)
            campeonato.excluir_luta(luta)
            self.__campeonatoDAO.update(campeonato)
            self.__tela_campeonato.mostra_mensagem("Luta desvinculada do campeonato com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Luta não existente")

    def listar_lutas_do_campeonato(self):
        id_campeonato = self.__tela_campeonato.seleciona_campeonato()

        lutas = self.__campeonatoDAO.get(id_campeonato).lutas
        if len(lutas) == 0:
            self.__tela_campeonato.mostra_mensagem('\nLista de Lutas está vazia\n')
        else:
            for luta in lutas:
                lista_narradores = []
                for narrador in luta.narradores:
                    nome_narrador = narrador.nome
                    lista_narradores.append(nome_narrador)
                self.__tela_campeonato.mostra_luta_campeonato(
                    {'id': luta.id, 'lutador1': luta.lutador1.nome, 'lutador2': luta.lutador2.nome,
                     'narradores': lista_narradores, 'data': luta.data, 'vencedor': luta.vencedor.nome,
                     'card': luta.card, 'local': luta.local})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_campeonato, 2: self.lista_campeonato_por_id,
                        3: self.lista_campeonatos_por_dono, 4: self.lista_campeonatos,
                        5: self.alterar_campeonato, 6: self.excluir_campeonato,
                        7: self.incluir_luta_ao_campeonato,
                        8: self.remover_luta_do_campeonato,
                        9: self.listar_lutas_do_campeonato,
                        0: self.retornar
                        }

        while True:
            opcao_escolhida = self.__tela_campeonato.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @staticmethod
    def convert_to_view_object_list(campeonatos: []):
        view_object_list = []
        for campeonato in campeonatos:
            view_object_list.append({"id": campeonato.id, "nome": campeonato.nome, "dono": campeonato.dono})
        return view_object_list

    @staticmethod
    def convert_to_view_object(campeonato):
        return {"id": campeonato.id, "nome": campeonato.nome, "dono": campeonato.dono}
