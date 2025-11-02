Frequencia = int(input("Insira a frequencia: "))
Diaria = input("passou hoje? (sim ou não): ")

if Diaria.lower() == "sim":
    Frequencia += 1
    
    if Frequencia <21:
        print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

    elif Frequencia >= 21:
        print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")

    elif Frequencia == 1:
        print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")

if Diaria.lower() in ["não", "nao"]:
    Frequencia = 0
    print("Sequência reiniciada")