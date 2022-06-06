import random


def criarPilha(tamanho):
    pilha = [''] * tamanho
    global quantidade
    for i in range(len(pilha)-5):
        pilha[i]= random.randint(1,10)
        quantidade+=1
    return pilha

def pilhaCheia(pilha):
    if not pilha:
        return print('É necessario criar a pilha')
    if quantidade==max:
        return True

def tamanhoPilha(pilha):
    if not pilha:
        return print('É necessario criar a pilha')
    return print(quantidade)

def liberaPilha(pilha):
    global quantidade
    quantidade=0

def insereNaPilha(pilha,valor):
    global quantidade
    if not pilha:
        return print('É necessario criar a pilha')
    if pilhaCheia(pilha):
        return print('Pilha cheia')
    pilha[quantidade]=valor
    quantidade+=1
    return print('valor inserido no topo da pilha')

def consultaTopoPilha(pilha):
    if not pilha or quantidade==0:
        return print('É necessario criar a pilha')
    return print(pilha[quantidade-1])

def removePilha(pilha):
    global quantidade
    if not pilha or quantidade==0:
        return print('É necessario criar a pilha/ Pilha vazia')
    quantidade-=1

def mostrarPilha(pilha):
    if quantidade == 0:
        print('Pilha vazia')
    else:
        print('\n'*5)
        for i in range(quantidade-1,-1,-1):
            print(' ____ ')
            print('|',pilha[i],'|')



max = 10
quantidade = 0
pilha = []
































