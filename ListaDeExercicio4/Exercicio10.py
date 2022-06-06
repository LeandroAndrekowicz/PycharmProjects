lista = []
for i in range(5):
    lista.append(int(input("Preencha o Vetor: ")))
x = int(input("Digite um valor: "))
for i in range(5):
    if x == lista[i]:
        print(x)
    else:
        print(-1)