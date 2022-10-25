from view.view_narrador import TelaNarrador


class ControladorNarrador:
    def __init__(self, controlador_sistema):
        # Tratar exceções
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaNarrador()
        self.__narradores = []

    def lista_campeonato_por_id(self, id: int):
        # Tratar a exceção
        for campeonato in self.__narradores:
            if campeonato.id == id:
                return campeonato
        return None

    def lista_campeonatos(self):
        self.__tela_campeonato.mostra_mensagem("--------------------------------------------------")
        if self.__narradores:
            for campeonato in self.__narradores:
                self.__tela_campeonato.mostra_campeonato(
                    {'id': campeonato.id, 'nome': campeonato.nome, 'dono': campeonato.dono})
        else:
            self.__tela_campeonato.mostra_mensagem("Não há campeonatos cadastrados")

        self.__tela_campeonato.mostra_mensagem("--------------------------------------------------")

    def lista_campeonatos_por_dono(self, dono: str):
        # Tratar exceções
        for campeonato in self.__narradores:
            if dono == campeonato.dono:
                self.__tela_campeonato.mostra_campeonato(
                    {'id': campeonato["id"], 'nome': campeonato["nome"], 'dono': campeonato["dono"]})

    def incluir_campeonato(self):
        # Tratar a exceções
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        if self.lista_campeonato_por_id(dados_campeonato['id']) is not None:
            self.__tela_campeonato.mostra_mensagem("Campeonato já existente!")

        campeonato = Campeonato(dados_campeonato["id"], dados_campeonato["nome"], dados_campeonato["dono"])
        self.__narradores.append(campeonato)
        time.sleep(0.4)
        self.__tela_campeonato.mostra_mensagem("Campeonato inserido com sucesso")

    def excluir_campeonato(self):
        # Tratar exceções
        self.lista_campeonatos()
        campeonato = self.pega_campeonato_por_id(self.__tela_campeonato.seleciona_campeonato())

        if campeonato is not None:
            self.__narradores.remove(campeonato)
            self.lista_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        # tratar exceções
        lista_opcoes = {1: self.incluir_campeonato, 2: self.lista_campeonato_por_id, 3: self.lista_campeonatos,
                        4: self.excluir_campeonato, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_campeonato.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
