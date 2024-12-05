import pandas
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/')
print(response.text[:600])

soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000]) # a função prettify() exibe o código HTML de forma mais estruturada
# Para utilizar classe BeautifulSoup é necessário indicar o documento (no caso está dentro da
# variável requisicao), logo em seguida o atributo que queremos (texto), depois especificamos
# formato que queremos entregar ('html.parser')
# BeautifulSoup: classe do módulo bs4 utilizada para fazer análise de documentos HTML

print("Pandas")
url_pandas = pandas.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/')
print(url_pandas)