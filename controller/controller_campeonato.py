class ControladorCampeonato:
    def __init__(self, controller_sistema, tela_campeonato):
        # Tratar exceções
        self.__campeonatos = []
        self._controlador_sistema = controller_sistema
        self.__tela_campeonato = tela_campeonato

    def lista_campeonato_por_id(self, id: int):
        # Tratar a exceção
        for campeonato in self.__campeonatos:
            if campeonato.id == id:
                return campeonato
        return None

    def lista_campeonatos(self):
        # Tratar exceções
        for campeonato in self.__campeonatos:
            self.__tela_campeonato.mostra_campeonato(
                {'id': campeonato.id, 'nome': campeonato.nome, 'dono': campeonato.dono})

    def lista_campeonatos_por_dono(self, dono: str):
        # Tratar exceções
        for campeonato in self.__campeonato:
            if dono == campeonato.dono:
                self.__tela_campeonato.mostra_campeonato(
                    {'id': campeonato.id, 'nome': campeonato.nome, 'dono': campeonato.dono})

    def incluir_campeonato(self):
        # Tratar a exceções
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        campeonato = self.lista_campeonato_por_id(dados_campeonato['id'])
        try:
            if campeonato is not None:
                raise KeyError
            self.__campeonatos.append(campeonato)
        except KeyError:
            self.__tela_campeonato.mostra_mensagem("Campeonato já existente!")

    def excluir_campeonato(self):
        # Tratar exceções
        self.lista_campeonatos()
        campeonato = self.pega_campeonato_por_id(self.__tela_campeonato.seleciona_campeonato())

        if campeonato is not None:
            self.__campeonatos.remove(campeonato)
            self.lista_campeonatos()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENÇÃO: Campeonato não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        # tratar exceções
        lista_opcoes = {1: self.incluir_luta, 2: self.lista_lutas_por_categoria, 3: self.lista_lutas,
                        4: self.excluir_luta, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_luta.tela_opcoes()]()
