#!/usr/bin/python3

'''
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## Funcoes

# Define a funcao
def sum(x=3, y=5):
    print("x: " + str(x))
    print("y: " + str(y))
    return x + y

# Chamada simples de funcao
x = 1
y = 2
z = sum(x, y)
print(z)

# Chamada de funcao com parametro sem ordem
z = sum(y=10, x=13)
print(z)

# Utiliza valor padrao dos parametros
z = sum()
print(z)

# PACKING E UNPACKING
# Atribuicao para mais de uma variável
a, b = x, y
print(f'a: {a}, b:{b}')

list = [1, 2, 3]
a, b, c = list
print(f'a: {a}, b:{b}, c:{c}')

# Ignorando um valor
a, b, _ = list
print(f'a: {a}, b:{b},')

# Multiplos valores (*)
a, *resto = list
print(f'a: {a}, resto: {resto}')

# troca de valores
a, b = b, a
print(f'a: {a}, b:{b}')


## CONDICIONAIS

temperature = 4
if temperature <= 0:
    print('Solido')
elif temperature > 0 and temperature < 100:
    print('Liquido')
else:
    print('Gasoso')

# Notacao matematica
if 0 < temperature < 100:
    print('Liquido')


## Operador ternario
# var = resultado_condicao_verdadeitra if condicao else resultado_condicao_false
valor = 4
positivo = True if valor > 0 else False
print(positivo)


###
# Exercicios
###
print ('-------------------------------------------------')
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
