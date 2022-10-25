class TelaSistema:
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

    def tela_opcoes(self):
        print("-------- Sistema ---------")
        print("Escolha sua opção")
        print("1 - Lutas")
        print("2 - Lutadores")
        print("3 - Narradores")
        print("4 - Campeonato")
        print("0 - Finalizar sistema")
        print("--------------------------")
        opcao = self.le_num_inteiro("Escolha a opção:", [0, 1, 2, 3, 4])
        return opcao
