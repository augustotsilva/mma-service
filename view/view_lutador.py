import PySimpleGUI as sg


class TelaLutador:
    def __init__(self, controlador_lutador):
        self.__controlador_lutador = controlador_lutador
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
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- LUTADORES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Lutador', "RD1", key='1')],
            [sg.Radio('Listar Lutadores por Peso', "RD1", key='2')],
            [sg.Radio('Listar Todos Lutadores', "RD1", key='3')],
            [sg.Radio('Alterar Lutadores', "RD1", key='4')],
            [sg.Radio('Excluir Lutador', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Lutadores').Layout(layout)

    def pega_dados_lutador(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS Lutador ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Text('Id:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('Altura:', size=(15, 1)), sg.InputText('', key='altura')],
            [sg.Text('Peso:', size=(15, 1)), sg.InputText('', key='peso')],
            [sg.Text('Envergadura:', size=(15, 1)), sg.InputText('', key='envergadura')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Lutadores').Layout(layout)

        button, values = self.open()

        nome_e = values['nome']
        try:
            nome = int(nome_e)
            self.mostra_mensagem('Nome inválido')
        except:
            nome = nome_e

        try:
            idade = int(values['idade'])
        except:
            self.mostra_mensagem('Idade deve ser um número inteiro')

        try:
            id = int(values['id'])
        except:
            self.mostra_mensagem('O ID do lutador deve ser um número inteiro')

        try:
            altura = float(values['altura'])
        except:
            self.mostra_mensagem('A altura do lutador deve ser um valor numérico')

        try:
            peso = float(values['peso'])
        except:
            self.mostra_mensagem('O peso do lutador deve ser um valor numérico')

        try:
            envergadura = float(values['envergadura'])
        except:
            self.mostra_mensagem('A envergadura do lutador deve ser um valor numérico')

        try:
            return {'nome': nome, 'idade': idade, 'id': id, 'altura': altura, 'peso': peso, 'envergadura': envergadura}
        except:
            return None

    def mostra_lutador(self, dados_lutador):
        string_todos_lutadores = ""
        for dado in dados_lutador:
            string_todos_lutadores = string_todos_lutadores + "NOME DO LUTADOR: " + dado["nome"] + '\n'
            string_todos_lutadores = string_todos_lutadores + "IDADE DO LUTADOR: " + str(dado["idade"]) + '\n'
            string_todos_lutadores = string_todos_lutadores + "ID DO LUTADOR: " + str(dado["id"]) + '\n'
            string_todos_lutadores = string_todos_lutadores + "ALTURA DO LUTADOR: " + str(dado["altura"]) + '\n'
            string_todos_lutadores = string_todos_lutadores + "PESO DO LUTADOR: " + str(dado["peso"]) + '\n'
            string_todos_lutadores = string_todos_lutadores + "ENVERGADURA DO LUTADOR: " + str(
                dado["envergadura"]) + '\n\n'

        sg.Popup('-------- LISTA DE LUTADORES ----------', string_todos_lutadores)

    def seleciona_lutador(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR LUTADOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do Lutador que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Lutador').Layout(layout)

        button, values = self.open()
        try:
            id_int = int(values['id'])
        except:
            self.mostra_mensagem('ID deve ser um número inteiro')
            self.close()
        try:
            lutador = self.__controlador_lutador.pega_lutador_por_id(int(values['id']))
            if lutador is None:
                raise Exception
            else:
                return lutador
        except Exception:
            self.mostra_mensagem('Esse lutador não existe')
        self.close()
        return lutador

    def pega_peso_lutador(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR LUTADOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite a faixa de peso que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Faixa de Peso:', size=(15, 1)), sg.InputText('', key='faixa_peso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Peso do Lutador').Layout(layout)

        button, values = self.open()

        peso = float(values['faixa_peso'])
        return peso

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
