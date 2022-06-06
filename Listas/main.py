import lista
listaCodigo = []
listaProduto = []
op = 1
lista.menu()
while op != 0:
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        quantidade = int(input("Digite quantos produtos quer cadastrar: "))
        listaCodigo, listaProduto = lista.criarLista(quantidade)
    if op == 2:
        lista.mostrarLista(listaCodigo, listaProduto)
    if op == 3:
        codigo = int(input("Digite o codigo do produto que deseja excluir: "))
        lista.excluirElemento(codigo, listaCodigo, listaProduto)
    if op == 4:
        listaCodigo, listaProduto = lista.inserirNoFinalDaLista(listaCodigo, listaProduto)
    if op == 5:
        listaCodigo, listaProduto = lista.inserirNoPrimeiroIndice(listaCodigo, listaProduto)
    if op == 6:
        indice = int(input("Digite em qual posição deseja adicionar o item: "))
        listaCodigo, listaProduto = lista.inserirNoIndice(listaCodigo,listaProduto,indice)
    if op == 7:
        codigo = int(input("Digite o codigo do produto que deseja consultar: "))
        lista.busca(listaCodigo, codigo)
    else:
        print("OPÇÃO INVÁLIDA!!!")