lista = []
tupla = ()
maior = 0
posicao = 0
for i in range(10):
    lista.append(int(input("Digite um valor: ")))
    tupla = lista
    if lista[i] > maior:
        maior = lista[i]
        posicao = i
print(tupla)
print(posicao)