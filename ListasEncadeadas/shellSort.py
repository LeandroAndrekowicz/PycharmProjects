def shell_sort(lista, n):
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = lista[i]
            j = i
            while j >= h and lista[j - h] > t:
                lista[j] = lista[j - h]
                j -= h

            lista[j] = t
        h = h // 2


lista = [34, 12, 20, 7, 13, 15, 2, 23]
n = len(lista)
print('Lista antes de ordenar:')
print(lista)
shell_sort(lista, n)
print('Lista depois de ordenar:')
print(lista)