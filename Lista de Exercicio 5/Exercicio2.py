matriz = []
maior = 0
pos1 = 0
pos2 = 0
for i in range(4):
    coluna = []
    for j in range(4):
        valor = int(input("Digite um valor: "))
        coluna.append(valor)
        if valor > maior:
            maior = valor
            pos1 = i
            pos2 = j
    matriz.append(coluna)
for i in range(0,3,1):
    print(matriz[i])
print("O maior valor eh: %.f e esta na posicao: [%.f %.f] do vetor"%(maior, pos1, pos2))
