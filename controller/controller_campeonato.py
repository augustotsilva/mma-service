from entity.campeonato import Campeonato
from view.view_campeonato import *


class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatos = []
        self.__lutas = []

    def lista_por_id(self, id: int = None):
        for campeonato in self.__campeonatos:
            if campeonato.id == id:
                return campeonato

    def lista_por_dono(self, dono: str = None):
        campeonatos = []
        for campeonato in self.__campeonatos:
            if dono.upper() == campeonato.dono.upper():
                campeonatos.append(campeonato)
        return campeonatos

    def lista_campeonato_por_id(self):
        if not self.__campeonatos:
            return self.__tela_campeonato.mostra_mensagem("Não há campeonatos registrados")
        campeonato = self.lista_por_id(self.__tela_campeonato.seleciona_campeonato())
        return self.__tela_campeonato.mostra_campeonato(self.convert_to_view_object(campeonato))

    def lista_campeonatos_por_dono(self):
        if not self.__campeonatos:
            return self.__tela_campeonato.mostra_mensagem("Não há campeonatos registrados")
        dono = self.__tela_campeonato.seleciona_dono()
        campeonatos = self.convert_to_view_object_list(self.lista_por_dono(dono))
        for campeonato in campeonatos:
            return self.__tela_campeonato.mostra_campeonato(campeonato)

    def lista_campeonatos(self):
        if self.__campeonatos:
            for campeonato in self.__campeonatos:
                self.__tela_campeonato.mostra_campeonato(self.convert_to_view_object(campeonato))
        else:
            self.__tela_campeonato.mostra_mensagem("Não há campeonatos cadastrados")

    def incluir_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        try:
            if self.lista_por_id(dados_campeonato['id']) is not None:
                raise ValueError
            campeonato = Campeonato(dados_campeonato["id"], dados_campeonato["nome"], dados_campeonato["dono"])
            self.__campeonatos.append(campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato inserido com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def alterar_campeonato(self):
        try:
            self.lista_campeonatos()
            if self.__campeonatos:
                id_campeonato = self.__tela_campeonato.seleciona_campeonato()
                campeonato = self.lista_por_id(id_campeonato)
                if campeonato is not None:
                    novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
                    campeonato.id = novos_dados_campeonato["id"]
                    campeonato.nome = novos_dados_campeonato["nome"]
                    campeonato.dono = novos_dados_campeonato["dono"]
                    self.lista_campeonatos()
                    self.__tela_campeonato.mostra_mensagem("Campeonato alterado com sucesso")
                else:
                    raise ValueError
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def excluir_campeonato(self):
        try:
            self.lista_campeonatos()
            if self.__campeonatos:
                id_campeonato = self.__tela_campeonato.seleciona_campeonato()
                campeonato = self.lista_por_id(id_campeonato)
                if campeonato is not None:
                    self.__campeonatos.remove(campeonato)
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
            luta = self.__controlador_sistema.controlador_narrador.lista_por_id(id_luta)
            campeonato.adicionar_luta(luta)
            self.__tela_campeonato.mostra_mensagem("Luta ligada ao campeonato com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Luta não existente")

    def remover_luta_do_campeonato(self):
        id_campeonato = self.__tela_campeonato.seleciona_campeonato()
        id_luta = self.__tela_campeonato.seleciona_luta()
        try:
            campeonato = self.lista_por_id(id_campeonato)
            luta = self.__controlador_sistema.controlador_narrador.lista_por_id(id_luta)
            campeonato.excluir_luta(luta)
            self.__tela_campeonato.mostra_mensagem("Luta desvinculada do campeonato com sucesso")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Luta não existente")

    # def listar_lutas_do_campeonato(self):
    #     id_campeonato = self.__tela_campeonato.seleciona_campeonato()
    #     id_luta = self.__tela_campeonato.seleciona_luta()
    #     try:
    #         campeonato = self.lista_por_id(id_campeonato)
    #         for luta in campeonato.lutas:
    #             self.__controlador_sistema
    #     except ValueError:
    #         self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Luta não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_campeonato, 2: self.lista_campeonato_por_id,
                        3: self.lista_campeonatos_por_dono, 4: self.lista_campeonatos,
                        5: self.alterar_campeonato, 6: self.excluir_campeonato,
                        7: self.incluir_luta_ao_campeonato,
                        8: self.remover_luta_do_campeonato,
                        # 9: self.listar_lutas_do_campeonato,
                        0: self.retornar
                        }

        while True:
            opcao_escolhida = self.__tela_campeonato.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @staticmethod
    def convert_to_view_object_list(narradores: []):
        view_object_list = []
        for narrador in narradores:
            view_object_list.append({"id": narrador.id, "nome": narrador.nome, "idade": narrador.idade,
                                     "temperamento": narrador.temperamento})
        return view_object_list

    @staticmethod
    def convert_to_view_object(narrador):
        return {"id": narrador.id, "nome": narrador.nome, "idade": narrador.idade,
                "temperamento": narrador.temperamento}
