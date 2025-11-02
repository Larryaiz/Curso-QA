import os

os.mkdir("comidas")

receitas = ["Cinnamon roll", "Escondidinho de carne", "Bolo de cenoura", "Peixe caiçara"]

with open("comidas/receitas.txt", "w") as livro:
    for item in receitas:
     livro.write(item + "\n")
