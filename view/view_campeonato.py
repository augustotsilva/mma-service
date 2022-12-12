class TelaCampeonato:
    # Tratar exceções
    def tela_opcoes(self):
        print("-------- CAMPEONATOS ----------")
        print("Escolha a opção")
        print("1 - Incluir campeonato")
        print("2 - Listar campeonatos por id")
        print("3 - Listar campeonatos por dono")
        print("4 - Listar todos os campeonatos")
        print("5 - Alterar campeonato")
        print("6 - Excluir campeonato")
        print("7 - Incluir luta ao campeonato")
        print("8 - Excluir luta do campeonato")
        print("9 - Listar lutas do campeonato")
        print("0 - Retornar")
        print("-------------------------------")

        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_campeonato(self):
        print("-------- DADOS CAMPEONATO ----------")
        id = self.le_num_inteiro("ID: ")
        nome = self.le_string("Nome: ")
        dono = self.le_string("Dono: ")
        print("------------------------------------")
        return {"id": id, "nome": nome, "dono": dono}

    def mostra_campeonato(self, dados_campeonato):
        # Tratar exceções
        if dados_campeonato is not None:
            print("------------------------------------")
            print('ID DO CAMPEONATO: ', dados_campeonato['id'])
            print('NOME DO CAMPEONATO: ', dados_campeonato['nome'])
            print('DONO: ', dados_campeonato['dono'])
            print("------------------------------------")
        else:
            print("Não há campeonatos cadastrados")

    def seleciona_campeonato(self):
        # Tratar as exceções
        id = self.le_num_inteiro('ID do campeonato que deseja selecionar: ')
        return id

    def seleciona_luta(self):
        # Tratar as exceções
        id = self.le_num_inteiro('ID da luta que deseja selecionar ao campeonato: ')
        return id

    def seleciona_dono(self):
        # Tratar as exceções
        dono = self.le_string('Nome do dono que deseja selecionar: ')
        return dono

    def mostra_mensagem(self, msg):
        print("--------------------------------------------------")
        print(msg)
        print("--------------------------------------------------")

    def mostra_luta_campeonato(self, dados_luta):
        print()
        print('ID DA LUTA: ', dados_luta['id'])
        print('PRIMEIRO LUTADOR DA LUTA: ', dados_luta['lutador1'])
        print('SEGUNDO LUTADOR DA LUTA: ', dados_luta['lutador2'])
        print('NARRADORES DA LUTA: ', end='')
        for narrador in dados_luta['narradores']:
            print(narrador, end=' ')
            print()
        print('DATA DA LUTA: ', dados_luta['data'])
        print('VENCEDOR DA LUTA: ', dados_luta['vencedor'])
        print('CARD DA LUTA: ', dados_luta['card'])
        print('LOCAL DA LUTA: ', dados_luta['local'])
        print("\n")

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
