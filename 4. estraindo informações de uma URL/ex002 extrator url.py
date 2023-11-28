import re
class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return 'URL: ' + self.url + '\n' + 'URL Base: ' + self.get_url_base() + '\n' + 'Parâmetros: ' + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com.(br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida.')

    def get_url_base(self):
        base_url = self.url[:self.url.find('?')]
        return base_url

    def get_url_parametros(self):
        self.parametros_url = self.url[self.url.find('?') + 1:]
        return self.parametros_url

    def get_valor_parametro(self,nome_parametro):
        parametro_de_busca = nome_parametro
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e = self.get_url_parametros().find('&', indice_valor)
        if indice_e == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e]
        return valor

url = 'https://www.bytebank.com.br/cambio?quantidade=100&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print(1 is True)

#print(extrator_url == extrator_url_2)
