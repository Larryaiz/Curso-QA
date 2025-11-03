import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"],
    "Idade": [25, 30, 22, 28, 35, 27, 40],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(dados)

print("DataFrame completo:")
print(df)

recife_df = df[df["Cidade"] == "Recife"]

print("\nMoradores de Recife:")
print(recife_df)
