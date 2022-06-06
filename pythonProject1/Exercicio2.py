watts = float(input("Digite a quantidade de watts da sua lampada:"))
largura = float(input("Digite a largura do comodo:"))
comprimento = float (input("Digite o comprimento do comodo:"))
area = largura*comprimento
metro = watts/18
qntLampadas = area/metro
print("A area do seu comodo eh: %.2f \nPara iluminar todo seu comodo serão necessarias: %.2f lampadas" % (area, qntLampadas))