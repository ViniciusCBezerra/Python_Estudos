import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return 'URL: ' + self.url + '\n' + 'URL Base: ' + self.get_url_base() + '\n' + 'URL Parâmetros: ' + self.get_url_parametros()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia!')

        padrao_url = re.compile('(http(s)?://)?(www.)?(bytebank.com(.br)?/cambio)')
        url_in_padrao = padrao_url.match(self.url)
        if not url_in_padrao:
            raise ValueError('A URL é inválida.')
        else:
            print('A URL é válida.')

    def get_url_base(self):
        url_base = self.url[:self.url.find('?')]
        return url_base

    def get_url_parametros(self):
        if self.url.find('?') == -1:
            return 'Não possui parâmetros.'
        url_parametros = self.url[self.url.find('?') + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        if self.url.find('?') == -1:
            return 'Ocorreu um erro! A URL não possui parâmetros!'
        else:
            indice_parametro = self.url.find(parametro_busca)
            indice_tam_parametro = indice_parametro + len(parametro_busca) + 1
            indice_e = self.url.find('&',indice_tam_parametro)
            if indice_e == - 1:
                valor = self.url[indice_tam_parametro:]
            else:
                valor = self.url[indice_tam_parametro:indice_e]
            return valor

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == 'real' and moeda_destino == 'dolar':
    conversao = int(quantidade) / valor_dolar
    print(f'O valor em reais é {quantidade} e o valor convertido em dolar fica {conversao}')

elif moeda_origem == 'dolar' and moeda_destino == 'real':
    conversao = int(quantidade) * valor_dolar
    print(f'O valor em dolar é {quantidade} e o valor convertido em real fica {conversao}')
else:
    print(f'O cambio de {moeda_origem} para {moeda_destino} não está disponivel.')