import time

class TelaCampeonato:
    # Tratar exceções
    def tela_opcoes(self):
        print("-------- CAMPEONATOS ----------")
        print("Escolha a opção")
        print("1 - Incluir campeonato")
        print("2 - Listar campeonatos por dono")
        print("3 - Listar todos os campeonatos")
        print("4 - Excluir campeonato")
        print("0 - Retornar")
        print("-------------------------------")

        opcao = int(input("Escolha a opção: "))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_campeonato(self):
        print("-------- DADOS CAMPEONATO ----------")
        id = input("ID: ")
        nome = input("Nome: ")
        dono = input("Dono: ")
        print("------------------------------------")
        return {"id": id, "nome": nome, "dono": dono}

    def mostra_campeonato(self, dados_campeonato):
        # Tratar exceções
        if dados_campeonato is not None:
            print('ID DO CAMPEONATO: ', dados_campeonato['id'])
            print('NOME DO CAMPEONATO: ', dados_campeonato['nome'])
            print('DONO: ', dados_campeonato['dono'])
            print("------------------------------------")
        else:
            print("Não há campeonatos cadastrados")

    def seleciona_campeonato(self):
        # Tratar as exceções
        id = input('ID do campeonato que deseja selecionar: ')
        return id

    def mostra_mensagem(self, msg):
        time.sleep(0.4)
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
