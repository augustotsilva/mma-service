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

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_campeonato(self):
        print("-------- DADOS CAMPEONATO ----------")
        id = input("ID: ")
        nome = input("Nome: ")
        idade = input("Dono: ")

        return { "id": id, "nome": nome, "dono": dono }
    
    def mostra_campeonato(self, dados_campeonato):
        # Tratar exceções
        print('ID DO CAMPEONATO: ', dados_campeonato['id'])
        print('NOME DO CAMPEONATO: ', dados_campeonato['nome'])
        print('DONO: ', dados_campeonato['idade'])
        print()
        
    def seleciona_lutador(self):
        # Tratar as exceções
        id = input('ID do campeonato que deseja selecionar: ')
        return id
    
    def mostra_mensagem(self, msg):
        print(msg)

