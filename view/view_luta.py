class TelaLuta:
    def __init__(self, controlador_luta):
        self.__controlador_luta = controlador_luta

    def tela_opcoes(self):
        print("-------- LUTAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Luta")
        print("2 - Listar Todas as Lutas")
        print('3 - Alterar Luta')
        print("4 - Excluir Luta")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opção:", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_luta(self):
        print("-------- DADOS LUTA ----------")
        while True:
            try:
                id = int(input("ID da Luta: "))
                break
            except:
                print('\nDigite um número inteiro\n')

        while True:
            try:
                id_lutador1 = int(input("ID do primeiro Lutador: "))
                break
            except:
                print('\nDigite um número inteiro\n')

        while True:
            try:
                id_lutador2 = int(input("ID do segundo Lutador: "))
                break
            except:
                print('\nDigite um número inteiro\n')

        id_narradores = [int(id_narrador) for id_narrador in input('IDs dos Narradores que deseja selecionar: ').split()]

        data = input('Data da Luta: ')

        while True:
            while True:
                try:
                    id_vencedor = int(input("ID do Lutador vencedor: "))
                    break
                except:
                    print('\nDigite um número inteiro\n')
            try:
                if id_vencedor != id_lutador1 and id_vencedor != id_lutador2:
                    raise Exception
                else:
                    break
            except Exception:
                print('\nO ID do vencedor da Luta precisa ser um dos IDs dos Lutadores cadatrados!\n')

        while True:
            try:
                card = int(input("Card da luta: "))
                break
            except:
                print('\nDigite um número inteiro\n')

        local = input('Local da Luta: ')
        
        return {'id': id, 'id_lutador1': id_lutador1, 'id_lutador2': id_lutador2, 'id_narradores': id_narradores, "data": data,
                "id_vencedor": id_vencedor, "card": card, 'local': local}

    def mostra_luta(self, dados_luta):
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
