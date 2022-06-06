i = 0
total = 0
while i < 10:
    numeros = float(input("Digite um numero:"))
    i = i + 1
    total = numeros + total
media = total/10
print("A media dos numeros eh: %.2f"% media)
