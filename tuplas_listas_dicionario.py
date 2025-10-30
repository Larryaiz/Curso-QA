
tupla_dados = (10, 20, 30, 40, 50)
print("Tupla:", tupla_dados)

lista_dados = list(tupla_dados)
print("Lista:", lista_dados)

lista_dados.append(60)
lista_dados.append(70)
print("Lista com dados extras:", lista_dados)

lista_dados.pop(0)
print("Lista após remover o primeiro dado:", lista_dados)

lista_dados.pop()
print("Lista após remover o último dado:", lista_dados)

print("Primeiro dado da lista:", lista_dados[0])

print("Quantidade de dados na lista:", len(lista_dados))

# Dicionário

dados = {
    "Nome": "Grazi",
    "Idade": 24,
    "Profissão": "Ilustrador"
}


print("Nome do usuário:", dados["Nome"])
