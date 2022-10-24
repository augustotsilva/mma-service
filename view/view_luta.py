class TelaLuta:
    def tela_opcoes(self):
        print("-------- LUTAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Luta")
        print("2 - Listar Lutas por Categoria")
        print("3 - Listar Todas as Lutas")
        print("4 - Excluir Luta")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opção:", [0, 1, 2, 3, 4])
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
            while True:
                try:
                    id_lutador1 = int(input("ID do primeiro Lutador: "))
                    break
                except:
                    print('Digite um número inteiro')
            try:
                lutador1 = self.verifica_lutador(id_lutador1)
                break
            except Exception:
                print('Esse Lutador não existe')

        while True:
            while True:
                try:
                    id_lutador2 = int(input("ID do primeiro Lutador: "))
                    break
                except:
                    print('Digite um número inteiro')
            try:
                lutador2 = self.verifica_lutador(id_lutador2)
                break
            except Exception:
                print('Esse Lutador não existe')

        narradores = list(input('Narradores: '))
        
        data = self.le_letra(input('Data da Luta: '))

        while True:
            while True:
                try:
                    id_vencedor = int(input("ID do Lutador vencedor: "))
                    break
                except:
                    print('Digite um número inteiro')
            try:
                vencedor = self.verifica_lutador(id_vencedor)
                break
            except Exception:
                print('Esse Lutador não existe')

        while True:
            try:
                card = int(input("Card da luta: "))
                break
            except:
                print('Digite um número inteiro')
                
        local = self.le_letra(input('Local da Luta: '))

        return {"id": id, "lutador1": lutador1, 'lutador2': lutador2, "narradores": narradores, "data": data,
                "vencedor": vencedor, "card": card, 'local': local}

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
                try:
                    id = int(input('ID da Luta que deseja selecionar: '))
                    break
                except:
                    print('Digite um número inteiro')
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
                valor_errado = float(valor_lido)
                print('Você digitou um número, e não uma palavra')
            except ValueError:
                return mensagem

    def verifica_lutador(self, id):
        if self.__controlador_lutador.pega_lutador_por_id(id) is None:
            raise Exception
        else:
            return self.__controlador_lutador.pega_lutador_por_id(id)

