#!/usr/bin/python3

# Importacao do modulo sys
import sys

###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
lista = ['a','b','c']

def funcao(valor):
    for x in valor:
        print(x.upper())


funcao(lista)

print("------------------------")
## Usando a lista: [0, 1, 7, 4, 5]
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.
lista = [0, 1, 7, 4, 5]

def funcao2(valor):
    total = 0
    for x in valor:
        total = total + x
    return total

print("A soma da lista: " + str(lista) + " é igual a : " + str(funcao2(lista)))

print("------------------------")
# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida
lista = [0, 1, 2, 3, 4, 5]

def list_impar(valor):
    impares = []
    for x in valor:
        if not x % 2 == 0:
            impares.append(x)
    return impares

print(list_impar(lista))

print("------------------------")
## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.
frase = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
frase = frase.replace(',', '')
frase = frase.replace('.', '')

lista = frase.split(' ')
contador = 0
for x in lista:
    if len(x) >= 5:
        contador +=1
        
print("REALIZADO EM FOR - Existem " + str(contador) + " palavras com 5 ou mais caracteres.")

vetor = [x for x in lista if len(x) >= 5]
print("REALIZADO EM COMPREHENSION - Existem " + str(len(vetor)) + " palavras com 5 ou mais caracteres.")

print("------------------------")
# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
multiplos = [i * 3 for i in range(0,100)]

print('Multiplos:')
for i in multiplos:
    print(i)

print("------------------------")
# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
'''def valores_primos(inicio, fim):
    i = 0
    primos = []
    while(i != fim):
        if (n % count == 0):
            impares.append(x)
    return impares

list_impar(lista)'''