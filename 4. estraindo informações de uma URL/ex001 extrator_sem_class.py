#url = 'http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100'
url = " "
url.replace(' ','')
if url == '':
    raise ValueError("A URL está vazia!")


#Separa base e parametros
base_url = url[:url.find('?')]
parametros_url = url[url.find('?')+1:]
print(f'Base da URL : {base_url}')
print(f'Parametros da URL : {parametros_url}')

#busca valor de um parametro
parametro_de_busca = 'quantidade'
indice_parametro = parametros_url.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e = parametros_url.find('&',indice_valor)
if indice_e == -1:
    valor = parametros_url[indice_valor:]
else:
    valor = parametros_url[indice_valor:indice_e]

print(valor)
