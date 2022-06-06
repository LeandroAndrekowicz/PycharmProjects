matriz = []
maior10 = 0
for i in range(4):
    coluna = []
    for j in range(4):
        valor = int(input("Digite um valor: "))
        coluna.append(valor)
        if valor > 10:
            maior10 +=1
    matriz.append(coluna)
for i in range(4):
    print(matriz[i])
print("A quantidade de valores maiores que 10 eh: ",maior10)