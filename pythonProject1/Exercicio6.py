comprimento = float(input("Digite o comprimento da sua cozinha:"))
largura = float(input("Digite a largura da sua cozinha:"))
altura = float(input("Digite a altura da sua cozinha:"))
area = comprimento*largura*altura
azulejo = 1.5
qntAzulejo = area/azulejo
print("A quantidade de azuleijos necessarias para cobrir %.2f metros sera:%.2f"%(area, qntAzulejo))