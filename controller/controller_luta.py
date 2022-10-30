from view.view_luta import TelaLuta
from entity.luta import Luta
from controller.controller_lutador import ControladorLutador

class ControladorLuta:
    def __init__(self, controlador_sistema):
        self.__lutas = []
        self.__tela_luta = TelaLuta(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_lutador = ControladorLutador(self)
        
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
                self.__tela_luta.mostra_luta({'id': luta.id, 'lutador1': luta.lutador1.nome, 'lutador2': luta.lutador2.nome, 'data': luta.data, 'vencedor': luta.vencedor.nome, 'card': luta.card, 'local': luta.local})
            
    def lista_lutas_por_categoria(self):
        categoria = self.__tela_luta.pega_categoria_luta()
        self.__tela_luta.le_num_real(categoria)
        if len(self.__lutas) == 0:
            self.__tela_luta.mostra_mensagem('Lista de Lutas está vazia')
        else:
            for luta in self.__lutas:
                if categoria - 0.5 < luta.lutador1.peso and luta.lutador2.peso < categoria + 0.5:
                    self.__tela_luta.mostra_luta({'id': luta.id, 'lutador1': luta.lutador1, 'lutador2': luta.lutador2, 'narradores': luta.narradores, 'data': luta.data, 'vencedor': luta.vencedor, 'card': luta.card, 'local': luta.local})
    
    '''
    def incluir_luta(self):
        dados_luta = self.__tela_luta.pega_dados_luta()
        luta = self.pega_luta_por_id(dados_luta['id'])
        try:
            if luta != None:
                raise KeyError
            luta = Luta(dados_luta['id'], dados_luta['lutador1'], dados_luta['lutador2'], dados_luta['data'], dados_luta['vencedor'], dados_luta['card'], dados_luta['local'])
            self.__lutas.append(luta)
        except:
            self.__tela_luta.mostra_mensagem("Luta já existente!")
    '''
    
    def excluir_luta(self):
        self.lista_lutas()
        luta = self.__tela_luta.seleciona_luta()
        
        if luta is not None:
            self.__lutas.remove(luta)
            self.__tela_luta.mostra_mensagem('Luta excluido com sucesso!')
    
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
        lista_opcoes = {1: self.incluir_luta, 2: self.lista_lutas_por_categoria, 3: self.lista_lutas, 4: self.excluir_luta, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_luta.tela_opcoes()]()
    
    def verifica_lutador(self, id):
        lutador = self.__controlador_lutador.pega_lutador_por_id(id)
        return lutador
    
    def incluir_luta(self):
        dados_luta = self.__tela_luta.pega_dados_luta()

        try:
            lutador1 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_lutador1"])
            if lutador1 is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('Nenhum Lutador possui o ID que você colocou na opção de primeiro Lutador')

        try:
            lutador2 = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_lutador2"])
            if lutador2 is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('Nenhum Lutador possui o ID que você colocou na opção de segundo Lutador')
                

        try:
            vencedor = self.__controlador_sistema.controlador_lutador.pega_lutador_por_id(dados_luta["id_vencedor"])
            if vencedor is None:
                raise Exception
        except Exception:
            return self.__tela_luta.mostra_mensagem('Nenhum Lutador possui esse ID')
                
        id = dados_luta['id']
        data = dados_luta['data']
        card = dados_luta['card']
        local = dados_luta['local']
        
        luta = Luta(id, lutador1, lutador2, data, vencedor, card, local)
        self.__lutas.append(luta)
        return self.__tela_luta.mostra_mensagem('Luta incluida com sucesso!')
