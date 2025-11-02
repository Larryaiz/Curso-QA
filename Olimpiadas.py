def divisao_times(matricula):
    if matricula % 2 == 0:
        return "AZUL"
    else:
        return "AMARELO"

registro = [] 

for i in range(5):
    matricula = int(input(f"Digite o número da matrícula: "))
    registro.append(matricula)

for matricula in registro:
    time = divisao_times(matricula)
    print(f"Matrícula {matricula} está no TIME {time}")
