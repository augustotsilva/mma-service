class TelaLutador:
    def __init__(self, controlador_lutador):
        self.__controlador_lutador = controlador_lutador

    def tela_opcoes(self):
        print("-------- LUTADORES ----------")
        print("Escolha a opção")
        print("1 - Incluir Lutador")
        print("2 - Listar Lutadores por Peso")
        print("3 - Listar Todos Lutadores")
        print("4 - Excluir Lutador")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opção:", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_lutador(self):
        print("-------- DADOS LUTADOR ----------")
        nome = self.le_letra("Nome: ")
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except:
                print('Insira um valor inteiro')
        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print('Insira um valor inteiro')
        altura = self.le_num_real('Altura: ')
        peso = self.le_num_real('Peso: ')
        envergadura = self.le_num_real('Envergadura: ')

        return {'nome': nome, 'idade': idade, 'id': id, 'altura': altura, 'peso': peso, 'envergadura': envergadura}

    def mostra_lutador(self, dados_lutador):
        print('NOME DO LUTADOR: ', dados_lutador['nome'])
        print('IDADE DO LUTADOR: ', dados_lutador['idade'])
        print('ID DO LUTADOR: ', dados_lutador['id'])
        print('ALTURA DO LUTADOR: ', dados_lutador['altura'])
        print('PESO DO LUTADOR: ', dados_lutador['peso'])
        print('ENVERGADURA DO LUTADOR: ', dados_lutador['envergadura'])
        print("\n")

    def seleciona_lutador(self):
        while True:
            id = input('ID do Lutador que deseja selecionar: ')
            try:
                id_int = int(id)
                break
            except:
                print('Você não está digitando um valor válido')
        try:
            lutador = self.__controlador_lutador.pega_lutador_por_id(id_int)
            if lutador is None:
                raise Exception
            else:
                return lutador
        except Exception:
            print("Esse Lutador não existe")
            return lutador
    
    def pega_peso_lutador(self):
        while True:
            try:
                peso = float(input('Faixa de peso que deseja selecionar: '))
                return peso
            except ValueError:
                print('Insira um valor numérico ')

    def mostra_mensagem(self, msg):
        print(msg)

    @property
    def controlador_lutador(self):
        return self.__controlador_lutador

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

    def le_num_real(self, mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                return valor_float
            except ValueError:
                print("Digite um número")

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
