lista = []
cont = 0
for i in range(7):
    lista.append(int(input("Digite um valor: ")))
    if lista[i] % 2 == 0:
        cont +=1
print("A quantidade de numeros pares eh: ",cont)
