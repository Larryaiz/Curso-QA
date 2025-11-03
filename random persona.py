from faker import Faker
import random
import pandas as pd

fake = Faker("pt_BR")

def criar_persona():
    return {
        "Nome": fake.name(),
        "Idade": random.randint(18, 60),
        "Cidade": fake.city()
    }

def gerar_personas(n=10):
    lista_personas = [criar_persona() for _ in range(n)]
    return pd.DataFrame(lista_personas)

num_personas = 10
df_personas = gerar_personas(num_personas)

df_personas.to_csv("personas_ficticias.csv", index=False)

print(f"{num_personas} personas geradas e salvas em 'personas_ficticias.csv'.")
print(df_personas)
