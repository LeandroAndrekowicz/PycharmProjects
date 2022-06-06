v1 = int(input("Digite o primeiro valor:"))
v2 = int(input("Digite o segundo valor:"))
t = 0
for i in range(v1, v2 , 1):
    v1 = v1+1
    t = t + v1
    print(i)
print("Soma = ",t)