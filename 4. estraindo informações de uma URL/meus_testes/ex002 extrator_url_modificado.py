class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
        if not self.url.startswith('http' or 'https'):
            raise ValueError("A URL deve estar completa!")
        if self.url.endswith('/cambio'):
            raise ValueError("A URL não possui parametros!")

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

extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)