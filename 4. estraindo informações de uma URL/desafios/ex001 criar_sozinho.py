class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''


    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia!')
        if not self.url.startswith('http' or 'https'):
            raise ValueError('A URL está incompleta!')


    def get_url_base(self):
        url_base = self.url[:self.url.find('?')]
        return url_base

    def get_url_parametros(self):
        url_parametros = self.url[self.url.find('?') + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.url.find(parametro_busca)
        indice_tam_parametro = indice_parametro + len(parametro_busca) + 1
        indice_e = self.url.find('&',indice_tam_parametro)
        if indice_e == - 1:
            valor = self.url[indice_tam_parametro:]
        else:
            valor = self.url[indice_tam_parametro:indice_e]
        return valor


extrator_url = ExtratorURL('http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_quantidade)