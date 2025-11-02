email_1 = input("Digite seu email: ")
email_2 = input("Digite outro email: ")

emails = [email_1,email_2]
check = "@jogajuntoinstituto.org"

for i in emails:
    if check in i:
        print(f"Este email {i} faz parte do instituto")
    else:
        print(f"Este email {i} não faz parte do instituto")


#Dado que o usuário está inserindo o email
#Quando o email possui '@jogajuntoinstituto.org' no texto
#Então o sistema informa que este faz parte do instituto


#Dado que o usuário está inserindo o email
#Quando o email NÃO possui '@jogajuntoinstituto.org' no texto
#Então o sistema informa que este NÃO faz parte do instituto