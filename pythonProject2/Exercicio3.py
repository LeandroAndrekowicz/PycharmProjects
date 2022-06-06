valor = float(input("Digite um valor:"))
if valor > 0:
    print("O valor %.2f eh positivo"% valor)
elif valor == 0:
    print("O valor %.2f eh neutro"% valor)
else:
    print("O valor %.2f eh negativo"% valor)