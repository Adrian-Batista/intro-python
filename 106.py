#!/usr/bin/python3

import sys
import cvs


###
## Exercicios
###

capitais = []
with open('capitais-BR.csv', newline='') as csv_file:
    arquivo = csv.reader(csv_file, delimiter=';', quotechar='|')
    for cidade in arquivo:
        capitais.append(cidade)

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.

def define_default_city(state):
    for capital in capitals:
        if capital[0] == state:
            return True

    return False

city_exists = define_default_city('Roraima')

print("------------------------")
# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente. Ela deve executar sem erro mesmo que alguns dados estejam faltando.

def remover_estados_sudeste():
    estados_sudeste = ['São Paulo', 'Rio de Janeiro', 'Espírito Santo', 'Minas Gerais']

    lista_estados = [valor for valor in capitals if valor[0] not in estados_sudeste]
    
    with open('capitais-BR.csv', mode='w') as csv_file:
        state_writer = csv.writer(csv_file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for state in lista_estados:
            state_writer.writerow(state)
    
    print('Arquivo "capitais-BR.csv" atualizado.')

remover_estados_sudeste()

print("------------------------")
# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro. O algoritmo precisa ser eficiente, nesse caso especifico a melhor a melhor complexidade que pode ser acancada é linear. Algoritmos de complexidade quadratica, cubica, fatorial, etc. não sao considerados como eficientes pois a complexidade linear eh garantida. Como regra geral, se seu algoritmo demorar mais do que alguns segundos, ele, provavelmente, nao eh linear.

def verfica_cpf():
    dados_unicos = []
    with open('lista-cpf.txt', 'r') as txt_file:
        linhas = set(txt_file.readlines())
        dados_unicos = (tuple(linhas))
            
    with open('lista-cpf-unicos.txt', 'w') as txt_file:
        for cpf in dados_unicos:
            txt_file.write(cpf)
    
    print('Arquivo "lista-cpf-unicos.txt" criado.')

verfica_cpf()