numero = int(input("Digite o numero que quer converter:"))
if numero == 1:
    print("O numero %.f em romanos eh: I"% numero)
elif numero == 5:
    print("O numero %.f em romanos eh V"% numero)
elif numero == 10:
    print("O numero %.f em romanos eh X" % numero)
elif numero == 50:
    print("O numero %.f em romanos eh L" % numero)
elif numero == 100:
    print("O numero %.f em romanos eh C" % numero)
elif numero == 500:
    print("O numero %.f em romanos eh D" % numero)
elif numero == 1000:
    print("O numero %.f em romanos eh M" % numero)
else:
    print("Numero invalido!")