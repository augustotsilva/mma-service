from view.view_lutador import TelaLutador
from entity.lutador import Lutador


class ControladorLutador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lutadores = []
        self.__tela_lutador = TelaLutador(self)

    def pega_lutador_por_id(self, id: int):
        for lutador in self.__lutadores:
            if lutador.id == id:
                return lutador
        return None

    def incluir_lutador(self):
        dados_lutador = self.__tela_lutador.pega_dados_lutador()
        lutador = self.pega_lutador_por_id(dados_lutador['id'])
        try:
            if lutador != None:
                raise KeyError
            lutador = Lutador(dados_lutador['nome'], dados_lutador['idade'], dados_lutador['id'], dados_lutador['altura'], dados_lutador['peso'], dados_lutador['envergadura'])
            self.__lutadores.append(lutador)
        except KeyError:
            self.__tela_lutador.mostra_mensagem("\nLutador já existente!\n")

    def excluir_lutador(self):
        self.lista_lutadores()
        lutador = self.__tela_lutador.seleciona_lutador()
        if lutador is not None:
            self.__lutadores.remove(lutador)
            self.__tela_lutador.mostra_mensagem('\nLutador excluido com sucesso!\n')

    def lista_lutadores(self):
        if len(self.__lutadores) == 0:
            self.__tela_lutador.mostra_mensagem('\nLista de Lutadores está vazia\n')
        else:
            for lutador in self.__lutadores:
                self.__tela_lutador.mostra_lutador({'nome': lutador.nome, 'idade': lutador.idade, 'id': lutador.id, 'altura': lutador.altura, 'peso': lutador.peso, 'envergadura': lutador.envergadura})

    def lista_lutadores_por_peso(self):
        peso = self.__tela_lutador.pega_peso_lutador()
        if len(self.__lutadores) == 0:
            self.__tela_lutador.mostra_mensagem('\nLista de Lutadores está vazia\n')
        else:
            for lutador in self.__lutadores:
                try:
                    if peso - 1 <= lutador.peso <= peso + 1:
                        self.__tela_lutador.mostra_lutador(
                            {'nome': lutador.nome, 'idade': lutador.idade, 'id': lutador.id, 'altura': lutador.altura,
                            'peso': lutador.peso, 'envergadura': lutador.envergadura})
                    else:
                        raise Exception
                except Exception:
                    self.__tela_lutador.mostra_mensagem('\nNão há nenhum Lutador nessa faixa de peso!\n')

    def alterar_lutador(self):
        self.lista_lutadores()
        lutador = self.__tela_lutador.seleciona_lutador()

        if lutador is not None:
            novos_dados_lutador = self.__tela_lutador.pega_dados_lutador()
            lutador.nome = novos_dados_lutador["nome"]
            lutador.idade = novos_dados_lutador["idade"]
            lutador.id = novos_dados_lutador["id"]
            lutador.altura = novos_dados_lutador["altura"]
            lutador.peso = novos_dados_lutador["peso"]
            lutador.envergadura = novos_dados_lutador["envergadura"]
            self.lista_lutadores()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_lutador, 2: self.lista_lutadores_por_peso, 3: self.lista_lutadores, 4: self.alterar_lutador,
                        5: self.excluir_lutador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_lutador.tela_opcoes()]()
