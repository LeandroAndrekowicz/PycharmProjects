lado1 = float(input("Digite o primeiro lado do triangulo:"))
lado2 = float(input("Digite o segundo lado do triangulo:"))
lado3 = float(input("Digite o terceiro lado do triangulo:"))
if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Voce tem um triangulo Equílatero, ou seja, todos os lados iguais.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Voce tem um triangulo Isóceles, ou seja, dois lados iguais")
else:
    print("Voce tem um triangulo Escaleno, ou seja, nenhum dos lados eh igual")