matriz1 = []
matriz2 = []
matriz3 = []
maior = 0
cont = 0
print("DIGITE OS VALORES DA PRIMEIRA MATRIZ")
for i in range(4):
    coluna1 = []
    for j in range(4):
        valor = int(input("Digite um valor: "))
        coluna1.append(valor)
        if valor > maior:
            matriz3.append(valor)
            cont += 1
    matriz1.append(coluna1)
print("DIGITE OS VALORES DA SEGUNDA MATRIZ")
for i in range(4):
    coluna2 = []
    for j in range(4):
        valor = int(input("Digite um valor: "))
        coluna2.append(valor)
        if valor > maior:
            matriz3.append(valor)
            cont += 1
    matriz2.append(coluna2)
for i in range (4):
    print(matriz3[i])