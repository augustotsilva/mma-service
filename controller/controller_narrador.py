from view.view_narrador import TelaNarrador
from entity.narrador import Narrador

class ControladorNarrador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_narrador = TelaNarrador()
        self.__narradores = []

    def lista_narrador_por_id(self, id: int):
        for narrador in self.__narradores:
            if narrador.id == id:
                return narrador
        return None

    def lista_narradores(self):
        # Tratar exceções
        self.__tela_narrador.mostra_mensagem("--------------------------------------------------")
        if len(self.__narradores) == 0:
            self.__tela_narrador.mostra_mensagem('\nLista de Narradores está vazia\n')
        else:
            for narrador in self.__narradores:
                self.__tela_narrador.mostra_narrador({'id': narrador.id, 'nome': narrador.nome, 'idade': narrador.idade, 'temperamento': narrador.temperamento})
        self.__tela_narrador.mostra_mensagem("--------------------------------------------------")

    def incluir_narrador(self):
        dados_narrador = self.__tela_narrador.pega_dados_narradores()
        narrador = self.lista_narrador_por_id(dados_narrador['id'])
        try:
            if narrador != None:
                raise KeyError
            narrador = Narrador(dados_narrador['id'], dados_narrador['nome'], dados_narrador['idade'], dados_narrador['temperamento'])
            self.__narradores.append(narrador)
        except KeyError:
            self.__tela_narrador.mostra_mensagem("\nNarrador já existente!\n")

    def excluir_narrador(self):
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
        lista_opcoes = {1: self.incluir_narrador, 2: self.lista_narrador_por_id, 3: self.lista_narradores,
                        4: self.excluir_narrador, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_narrador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
