import pandas as pd

df = pd.read_csv('clientes.csv')

# Setando a largura do display para que as colunas sejam exibidas de forma completa
pd.set_option('display.width', None)
# Para exibir o início do DataFrame
print(df.head())

# Removendo dodos nulos
df.drop('pais', axis=1, inplace=True) # O índice 1 é referente a coluna
df.drop(2, axis=0, inplace=True) # O índice 0 é referente a linha

# Padronizar os textos do DataFrame
df['nome'] = df['nome'].str.title() # Transforma todas as iniciais em maiúsculas
df['endereco'] = df['endereco'].str.lower() # Transforma tudo em minúscula
df['estado'] = df['estado'].str.upper # Transforma todas as letras em maiúsculas


