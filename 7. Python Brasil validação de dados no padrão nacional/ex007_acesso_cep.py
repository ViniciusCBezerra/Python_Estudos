import requests
from ex007_cep import BuscaEndereco

cep = '03918000'
objeto_cep = BuscaEndereco(cep)


bairro,cidade,uf = objeto_cep.acessa_via_cep()
print(f'Bairro: {bairro}')
print(f'Cidade: {cidade}')
print(f'Uf: {uf}')
