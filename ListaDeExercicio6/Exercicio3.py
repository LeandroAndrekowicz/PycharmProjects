import calculosExercicio3
opcao = 0
calculosExercicio3.menu()
while opcao != 4:
    opcao = int(input("DIGITE A OPCAO DESEJADA: "))
    if opcao == 1:
        raio = float(input("Digite o raio da circunferencia: "))
        calculosExercicio3.circunferencia(raio)
    elif opcao == 2:
        base = float(input("Digite a base do triangulo: "))
        altura = float(input("Digite a altura do triangulo: "))
        calculosExercicio3.triangulo(base, altura)
    elif opcao == 3:
        base = float(input("Digite a base do retangulo: "))
        altura = float(input("Digite a altura do retangulo: "))
        calculosExercicio3.retangulo(base, altura)
    elif opcao == 4:
        calculosExercicio3.saindo()
    else:
        calculosExercicio3.invalida()