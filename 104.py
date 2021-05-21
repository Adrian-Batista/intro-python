#!/usr/bin/python3

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
lista1 = [1,2,3]
lista2 = [1,3,2]

def funcao(lista1, lista2):
    if lista1 == lista2:
        print('Listas iguais!')
        return True
    else:
        print('Listas diferentes!')
        return False

print(funcao(lista1,lista2))

print("------------------------")
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
valor = 'Luz azul'

def funcao2(valor):
    verifica = valor.replace(" ", "").lower()
    if verifica == verifica[::-1]:
        print('A palavra: ' + verifica + ' é uma palindrome!')
        return True
    else:
        print('A palavra: ' + verifica + ' NÂO é uma palindrome!')
        return False

print(funcao2(valor))
# OBS.: Utilize apenas o que foi estudado ate agora
