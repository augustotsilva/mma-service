from DAO.narrador_dao import NarradorDAO
from entity.narrador import Narrador
from view.view_narrador import TelaNarrador


class ControladorNarrador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_narrador = TelaNarrador()
        self.__narradorDAO = NarradorDAO()
        self.__narradores = []

    def lista_por_id(self, id: int):
        return self.__narradorDAO.get(id)

    def lista_narrador_por_id(self):
        if not self.__narradorDAO.get_all():
            return self.__tela_narrador.mostra_mensagem("Não há narradores registrados")
        narrador = self.lista_por_id(self.__tela_narrador.seleciona_narrador())
        return self.__tela_narrador.mostra_narrador(self.convert_to_view_object(narrador))

    def lista_narradores(self):
        narradores = self.__narradorDAO.get_all()
        if narradores:
            for narrador in narradores:
                self.__tela_narrador.mostra_narrador(self.convert_to_view_object(narrador))
        else:
            self.__tela_narrador.mostra_mensagem("Não há narradores cadastrados")

    def incluir_narrador(self):
        dados_narrador = self.__tela_narrador.pega_dados_narrador()
        if self.lista_por_id(dados_narrador['id']) is not None:
            self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador já existente")
        else:
            narrador = Narrador(dados_narrador["id"], dados_narrador["nome"], dados_narrador["idade"],
                                dados_narrador["temperamento"])
            self.__narradorDAO.add(narrador)
            self.__tela_narrador.mostra_mensagem("Narrador inserido com sucesso")

    def alterar_narrador(self):
        self.lista_narradores()
        narradores = self.__narradorDAO.get_all()
        if narradores:
            id_narrador = self.__tela_narrador.seleciona_narrador()
            narrador = self.lista_por_id(id_narrador)
            if narrador is not None:
                novos_dados_narrador = self.__tela_narrador.pega_dados_narrador()
                narrador.id = novos_dados_narrador["id"]
                narrador.nome = novos_dados_narrador["nome"]
                narrador.idade = novos_dados_narrador["idade"]
                narrador.temperamento = novos_dados_narrador["temperamento"]
                self.__narradorDAO.update(narrador)
                self.lista_narradores()
                self.__tela_narrador.mostra_mensagem("Narrador alterado com sucesso")
            else:
                self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador não existente")

    def excluir_narrador(self):
        self.lista_narradores()
        narradores = self.__narradorDAO.get_all()
        if narradores:
            id_narrador = self.__tela_narrador.seleciona_narrador()
            narrador = self.lista_por_id(id_narrador)
            if narrador is not None:
                self.__narradorDAO.remove(narrador.id)
                self.__tela_narrador.mostra_mensagem("Narrador excluído com sucesso")
            else:
                self.__tela_narrador.mostra_mensagem("ATENÇÃO: Narrador não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_narrador, 2: self.lista_narrador_por_id, 3: self.lista_narradores,
                        4: self.alterar_narrador, 5: self.excluir_narrador, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_narrador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @staticmethod
    def convert_to_view_object_list(narradores):
        view_object_list = []
        for narrador in narradores:
            view_object_list.append({"id": narrador.id, "nome": narrador.nome, "idade": narrador.idade,
                                     "temperamento": narrador.temperamento})
        return view_object_list

    @staticmethod
    def convert_to_view_object(narrador):
        return {"id": narrador.id, "nome": narrador.nome, "idade": narrador.idade,
                "temperamento": narrador.temperamento}
