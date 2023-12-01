palavras_quantidade  = {"Guilherme" : 1,"cachorro" : 2,"nome" : 2,"vindo" : 1}
print('Chaves: ')
for chaves in palavras_quantidade.keys():
    print(chaves)
print()
print('Valores: ')
for valor in palavras_quantidade.values():
    print(valor)
print()
print('Itens: ')
for item in palavras_quantidade.items():
    print(item)
print()
print('Chaves e Valores: ')
for chave,valor in palavras_quantidade.items():
    print(chave,'=',valor)
print()
