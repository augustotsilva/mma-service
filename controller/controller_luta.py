from entity.luta import Luta
from view.view_luta import TelaLuta


class ControladorLuta:
    def __init__(self, controlador_sistema):
        self.__lutas = []
        self.__tela_luta = TelaLuta(self)
        self.__controlador_sistema = controlador_sistema

    def pega_luta_por_id(self, id: int):
        for luta in self.__lutas:
            if luta.id == id:
                return luta
        return None

    def lista_lutas(self):
        if len(self.__lutas) == 0:
            self.__tela_luta.mostra_mensagem('\nLista de Lutas está vazia\n')
        else:
            for luta in self.__lutas:
                lista_narradores = []
                for narrador in luta.narradores:
                    nome_narrador = narrador.nome
                    lista_narradores.append(nome_narrador)
                self.__tela_luta.mostra_luta({'id': luta.id, 'lutador1': luta.lutador1.nome, 'lutador2': luta.lutador2.nome, 'narradores': lista_narradores, 'data': luta.data, 'vencedor': luta.vencedor.nome, 'card': luta.card, 'local': luta.local})

    def incluir_luta(self):
        dados_luta = self.__tela_luta.pega_dados_luta()
        try:
            lutador1 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_lutador1"])
            if lutador1 is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui o ID que você colocou na opção de primeiro Lutador\n')

        try:
            lutador2 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_lutador2"])
            if lutador2 is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui o ID que você colocou na opção de segundo Lutador\n')

        if lutador1.id == lutador2.id:
            return self.__tela_luta.mostra_mensagem('\nImpossível fazer a luta com os mesmos lutadores!\n')

        try:
            vencedor = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_vencedor"])
            if vencedor is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui esse ID\n')

        id = dados_luta['id']

        try:
            narradores = []
            for id_narrador in dados_luta["id_narradores"]:
                narrador = self.__controlador_sistema.controlador_narrador.lista_por_id(id_narrador)
                narradores.append(narrador)
            for narrador in narradores:
                if narrador is None:
                    raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('Algum ID inserido não tem um Narrador correspondente!')

        data = dados_luta['data']
        card = dados_luta['card']
        local = dados_luta['local']

        luta = Luta(id, lutador1, lutador2, narradores, data, vencedor, card, local)
        self.__lutas.append(luta)
        return self.__tela_luta.mostra_mensagem('\nLuta incluida com sucesso!\n')

    def excluir_luta(self):
        if len(self.__lutas) != 0:
            self.lista_lutas()
        else:
            return self.__tela_luta.mostra_mensagem('\nNão é possível exluir uma Luta pois não existe nenhuma\n')

        luta = self.__tela_luta.seleciona_luta()

        if luta is not None:
            self.__lutas.remove(luta)
            self.__tela_luta.mostra_mensagem('\nLuta excluida com sucesso!\n')

    def alterar_luta(self):
        if len(self.__lutas) != 0:
            self.lista_lutas()
        else:
            return self.__tela_luta.mostra_mensagem('\nNão é possível alterar uma Luta pois não existe nenhuma\n')
        
        luta = self.__tela_luta.seleciona_luta()

        if luta is not None:
            novos_dados_luta = self.__tela_luta.pega_dados_luta()
            
            try:
                lutador1 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(novos_dados_luta["id_lutador1"])
                if lutador1 is None:
                    raise Exception
            except Exception:
                return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui o ID que você colocou na opção de primeiro Lutador\n')

            try:
                lutador2 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(novos_dados_luta["id_lutador2"])
                if lutador2 is None:
                    raise Exception
            except Exception:
                return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui o ID que você colocou na opção de segundo Lutador\n')

            if lutador1.id == lutador2.id:
                return self.__tela_luta.mostra_mensagem('\nImpossível fazer a luta com os mesmos lutadores!\n')

            try:
                vencedor = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(novos_dados_luta["id_vencedor"])
                if vencedor is None:
                    raise Exception
            except Exception:
                return self.__tela_luta.mostra_mensagem('\nNenhum Lutador possui esse ID\n')

            try:
                narradores = []
                for id_narrador in novos_dados_luta["id_narradores"]:
                    narradores.append(self.__controlador_sistema.controlador_narrador.lista_por_id(id_narrador))
                for narrador in narradores:
                    if narrador is None:
                        raise Exception
            except Exception:
                return self.__tela_luta.mostra_mensagem('Algum ID inserido não tem um Narrador correspondente!')

            luta.id = novos_dados_luta["id"]
            luta.lutador1 = lutador1
            luta.lutador2 = lutador2
            luta.narradores = narradores
            luta.data = novos_dados_luta["data"]
            luta.vencedor = vencedor
            luta.card = novos_dados_luta["card"]
            luta.local = novos_dados_luta["local"]
            self.lista_lutas()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_luta, 2: self.lista_lutas, 3: self.alterar_luta, 4: self.excluir_luta, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_luta.tela_opcoes()]()
