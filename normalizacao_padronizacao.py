import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

df = pd.read_csv('clientes-v2-tratados.csv')
pd.set_option('display.width', None)

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler: mudança de padrões nos dados;
# No modo padrão, na Escala-Padrão dos dados a média tende a ser 0
# enquanto o desvio tende a ser 1
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
# Bem parecido com último, porém nesse é utilizado a mediana e o IQR (intervalo interquartil)
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print("MinMaxScaler (0 à 1): ")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))

print("MinMaxScaler_mm (-1 à 1): ")
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Std: {:.4f}".format(df['idadeMinMaxScaler_mm'].min(), df['idadeMinMaxScaler_mm'].max(), df['idadeMinMaxScaler_mm'].mean(), df['idadeMinMaxScaler_mm'].std()))

print("StandardScaler (A tendência da média é ser 0 e o desvio padrão 1): ")
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Std: {:.4f}".format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].mean(), df['idadeStandardScaler'].std()))

print("RobusterScaler (0 à 1): ")
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Std: {:.4f}".format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))

