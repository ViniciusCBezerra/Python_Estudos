class ContaCorrente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return f"Codigo {self.codigo} Saldo {self.saldo} <<"

def deposita_em_todas_as_contas(contas):
    for conta in contas:
        conta.deposita(100)

#Aula 1
print('Aula 1')
print()

conta_gui = ContaCorrente(29)
conta_gui.deposita(150)
print(conta_gui)
print()

conta_dani = ContaCorrente(47)
conta_dani.deposita(1000)
print(conta_dani)
print()

contas = [conta_gui,conta_dani]
print(contas)
print()

for conta in contas:
    print(conta)
print()

contas[0].deposita(100)
print(contas[0])
#Aula 2
print('Aula 2')
print()

contas = [conta_gui,conta_dani]
deposita_em_todas_as_contas(contas)
#agencia bancaria
contas.insert(0,76)

#deposita_em_todas_as_contas(contas) #nao seria possivel
#Aula 2 Parte 2

guilherme = ('Guilherme',31,1992)
daniela = ('Daniela',23,2000)

usuarios = [guilherme,daniela]
usuarios.append(('Paulo',12,2011))
print(usuarios)

#Aula 3
print('Aula 3')
print()

contas = (conta_gui,conta_dani)
for conta in contas:
    print(conta)

