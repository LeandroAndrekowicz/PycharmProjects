kmInicial = float(input("Digite a quantidade de Kilometros inicial:"))
kmFinal = float(input("Digite a quantidade de Kilometros final:"))
gasolina = float(input("Digite quantos Kilometros seu carro faz por litro?:"))
cobrar = float(input("Digite qual o valor por Kilometro cobrado:"))
kmTotal = kmFinal-kmInicial
gastoGasolina = kmTotal/gasolina
gastoTotal = gasolina*1.9
lucro = (cobrar*gasolina)-gastoTotal
print("Para percorrer %.2f Km voce utilizou %.2f litros de gasolina. \nSeu lucro foi de %.2f reais"% (kmTotal, gastoGasolina, lucro))

