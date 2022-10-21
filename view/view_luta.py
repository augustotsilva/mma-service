from controller.controller_luta import *


class TelaLuta:
    def __init__(self, controlador_luta):
        if isinstance(controlador_luta, ControladorLuta):
            self.__controlador_luta = controlador_luta
        
    def tela_opcoes(self):
        print("-------- LUTAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Luta")
        print("2 - Listar Lutas por Categoria")
        print("3 - Listar Todas as Lutas")
        print("4 - Excluir Luta")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opção:", [0,1,2,3,4])
        return opcao
    
    def pega_dados_luta(self):
        # Falta exceções
        print("-------- DADOS LUTA ----------")
        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print('Insira um valor inteiro')             
        lutador1 = input("Primeiro Lutador: ")
        lutador2 = input("Segundo Lutador: ")
        narradores = list(input('Narradores: '))
        data = self.le_letra(input('Data da Luta: '))
        vencedor = input('Vencedor da Luta: ')
        while True:
            try:
                card = int(input("Card: "))
                break
            except:
                print('Insira um valor inteiro')
        local = self.le_letra(input('Local da Luta: '))

        return {"id": id, "lutador1": lutador1, 'lutador2': lutador2, "narradores": narradores, "data": data, "vencedor": vencedor, "card" : card, 'local': local}

    def mostra_luta(self, dados_luta):
        print('ID DA LUTA: ', dados_luta['id'])
        print('PRIMEIRO LUTADOR DA LUTA: ', dados_luta['lutador1'])
        print('SEGUNDO LUTADOR DA LUTA: ', dados_luta['lutador2'])
        print('NARRADORES DA LUTA: ', dados_luta['narradores'])
        print('DATA DA LUTA: ', dados_luta['data'])
        print('VENCEDOR DA LUTA: ', dados_luta['vencedor'])
        print('CARD DA LUTA: ', dados_luta['card'])
        print('LOCAL DA LUTA: ', dados_luta['local'])
        print()
        
    def seleciona_luta(self):
        while True:
            while True:
                id = input('ID da Luta que deseja selecionar: ')
                try:
                    id_int = int(id)
                    break
                except ValueError:
                    print('Você não está digitando um valor válido')
            try:
                id_valido = self.__controlador_luta.pega_luta_por_id(id_int)
                if id_valido is None:
                    raise Exception
                else:
                    return id_valido
            except Exception:
                print("Essa Luta não existe")

    def mostra_mensagem(self, msg):
        print(msg)

    @property
    def controlador_luta(self):
        return self.__controlador_luta
    
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def le_letra(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_errado = float(valor_lido)
                print('Você digitou um número, e não uma palavra')
            except ValueError:
                return valor_lido
