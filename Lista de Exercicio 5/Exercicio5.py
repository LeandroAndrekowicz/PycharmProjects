matriz1 = []
matriz2 = []
print("DIGITE OS VALORES DA MATRIZ!!")
for i in range(3):
    coluna1 = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        coluna1.append(valor*valor)
    matriz1.append(coluna1)
matriz2 = matriz1
for i in range(3):
    print(matriz2[i])