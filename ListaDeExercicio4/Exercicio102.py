import random
cont = 0
lista = [random.randint(1, 10000) for i in range(5)]
x = int(input("Digite um valor: "))
print(lista)
for i in range(5):
    if x == lista[i]:
        print(x)
    else:
        print(-1)