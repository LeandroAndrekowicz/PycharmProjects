dia = int(input("Digite o dia do seu nascimento:"))
mes = int(input("Digite o mes do seu nascimento:"))
if dia <= 31 or mes <= 12:
    if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
        print("Seu signo eh Áries")
    elif dia >= 21 and mes == 4 or dia <=20 and mes == 5:
        print("Seu signo eh Touro")
    elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
        print("Seu signo eh Gêmeos")
    elif dia >= 21 and mes == 6 or dia <= 22 and mes == 7:
        print("Seu signo eh Câncer")
    elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
        print("Seu signo eh Leão")
    elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
        print("Seu signo eh Virgem")
    elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
        print("Seu signo eh Libra")
    elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
        print("Seu signo eh Escorpião")
    elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
        print("Seu signo eh Sagitário")
    elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
        print("Seu signo eh Capricórnio")
    elif dia >= 21 and mes == 1 or dia <= 18 and mes == 2:
        print("Seu signo eh Aquário")
    elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
        print("Seu signo eh Peixes")
else:
    print("Mes ou dia invalido!")