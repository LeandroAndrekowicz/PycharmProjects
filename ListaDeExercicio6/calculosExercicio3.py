def menu():
    print("*******************************************")
    print("** Digite 1 para escolher circunferência **")
    print("** Digite 2 para escolher triângulo      **")
    print("** Digite 3 para escolher retângulo      **")
    print("** Digite 4 para sair do programa        **")
    print("*******************************************")

def circunferencia(raio):
    area = 2 * 3.14 * raio
    print("A area da circunferencia eh: %.2f" % area)
    return area
def triangulo(base, altura):
    area = (base*altura)/2
    print("A area do triangulo eh: %.2f" % area)
    return area
def retangulo(base, altura):
    area = base * altura
    print("A area do retangulo eh: %.2f" % area)
    return area
def saindo():
    print("*******************************************")
    print("**         SAINDO DO PROGRAMA!!          **")
    print("*******************************************")
def invalida():
    print("*******************************************")
    print("**           OPCAO INVALIDA!!            **")
    print("*******************************************")