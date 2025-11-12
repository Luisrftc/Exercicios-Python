senha = 0
cont = 0

for i in range (1,4):
    print("Usuário",i)
    senha = int(input("Informe a senha:"))
    if cont > 0:
        cont = 0

    while senha != 1234 and cont < 2:
        if senha != 1234 and cont < 1:
            print("Senha inválida!")
            senha = int(input("Informe a senha:"))
        elif senha == 1234 and cont < 2:
            print("Acesso permitido!")
        else:
             print("Acesso bloqueado!")
        cont += 1

print("Fim")
