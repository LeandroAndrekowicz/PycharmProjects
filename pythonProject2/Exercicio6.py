qntMacas = int(input("Digite a quantidade de maças que ira comprar:"))
if qntMacas < 6:
    valor = qntMacas*0.5
    print("Voce ira pagar %.f por %.f maças "%(valor, qntMacas))
else:
    valor = qntMacas*0.4
    print("Voce ira pagar %.f por %.f maças " % (valor, qntMacas))