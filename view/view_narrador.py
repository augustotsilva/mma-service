class TelaNarrador:
    # Tratar exceções
    def tela_opcoes(self):
        print("-------- NARRADORES ----------")
        print("Escolha a opção")
        print("1 - Incluir narrador")
        print("2 - Listar narrador por id")
        print("3 - Listar todos os narradores")
        print("4 - Alterar narrador")
        print("5 - Excluir narrador")
        print("0 - Retornar")
        print("-------------------------------")

        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_narrador(self):
        print("-------- DADOS NARRADOR ----------")
        id = self.le_num_inteiro("ID: ")
        nome = self.le_string("Nome: ")
        idade = self.le_num_inteiro("Idade: ")
        temperamento = self.le_string("Temperamento: ")
        print("------------------------------------")
        return {"id": id, "nome": nome, "idade": idade, "temperamento": temperamento}

    def mostra_narrador(self, dados_narrador):
        # Tratar exceções
        if dados_narrador is not None:
            print("------------------------------------")
            print('ID DO NARRADOR: ', dados_narrador['id'])
            print('NOME DO NARRADOR: ', dados_narrador['nome'])
            print('IDADE: ', dados_narrador['idade'])
            print('TEMPERAMENTO: ', dados_narrador['temperamento'])
            print("------------------------------------")
        else:
            print("Não há narradores cadastrados")

    def seleciona_narrador(self):
        # Tratar as exceções
        id = self.le_num_inteiro('ID do narrador que deseja selecionar: ')
        return id

    def mostra_mensagem(self, msg):
        print("--------------------------------------------------")
        print(msg)
        print("--------------------------------------------------")

    @staticmethod
    def le_num_inteiro(mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor inválido!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    @staticmethod
    def le_string(mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                if valor_lido is None or '':
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Valor inválido!")
