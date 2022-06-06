lista = []
maior = 0
menor = 999999999999
posicao1 = 0
posicao2 = 0
for i in range(5):
    lista.append(int(input("Digite um numero: ")))
    if lista[i] > maior:
        maior = lista[i]
        posicao1 = i
    if lista[i] < menor:
        menor = lista[i]
        posicao2 = i
print("O maior numero eh: %.f e esta na posição %.f da lista\nO menor numero eh: %.f e esta na posição %.f da lista"% (maior, posicao1, menor, posicao2))