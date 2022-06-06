#Código da lista

def criarLista(quantidade):
    listaCodigo = [''] * quantidade
    listaProduto = [''] * quantidade
    for i in range(quantidade):
        listaCodigo[i] = int(input("Digite o codigo do produto: "))
        listaProduto[i] = input("Digite o nome do produto: ")
    return listaCodigo, listaProduto


def mostrarLista(listaCodigo, listaProduto):
    if len(listaCodigo) == 0:
        print("Sem produtos Cadastrados!!")
    for i in range(len(listaCodigo)):
        print(listaCodigo[i], "|", listaProduto[i])


def excluirElemento(codigo, listaCodigo ,listaProduto):
    chave = ""
    for i in range(len(listaCodigo)):
        if listaCodigo[i] == codigo:
            chave = i
            break
    if chave!= "":
        for i in range(chave,len(listaCodigo)-1):
            listaCodigo[i]= listaCodigo[i+1]
        listaCodigo[len(listaCodigo)-1]= ''

        for i in range(chave,len(listaProduto)-1):
            listaProduto[i]= listaProduto[i+1]
        listaProduto[len(listaProduto)-1]= ''
        return listaCodigo, listaProduto

    print('O  elemento {} não se encontra na lista'.format(codigo))


def inserirNoFinalDaLista(listaCodigo, listaProduto):
    codigo = int(input("Digite o codigo do produto a adicionar: "))
    produto = input("Digite o nome do produto a adicionar: ")
    listaCodigo.append(codigo)
    listaProduto.append(produto)
    return listaCodigo,listaProduto


def inserirNoPrimeiroIndice(listaCodigo, listaProduto):
    tamanhoLista = len(listaCodigo) + 1
    temp= [0]*tamanhoLista
    temp2= [0]*tamanhoLista
    codigo = int(input("Digite o codigo do produto que deseja cadastrar: "))
    produto = input("Digite o nome do produto que deseja cadastrar: ")
    for i in range(len(listaProduto)):
        temp[i+1] = listaProduto[i]
    temp[0]= produto
    listaProduto = temp

    for i in range(len(listaCodigo)):
        temp2[i + 1] = listaCodigo[i]
    temp2[0] = codigo
    listaCodigo = temp2

    return listaCodigo, listaProduto


def inserirNoIndice(listaCodigo, listaProduto,indice):
    temp = listaCodigo.copy()
    temp.append(0)
    temp2 = listaProduto.copy()
    temp2.append(0)

    codigo = int(input("Digite o codigo do produto que deseja cadastrar: "))
    produto = input("Digite o nome do produto que deseja cadastrar: ")
    for i in range(indice,len(listaCodigo)):
        temp[i+1] = listaCodigo[i]
    listaCodigo=temp
    listaCodigo[indice]=codigo

    for i in range(indice,len(listaProduto)):
        temp2[i+1] = listaProduto[i]
    listaProduto=temp2
    listaProduto[indice]=produto

    return listaCodigo, listaProduto


def busca(listaCodigo, codigo):
    estado = False
    for i in range(len(listaCodigo)):
        if listaCodigo[i] == codigo:
            estado = True
            break
    if estado==True:
        return print('O índice do elemento {} é {}'.format(codigo,i))
    else:
        return print('O  elemento {} não se encontra na lista'.format(codigo))















def menu():
    print("********************************************************")
    print("** Digite 1 para criar a lista                        **")
    print("** Digite 2 para mostrar a lista                      **")
    print("** Digite 3 para excluir algum item da lista          **")
    print("** Digite 4 para inserir no final da lista            **")
    print("** Digite 5 para inserir do começo da lista           **")
    print("** Digite 6 para inserir em qualquer posição da lista **")
    print("** Digite 7 para ver se o item esta cadastrado        **")
    print("** Digite 0 para sair do programa                     **")
    print("********************************************************")
