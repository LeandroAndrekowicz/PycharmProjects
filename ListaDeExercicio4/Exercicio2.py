lista = []
maior = 0
menor = 9999999999

for i in range (5):
    lista.append(int(input("Digite um valor: ")))
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(maior+menor)
