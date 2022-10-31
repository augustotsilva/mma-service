import time


class TelaNarrador:
    # Tratar exceções
    def tela_opcoes(self):
        print("-------- NARRADORES ----------")
        print("Escolha a opção")
        print("1 - Incluir narrador")
        print("2 - Listar narradores por dono")
        print("3 - Listar todos os narradores")
        print("4 - Excluir narrador")
        print("0 - Retornar")
        print("-------------------------------")

        opcao = int(input("Escolha a opção: "))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_narradores(self):
        print("-------- DADOS NARRADOR ----------")
        id = input("ID: ")
        nome = input("Nome: ")
        idade = input('Idade:')
        temperamento = input("Temperamento: ")
        print("------------------------------------")
        return {'id': id, 'nome': nome, 'idade': idade, 'temperamento': temperamento}

    def mostra_narrador(self, dados_narrador):
        # Tratar exceções
        print("------------------------------------")
        print('ID DO NARRADOR: ', dados_narrador['id'])
        print('NOME DO NARRADOR: ', dados_narrador['nome'])
        print('Idade: ', dados_narrador['idade'])
        print('Temperamento: ', dados_narrador['temperamento'])
        print("------------------------------------")

    def seleciona_narrador(self):
        # Tratar as exceções
        id = input('ID do narrador que deseja selecionar: ')
        return id

    def mostra_mensagem(self, msg):
        print(msg)

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
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
