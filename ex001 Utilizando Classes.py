class Cliente:
    def __init__(self , nome , email , plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic' , 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano invalido')

    def mudar_plano(self, novo):
        if novo in self.lista_planos:
            self.plano = novo
        else:
            print('Plano invalido')

    def ver_filme(self, filme,plano_filme):
        if self.plano == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver Filme {filme}')
        elif self.plano =='basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para ver esse filme')
        else:
            print('Plano invalido')


cli=Cliente('vini' , 'vini@gmail' , 'basic')
print(cli.plano)
cli.ver_filme("Harry potter", "premium")

cli.mudar_plano('premium')
print(cli.plano)
cli.ver_filme("Harry potter", "premium")