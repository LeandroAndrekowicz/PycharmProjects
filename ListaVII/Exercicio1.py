lista = [['Brasil', 'Italia',10, 9], ['Brasil', 'Espanha', 5, 7], ['Italia', 'Espanha', 7,8]]
totalFaltas = 0
maisFaltas = 0
menosFaltas = 9999999



for l in range(2,4,1):
    for c in range(3):
        if maisFaltas<lista[c][l]:
            maisFaltas = lista[c][l]
            pos1 = l-1
            pos2 = c

        if menosFaltas>lista[c][l]:
            menosFaltas = lista[c][l]
            pos3 = l-1
            pos4 = c-1

        totalFaltas += lista[c][l]


maior = lista[pos1][pos2]
menor = lista[pos3][pos4]

for i in range(3):
    print(lista[i])
print("\n")
print("O time com mais Faltas por jogo foi: ",maior)
print("O time com menos Faltas por jogo foi: ",menor)
print("O total de faltas foi: ", totalFaltas)
