cont = 0
contI = 0
contP = 0
while cont < 10:
    cont = cont + 1
    num = int(input("Digite um numero:"))
    if num % 2 == 0:
        contP = contP + 1
    else:
        contI = contI + 1
print ("A quantidade de numeros pares eh:", contP, "\nA quantidade de numeros impares eh:", contI)
