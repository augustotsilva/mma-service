from Telas.view_luta import *
from Entidades.luta import *


class ControladorLuta:
    def __init__(self, controlador_sistema):
        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema
        self.__lutas = []
        self.__tela_luta = TelaLuta(self)
        
    def pega_luta_por_id(self, id: int):
        for luta in self.__lutas:
            if luta.id == id:
                return luta
        return None
    
    def lista_lutas(self):
        if len(self.__lutas) == 0:
            self.__tela_luta.mostra_mensagem('Lista de Lutas está vazia')
        else:
            for luta in self.__lutas:
                self.__tela_luta.mostra_luta({'id': luta.id, 'lutador1': luta.lutador1, 'lutador2': luta.lutador2, 'narradores': luta.narradores, 'data': luta.data, 'vencedor': luta.vencedor, 'card': luta.card, 'local': luta.local})
            
    def lista_lutas_por_categoria(self, categoria: float):
        self.__tela_luta.le_num_real(categoria)
        if len(self.__lutas) == 0:
            self.__tela_luta.mostra_mensagem('Lista de Lutas está vazia')
        else:
            for luta in self.__lutas:
                if categoria - 0.5 < luta.lutador1.peso and luta.lutador2.peso < categoria + 0.5:
                    self.__tela_luta.mostra_luta({'id': luta.id, 'lutador1': luta.lutador1, 'lutador2': luta.lutador2, 'narradores': luta.narradores, 'data': luta.data, 'vencedor': luta.vencedor, 'card': luta.card, 'local': luta.local})
    
    def incluir_luta(self):
        dados_luta = self.__tela_luta.pega_dados_luta()
        luta = self.pega_luta_por_id(dados_luta['id'])
        try:
            if luta != None:
                raise KeyError
            self.__lutas.append(luta)
        except:
            self.__tela_luta.mostra_mensagem("Luta já existente!")
    
    def excluir_luta(self):
        self.lista_lutas()
        id_luta = self.__tela_luta.seleciona_luta()
        luta = self.pega_luta_por_id(id_luta)
        
        if luta is not None:
            self.__lutas.remove(luta)
            self.lista_lutas()
        else:
            self.__tela_luta.mostra_mensagem("ATENÇÃO: Luta não existente")
    
    def alterar_luta(self):
        self.lista_lutas()
        id_luta = self.__tela_luta.seleciona_luta()
        luta = self.pega_luta_por_id(id_luta)

        if luta is not None:
            novos_dados_luta = self.__tela_luta.pega_dados_luta()
            luta.id = novos_dados_luta["id"]
            luta.lutador1 = novos_dados_luta["lutador1"]
            luta.lutador2 = novos_dados_luta["lutador2"]
            luta.narradores = novos_dados_luta["narradores"]
            luta.data = novos_dados_luta["data"]
            luta.vencedor = novos_dados_luta["vencedor"]
            luta.card = novos_dados_luta["card"]
            luta.local = novos_dados_luta["local"]
            self.lista_lutas()
        else:
            self.__tela_lutador.mostra_mensagem("ATENCAO: Luta não existente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        # tratar exceções
        lista_opcoes = {1: self.incluir_luta, 2: self.lista_lutas_por_categoria, 3: self.lista_lutas, 4: self.excluir_luta, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_luta.tela_opcoes()]()