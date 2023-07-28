lista = [12, 10, 7, 5,]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print (lista_animal)

tupla = (1, 10, 12, 14,)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print (type(lista_numerica))
lista_numerica[0] = 100
print (lista_numerica)
#print(lista_animal[1])
#nova_lista = lista_animal * 2
#print(nova_lista)
#lista.sort()
#lista_animal.sort()
#print (lista)
#print (lista_animal)
#lista_animal.reverse()
#print(lista_animal)
#if 'lobo' in lista_animal:
   # print('existe na lista')
#else:
    #print('não existe um na lista. Será incluido')
    #lista_animal.append('lobo')
    #print(lista_animal)


#lista_animal.pop()
#print(lista_animal)
#print(max(lista_animal))
#print(min(lista))
#print(max(lista))

#soma = 0
#for x in lista:
    #print(x)
    #soma += x
#print(soma)
