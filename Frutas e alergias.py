Frutas = ['Abacate', 'Banana', 'Morango']
Alergias = ['Uva', 'Abacaxi', 'Pera', 'Morango']

Frutas.append("Laranja")

for fruta in Frutas:
    if fruta in Alergias:
        print(f"{fruta} está na lista de alergias!")

