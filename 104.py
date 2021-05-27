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
string1 = 'Luz azul'
string2 = 'Luzazul'

def funcao2(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    if string1 == string2[::-1]:
        print('A palavra: ' + str(string2) + ' é uma palindrome perfeita de: ' + str(string1))
        return True
    else:
        print('A palavra: ' + str(string2) + ' NÂO é uma palindrome de: ' + str(string1))
        return False

print(funcao2(string1, string2))
# OBS.: Utilize apenas o que foi estudado ate agora
