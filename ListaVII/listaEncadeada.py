from no import No

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho=0

    def inserirFimDaLista(self,valor):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(valor)
        else:
            self.cabeca = No(valor)

        self.tamanho = self.tamanho + 1

    def buscarValorIndice(self,indice):
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("erro no indice")
        if ponteiro:
            return ponteiro.dado
        raise IndexError("erro no indice")


    def alterarValorIndice(self,indice,valor):
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("erro no indice")
        if ponteiro:
            ponteiro.dado = valor
        else:
            raise IndexError("erro no indice")

    def buscarIndiceDoValor(self,valor):
        ponteiro = self.cabeca
        i=0
        while(ponteiro):
            if ponteiro.dado == valor:
                return i
            ponteiro = ponteiro.proximo
            i+=1
        raise ValueError('{} não se encontra na lista'.format(valor))

    def inserirNoIndice(self,indice,valor):
        novoNo = No(valor)
        if indice==0:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
        else:
            ponteiro = self.cabeca
            for i in range(indice-1):
                if ponteiro:
                    ponteiro = ponteiro.proximo
            novoNo.proximo = ponteiro.proximo
            ponteiro.proximo = novoNo
        self.tamanho = self.tamanho + 1

    def removerValor(self,valor):
        if self.cabeca == None:
            raise ValueError('{} não se encontra na lista'.format(valor))
        elif self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
            self.tamanho = self.tamanho - 1
            return True
        else:
            antecessor = self.cabeca
            ponteiro = self.cabeca.proximo
            while(ponteiro):
                if ponteiro.dado == valor:
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo=None
                    self.tamanho = self.tamanho - 1
                    return True
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
        raise ValueError('{} não se encontra na lista'.format(valor))

    def mostrarLista(self):
        lista = ""
        ponteiro = self.cabeca
        while (ponteiro):
            lista = lista + str(ponteiro.dado) + "->"
            ponteiro = ponteiro.proximo
        print(lista)
