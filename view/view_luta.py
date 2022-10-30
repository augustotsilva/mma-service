class TelaLuta:
    def __init__(self, controlador_luta):
        self.__controlador_luta = controlador_luta

    def tela_opcoes(self):
        print("-------- LUTAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Luta")
        print("2 - Listar Lutas por Categoria")
        print("3 - Listar Todas as Lutas")
        print('4 - Alterar Luta')
        print("5 - Excluir Luta")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5])
        return opcao

    def pega_dados_luta(self):
        # Falta a exceção dos Narradores
        print("-------- DADOS LUTA ----------")
        while True:
            try:
                id = int(input("ID da Luta: "))
                break
            except:
                print('Digite um número inteiro')

        while True:
            try:
                id_lutador1 = int(input("ID do primeiro Lutador: "))
                break
            except:
                print('Digite um número inteiro')

        while True:
            try:
                id_lutador2 = int(input("ID do segundo Lutador: "))
                break
            except:
                print('Digite um número inteiro')

        #narradores = list(input('Narradores: '))

        data = input('Data da Luta: ')

        while True:
            while True:
                try:
                    id_vencedor = int(input("ID do Lutador vencedor: "))
                    break
                except:
                    print('Digite um número inteiro')
            try:
                if id_vencedor != id_lutador1 and id_vencedor != id_lutador2:
                    raise Exception
                else:
                    break
            except Exception:
                print('O ID do vencedor da Luta precisa ser um dos IDs dos Lutadores cadatrados!')

        while True:
            try:
                card = int(input("Card da luta: "))
                break
            except:
                print('Digite um número inteiro')

        local = self.le_letra('Local da Luta: ')

        return {'id': id, 'id_lutador1': id_lutador1, 'id_lutador2': id_lutador2, "data": data,
                "id_vencedor": id_vencedor, "card": card, 'local': local}

    def mostra_luta(self, dados_luta):
        print()
        print('ID DA LUTA: ', dados_luta['id'])
        print('PRIMEIRO LUTADOR DA LUTA: ', dados_luta['lutador1'])
        print('SEGUNDO LUTADOR DA LUTA: ', dados_luta['lutador2'])
        #print('NARRADORES DA LUTA: ', dados_luta['narradores'])
        print('DATA DA LUTA: ', dados_luta['data'])
        print('VENCEDOR DA LUTA: ', dados_luta['vencedor'])
        print('CARD DA LUTA: ', dados_luta['card'])
        print('LOCAL DA LUTA: ', dados_luta['local'])
        print("\n")

    def pega_categoria_luta(self):
        # Falta coisa
        while True:
            try:
                peso = float(input('Faixa de peso que deseja selecionar: '))
                break
            except ValueError:
                print('Insira um valor numérico ')

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
            print("Essa Luta não existe")
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

    def le_letra(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                if valor_lido.isalpha():
                    return valor_lido
                else:
                    raise ValueError
            except ValueError:
                print('Digite uma palavra')
