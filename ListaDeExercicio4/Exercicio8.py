import random
cont = 0
lista = [random.randint(1, 6) for i in range(50)]
for i in range(50):
    if lista[i] == 6:
        cont +=1
porcentagem = (cont*100)/50
print(lista)
print('O percentual de ocorrencias do numero 6 eh: ',porcentagem,'%')