def contar_vogais(palavra):
    vogais = "a","e","i","o","u"
    contador = 0

    for letra in palavra.lower():
        if letra in vogais:
            contador += 1

    return contador

palavra_usuario = input("Digite uma palavra: ")

total_vogais = contar_vogais(palavra_usuario)

print(f'A palavra "{palavra_usuario}" tem {total_vogais}')