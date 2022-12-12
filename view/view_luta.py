import PySimpleGUI as sg

class TelaLuta:
    def __init__(self, controlador_luta):
        self.__controlador_luta = controlador_luta
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- LUTAS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Luta', "RD1", key='1')],
        [sg.Radio('Listar todas as Lutas', "RD1", key='2')],
        [sg.Radio('Alterar Luta', "RD1", key='3')],
        [sg.Radio('Excluir Luta', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
        
    def pega_dados_luta(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS LUTA ----------', font=("Helvica", 25))],
        [sg.Text('ID da Luta:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Text('ID do lutador 1', size=(15, 1)), sg.InputText('', key='id_lutador1')],
        [sg.Text('ID do Lutador 2:', size=(15, 1)), sg.InputText('', key='id_lutador2')],
        #[sg.Text('ID dos Narradores da Luta:', size=(15, 1)), sg.InputText('', key='id_narradores')],
        [sg.Text('Data da Luta:', size=(15, 1)), sg.InputText('', key='data')],
        [sg.Text('ID do Lutador vencedor:', size=(15, 1)), sg.InputText('', key='id_vencedor')],
        [sg.Text('Card:', size=(15, 1)), sg.InputText('', key='card')],
        [sg.Text('Local:', size=(15, 1)), sg.InputText('', key='local')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Lutas').Layout(layout)
        
        button, values = self.open()
        
        id = int(values['id'])
        id_lutador1 = int(values['id_lutador1'])
        id_lutador2 = int(values['id_lutador1'])
        #id_narradores = [int(id_narrador) for id_narrador in values['id_narradores'].split()]
        data = values['data']
        id_vencedor = int(values['id_vencedor'])
        card = int(values['card'])
        local = values['local']
        try:
            if (id_vencedor != id_lutador1) and (id_vencedor != id_lutador2):
                raise Exception
        except Exception:
            self.mostra_mensagem('O ID do lutador vencedor precisa ser de um dos lutadores cadastrados')
        self.close()
        
        return {'id': id, 'id_lutador1': id_lutador1, 'id_lutador2': id_lutador2, #'id_narradores': id_narradores,
                "data": data, "id_vencedor": id_vencedor, "card": card, 'local': local}

    def mostra_luta(self, dados_luta):
        string_todas_lutas = ""
        for dado in dados_luta:
            string_todas_lutas = string_todas_lutas + "ID DA LUTA: " + str(dado["id"]) + '\n'
            string_todas_lutas = string_todas_lutas + "PRIMEIRO LUTADOR: " + str(dado["lutador1"]) + '\n'
            string_todas_lutas = string_todas_lutas + "SEGUNDO LUTADOR: " + str(dado["lutador2"]) + '\n'
            #for narrador in dados_luta['narradores']:
                #string_todas_lutas = string_todas_lutas + "NARRADOR DA LUTA: " + str(narrador) + '\n'
            string_todas_lutas = string_todas_lutas + "NARRADORES DA LUTA: " + str(dado["narradores"]) + '\n'
            string_todas_lutas = string_todas_lutas + "DATA DA LUTA: " + str(dado["data"]) + '\n'
            string_todas_lutas = string_todas_lutas + "VENCEDOR DA LUTA: " + str(dado["vencedor"]) + '\n'
            string_todas_lutas = string_todas_lutas + "CARD DA LUTA: " + str(dado["card"]) + '\n'
            string_todas_lutas = string_todas_lutas + "LOCAL DA LUTA: " + str(dado["local"]) + '\n\n'

        sg.Popup('-------- LISTA DE LUTAS ----------', string_todas_lutas)

    def seleciona_luta(self):
        while True:
            try:
                id = int(input('ID da Luta que deseja selecionar: '))
                break
            except:
                print('Digite um número inteiro')
        try:
            luta = self.__controlador_luta.pega_luta_por_id(id)
            if luta is None:
                raise Exception
            else:
                return luta
        except Exception:
            print("\nEssa Luta não existe\n")
            return luta

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
