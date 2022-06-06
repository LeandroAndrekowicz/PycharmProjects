lista = []
for i in range(10):
    numero = int(input('Insira um numero: '))
    lista.append(numero)
contador = 1
for c in range(len(lista) - 1):
    if lista[c] != lista[c+1]:
        contador += 1
if contador == 1:
    print(f'Existem {0} numeros diferentes!')
else:
    print(f'existem {contador} numeros diferentes!')