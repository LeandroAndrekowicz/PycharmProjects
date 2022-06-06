matriz1 = []
matriz2 = []
matriz3 = []
valorT = 0
print("DIGITE OS VALORES DA PRIMEIRA MATRIZ!!")
for i in range(3):
    coluna1 = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        coluna1.append(valor)
    matriz1.append(coluna1)
print("DIGITE OS VALORES DA SEGUNDA MATRIZ!!")
for i in range(3):
    coluna2 = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        coluna2.append(valor)
    matriz2.append(coluna2)
for i in range(3):
    coluna3 = []
    for j in range(3):
        valorT = matriz1[i][j]*matriz2[i][j]
        coluna3.append(valorT)
    matriz3.append(coluna3)
print("A MULTIPLICAÇÃO DAS MATRIZES EH: ")
for i in range(3):
    print(matriz3[i])