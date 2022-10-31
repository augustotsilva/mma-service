from entity.narrador import Narrador
from view.view_narrador import TelaNarrador


class ControladorNarrador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_narrador = TelaNarrador()
        self.__narradores = []

    def lista_por_id(self, id: int = None):
        for campeonato in self.__narradores:
            if campeonato.id == id:
                return campeonato

    def lista_por_dono(self, dono: str = None):
        campeonatos = []
        for campeonato in self.__narradores:
            if dono.upper() == campeonato.dono.upper():
                campeonatos.append(campeonato)
        return campeonatos

    def lista_narrador_por_id(self):
        if not self.__narradores:
            return self.__tela_narrador.mostra_mensagem("Não há narradores registrados")
        campeonato = self.lista_por_id(self.__tela_narrador.seleciona_narrador())
        return self.__tela_narrador.mostra_narrador(self.convert_to_view_object(campeonato))

    def lista_narradores(self):
        if self.__narradores:
            for campeonato in self.__narradores:
                self.__tela_narrador.mostra_narrador(
                    {'id': campeonato.id, 'nome': campeonato.nome, 'dono': campeonato.dono})
        else:
            self.__tela_narrador.mostra_mensagem("Não há narradores cadastrados")

    def incluir_narrador(self):
        dados_narrador = self.__tela_narrador.pega_dados_narradores()
        if self.lista_por_id(dados_narrador['id']) is not None:
            self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador não existente")
        else:
            campeonato = Narrador(dados_narrador["id"], dados_narrador["nome"], dados_narrador["dono"])
            self.__narradores.append(campeonato)
            self.__tela_narrador.mostra_mensagem("Narrador inserido com sucesso")

    def alterar_campeonato(self):
        self.lista_narradores()
        if self.__narradores:
            id_campeonato = self.__tela_narrador.seleciona_narrador()
            narrador = self.lista_por_id(id_campeonato)
            if narrador is not None:
                novos_dados_narrador = self.__tela_narrador.pega_dados_narradores()
                narrador.id = novos_dados_narrador["id"]
                narrador.nome = novos_dados_narrador["nome"]
                narrador.dono = novos_dados_narrador["dono"]
                self.lista_narradores()
                self.__tela_narrador.mostra_mensagem("Narrador alterado com sucesso")
            else:
                self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador não existente")

    def excluir_narrador(self):
        self.lista_narradores()
        if self.__narradores:
            id_campeonato = self.__tela_narrador.seleciona_narrador()
            campeonato = self.lista_por_id(id_campeonato)
            if campeonato is not None:
                self.__narradores.remove(campeonato)
                self.__tela_narrador.mostra_mensagem("Narrador excluído com sucesso")
            else:
                self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_narrador, 2: self.lista_narrador_por_id, 3: self.lista_narradores,
                        4: self.excluir_narrador, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_narrador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @staticmethod
    def convert_to_view_object_list(narradores: []):
        view_object_list = []
        for narrador in narradores:
            view_object_list.append({"id": narrador.id, "nome": narrador.nome, "dono": narrador.dono})
        return view_object_list

    @staticmethod
    def convert_to_view_object(narrador):
        return {"id": narrador.id, "nome": narrador.nome, "dono": narrador.dono}
