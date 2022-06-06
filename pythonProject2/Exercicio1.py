codigo = int(input("Digite o codigo do produto:"))
if codigo == 1:
    print("Seu produto eh do Sul.")
elif codigo == 2:
    print("Seu produto eh do Norte")
elif codigo == 3:
    print("Seu produto eh do Leste")
elif codigo == 4:
    print("Seu produto eh do Oeste")
elif codigo == 5 or codigo == 6:
    print("Seu produto eh do Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print("Seu produto eh do Sudeste")
elif codigo == 10:
    print("Seu produto eh do Centro-Oeste")
elif codigo == 11:
    print("Seu produto eh do Noroeste")
else:
    print("Seu produto eh importado")
