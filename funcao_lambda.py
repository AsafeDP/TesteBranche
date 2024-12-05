import pandas as pd

# funcão elevar ao cubo simples
def elevar_cubo(x):
    return x ** 3

# função elevar ao cubo com lambda
elevar_cubo_lambda = lambda x: x ** 3

print(elevar_cubo(2))
print(elevar_cubo_lambda(2))

df = pd.DataFrame({'Numero': [1, 2, 3, 4, 5, 10]})

# A função lambda é utilizada principalmente quando temos operações simples e diretas
df['cubo_funcao'] = df['Numero'].apply(elevar_cubo) # A função apply serve para aplicar uma função
df['cubo_lambda'] = df['Numero'].apply(lambda x: x ** 3)

print(df)

