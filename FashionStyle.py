valor_compra = float(input("Insira valor da compra: R$"))

if valor_compra > 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
elif valor_compra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
