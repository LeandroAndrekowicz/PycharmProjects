import Pilha

cheio = 20
op = 1
Pilha.menu()
while op != 0:
    op = int(input("Digite a opcao desejada: "))
    if op == 1:
        clientes = int(input("Digite quantos Clientes tem no no banco: "))
        pilha, pilhaPref = Pilha.criarPilha(clientes)
        print(pilha, pilhaPref)
