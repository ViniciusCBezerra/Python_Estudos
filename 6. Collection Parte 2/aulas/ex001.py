usuarios_data_science = {15,23,34,56}
usuarios_introducao_machine = {13,23,56,42}
# usuarios_total = usuarios_introducao_machine.copy()
# usuarios_total.extend(usuarios_data_science)
# usuarios_total = set(usuarios_total)
# print(usuarios_total)
# while True:
#     posicao = int(input('Digite a posição dos usuarios que deseja ver: ( 1 , 2 , 3 , 4 , 5 , 6 )  '))
#     u = 0
#     for usuario in usuarios_total:
#         u += 1
#         if u == posicao:
#             print(f'>> O valor da posição {u} é: {usuario} <<')
#     while True:
#         ver_mais = str(input('Deseja ver mais alguma posição? (S/N)')).upper().strip()
#         if ver_mais[0] in 'SN':
#             break
#     if ver_mais[0] == 'F':
#         break
#PARTE 2
# usuarios = {1,5,31,23,45,67,13}
# usuarios.add(76)
# usuarios = frozenset(usuarios)
# print(usuarios)
#PARTE 3
meu_texto = "Bem vindo meu nome é vinicius eu gosto do meu nome e gosto de ir à igreja todo domingo e sabado quero ser musico tocando flauta transversal"
print(set(meu_texto.split()))

