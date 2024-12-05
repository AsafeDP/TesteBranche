import pandas as pd

df = pd.read_csv('C:/users/Asafe/Downloads/clientes.csv')

print(df.head().to_string()) # A função to_string() é utilizada para exibir os dados em uma linha única

print(df.tail().to_string())

# Exibe a quantidade de linhas e colunas
print('\nQuantidade', df.shape)

# Verifica valores nulos
print('\nValores nulos:\n',df.isnull().sum()) # A função .isnull() é utilizada para verificar valores nulos
                                              # A função .sum() é utilizada para somar uma série de valores