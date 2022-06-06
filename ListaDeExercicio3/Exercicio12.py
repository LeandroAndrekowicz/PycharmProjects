print("CALCULADORA")
print("Digite 1 para Somar \nDigite 2 para Subtrair \nDigite 3 para Dividir \nDigite 4 para Multiplicar \nDigite 5 para Sair da Calculadora")
opcao = 0
while opcao != 5:
    opcao = int(input("Digite a Opção desejada:"))
    if opcao == 1:
        print("VOCE ESCOLHEU SOMAR")
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        soma = num1+num2
        print("A soma dos numeros eh: %.2f"%soma)
    elif opcao == 2:
        print("VOCE ESCOLHEU SUBTRAIR")
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        sub = num1 - num2
        print("A subtração dos numeros eh: %.2f" %sub)
    elif opcao == 3:
        print("VOCE ESCOLHEU A DIVISÃO")
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        div = num1 / num2
        print("A divisão dos numeros eh: %.2f" % div)
    elif opcao == 4:
        print("VOCE ESCOLHEU A MULTIPLICAÇÃO")
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
        mult = num1 * num2
        print("A multiplicação dos numeros eh:%.2f" % mult)
    elif opcao == 5:
        print("SAINDO DO PROGRAMA")
    else:
        print("OPÇÃO INVALIDA")