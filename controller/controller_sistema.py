from controller.controller_campeonato import ControladorCampeonato
from controller.controller_lutador import ControladorLutador
from controller.controller_narrador import ControladorNarrador
from view.view_sistema import TelaSistema
from controller.controller_luta import ControladorLuta


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__controlador_luta = ControladorLuta(self)
        self.__controlador_lutador = ControladorLutador(self)
        self.__controlador_narrador = ControladorNarrador(self)

    def cadastra_luta(self):
        self.__controlador_luta.abre_tela()

    def cadastra_lutador(self):
        self.__controlador_lutador.abre_tela()

    def cadastra_narrador(self):
        self.__controlador_narrador.abre_tela()

    def cadastra_campeonato(self):
        self.__controlador_campeonato.abre_tela()

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_luta, 2: self.cadastra_lutador, 3: self.cadastra_narrador,
                        4: self.cadastra_campeonato, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @property
    def controlador_lutador(self):
        return self.__controlador_lutador

    @property
    def controlador_luta(self):
        return self.__controlador_luta