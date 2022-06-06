def menu():
    print("*****************************************")
    print("**             CALCULADORA             **")
    print("** Digite 1 para Somar                 **\n** Digite 2 para Subtrair              **\n** Digite 3 para Dividir               **\n** Digite 4 para Multiplicar           **\n** Digite 5 para Sair da Calculadora   **")
    print("*****************************************")
def soma():
    print("*****************************************")
    print("**         VOCE ESCOLHEU SOMAR         **")
    print("*****************************************")
def subtrair():
    print("*****************************************")
    print("**       VOCE ESCOLHEU SUBTRAIR        **")
    print("*****************************************")
def divisao():
    print("*****************************************")
    print("**       VOCE ESCOLHEU DIVIDIR         **")
    print("*****************************************")
def multiplicacao():
    print("*****************************************")
    print("**      VOCE ESCOLHEU MULTIPLICAR      **")
    print("*****************************************")
def saindo():
    print("*****************************************")
    print("**        SAINDO DO PROGRAMA!!         **")
    print("*****************************************")
def opcaoInvalida():
    print("*****************************************")
    print("**          OPÇÃO INVÁLIDA!!           **")
    print("*****************************************")
def resSoma(num1,num2):
    soma = num1 + num2
    print("\n" * 4)
    print("*****************************************")
    print("**          %.f + %.f = %.f            **"%(num1,num2,soma))
    print("*****************************************")
    print("\n" * 4)
    return soma
def resSubtrair(num1,num2):
    sub = num1 - num2
    print("\n" * 4)
    print("*****************************************")
    print("**          %.f - %.f = %.f            **" % (num1, num2, sub))
    print("*****************************************")
    print("\n" * 4)
    return sub
def resDividir(num1,num2):
    div = num1 / num2
    print("\n" * 4)
    print("*****************************************")
    print("**          %.f / %.f = %.f            **" % (num1, num2, div))
    print("*****************************************")
    print("\n" * 4)
    return div
def resMultiplicar(num1,num2):
    mult = num1 * num2
    print("\n" * 4)
    print("*****************************************")
    print("**          %.f x %.f = %.f            **" % (num1, num2, mult))
    print("*****************************************")
    print("\n" * 4)
    return mult