notas = []
media = 0
for i in range(6):
    notas.append(float(input("Digite a nota do aluno: ")))
    media = media + notas[i]
mediaF = media/6
print("A media dos alunos eh: %.2f"%mediaF)
