i = 0
cont = 0
salarioTFla = 0
salarioTVas = 0
salarioTFlu = 0
salarioTBot = 0
salarioTotal = 0
fla = 0
vas = 0
flu = 0
bot = 0
out = 0
nitO = 0
outraCidade = 0
while i != 2:
    cont =+ cont
    print("DIGITE \n1 PARA ESCOLHER FLAMENGO \n2 PARA ESCOLHER VASCO \n3 PARA ESCOLHER FLUMINENSE \n4 PARA ESCOLHER BOTAFOGO \n5 PARA OUTROS TIMES")
    clube = int(input("Digite seu clube preferido: "))
    print("1 PARA ESCOLHER NITEROI \n2 PARA OUTRAS CIDADES")
    cidade = int(input("Digite sua cidade natal: "))
    if clube == 1:
        fla =+ 1
        salarioFla = float(input("Digite seu salario: "))
        salarioTFla = salarioTFla + salarioFla
        if cidade == 1:
            nitF =+ 1
        elif cidade == 2:
            outraCidadeFla =+ 1
        else:
            print("CIDADE INVALIDA")
    elif clube == 2:
        vas =+ 1
        salarioVas = float(input("Digite seu salario: "))
        salarioTVas = salarioTVas + salarioVas
        if cidade == 1:
            nitV =+ 1
        elif cidade == 2:
            outraCidadeVas =+ 1
        else:
            print("CIDADE INVALIDA")
    elif clube == 3:
        flu =+ 1
        salarioFlu = float(input("Digite seu salario: "))
        salarioTFlu = salarioTFlu + salarioFlu
        if cidade == 1:
            nitFlu =+ 1
        elif cidade == 2:
            outraCidadeFlu =+ 1
        else:
            print("CIDADE INVALIDA")
    elif clube == 4:
        bot =+ 1
        salarioBot = float(input("Digite seu salario: "))
        salarioTBot = salarioTBot + salarioBot
        if cidade == 1:
            nitB =+ 1
        elif cidade == 2:
            outraCidadeBot =+ 1
        else:
            print("CIDADE INVALIDA")
    elif clube == 5:
        out =+ 1
        salarioOut = float(input("Digite seu salario: "))
        salarioTotal = salarioTotal + salarioOut
        if cidade == 1:
            nitO =+ 1
        elif cidade == 2:
            outraCidade =+ 1
        else:
            print("CIDADE INVALIDA")
    else:
        print("TIME INVALIDO!!")
    print("DIGITE \n1 PARA CONTINUAR NO PROGRAMA \n2 PARA SAIR DO PROGRAMA")
    i = int(input("DIGITE:"))
if fla == 0:
    salarioTFla = 0
else:
    salarioTFla = (salarioTFla / fla)
if vas == 0:
    salarioTVas = 0
else:
    salarioTVas = (salarioTVas / vas)
if flu == 0:
    salarioTFlu = 0
else:
    salarioTFlu = (salarioTFlu / flu)
if bot == 0:
    salarioTBot = 0
else:
    salarioTBot = (salarioTBot / bot)
if out == 0:
    salarioTotal = 0
else:
    salarioTBot = (salarioTBot / bot)
    salarioTotal = salarioTotal / (out + outraCidade)
print("A quantidade de torcedores são: \nFLAMENGO: %.f \nVASCO: %.f \nFLUMINENSE: %.f \nBOTAFOGO: %.f \nOUTROS TIMES: %.f"%( fla, vas, flu, bot, out))
print("A media salarial dos torcedores são \nFLAMENGO: %.2f \nVASCO: %.2f \nFLUMINENSE: %.2f \nBOTAFOGO: %.2f \nOUTROS TIMES: %.2f"%( salarioTFla, salarioTVas, salarioTFlu, salarioTBot, salarioTotal))
print("A quantidade de pessoas nascidas em Niteroi que nao torce para nenhum time do Rio eh:", outraCidade)
print("O numero de pessoas entrevistadas foi: ", cont)