import random
dados = []
repetidos = []
for i in range(10):
    valor = random.randint(1,6)
    dados.append(valor)
dados.sort()

for i in range(1,7,1):
    repet = dados.count(i)
    repetidos.append(repet)

print(dados)
print(repetidos)
