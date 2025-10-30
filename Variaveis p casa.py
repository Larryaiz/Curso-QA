nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em centimetros: "))
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

total_notas = nota1 + nota2

print(f"Olá {nome}, sua idade é {idade}, sua altura é {altura:.1f}cm e a soma das suas notas é igual a {total_notas}")