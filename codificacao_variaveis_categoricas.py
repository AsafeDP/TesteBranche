import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('clientes-v2-tratados.csv')
pd.set_option('display.width', None)

print(df.head())