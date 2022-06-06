opcao = 0
quad = 0
while opcao != 2:
    opcao = int(input("Digite 2 para sair do programa:"))
    if opcao != 2:
        num = float(input("Digite um numero:"))
        quad = quad + (num*num)
    else:
        print("SAINDO DO PROGRAMA!!")
print("A soma dos quadrados foi: %.2f"% quad)
