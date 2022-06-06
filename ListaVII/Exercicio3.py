

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista3 = lista1+lista2
print(lista3)
for i in range(len(lista2)):
    inserindo = lista2[i]
    lista3.insert(i+1, inserindo)
print(lista3)



