#!/usr/bin/python3

import sys
import timeit

###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla

print(f'Métodos das LISTAS: \n{dir(list)}\n')
print(f'Métodos das TUPLAS: \n{dir(tuple)}\n')

print("------------------------")
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos

def dif_classes():
    lista = dir(list)
    tupla = dir(tuple)

    metodos_dif = [metodo for metodo in lista if metodo not in tupla]
    print(f'Métodos que apenas a lista possui: \n{metodos_dif}\n')    

dif_classes()

print("------------------------")
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.

professor1 = {
    'id': 42, 
    'name': 'Alexandre Abreu', 
    'age': 30, 
    'state_origin': 'Minas Gerais', 
    'courses': [
        'Inteligência Artificial', 
        'Mineração de Dados', 
        'Programação para Internet I', 
        'Programação para Internet II'
    ]
}
professor2 = {
    'id': 37,
    'name': 'Denilson Barbosa',
    'age': 40,
    'state_origin': 'Paraná',
    'courses': [
        'Inteligência Artificial',
        'Banco de Dados I',
        'Banco de Dados II',
        'Programação para Internet I'
    ]
}
professor3 = dict(id=28, name='Jorge Armino', idade=37)

professor1['coordenadas'] = ('59625489', '75365489')
professor2['coordenadas'] = ('15487532', '26054862')
professor3['coordenadas'] = ('84628562', '58743215')

print('Coordenadas do professor 1: {}' .format(professor1['coordenadas']))
print('Coordenadas do professor 2: {}' .format(professor2['coordenadas']))
print('Coordenadas do professor 3: {}' .format(professor3['coordenadas']))