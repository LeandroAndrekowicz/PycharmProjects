import menus
menus.menu()
opcao = 0
while opcao != 5:
    opcao = int(input("Digite a Opção desejada:"))
    print("\n" * 6)
    if opcao == 1:
        menus.soma()
        print("\n" * 4)
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        print("\n" * 4)
        menus.resSoma(num1, num2)
    elif opcao == 2:
        menus.subtrair()
        print("\n" * 4)
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        menus.resSubtrair(num1, num2)
    elif opcao == 3:
        menus.divisao()
        print("\n" * 4)
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        menus.resDividir(num1, num2)
    elif opcao == 4:
        menus.multiplicacao()
        print("\n" * 4)
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        menus.resMultiplicar(num1, num2)
    elif opcao == 5:
        menus.saindo()
        print("\n" * 2)
    else:
        menus.opcaoInvalida()
        print("\n" * 4)