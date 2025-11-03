import pandas as pd

df = pd.read_csv("dados_ficticios.csv")

print("DataFrame completo:")
print(df.head())

idade_maior_40 = df[df["idade"] > 40]
print("\nPessoas com idade maior que 40 anos:")
print(idade_maior_40)

renda_maior_5k = df[df["renda"] > 5000]
print("\nPessoas com renda maior que 5 mil:")
print(renda_maior_5k)

renda_maior_15k = df[df["renda"] > 15000]
print("\nPessoas com renda maior que 15 mil:")
print(renda_maior_15k)
