#!/usr/bin/python3


#########
# Exercicios - Listas
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
weekdays[2]

# Como verificar o tipo de 'mon'?
type(weekdays[0])

# Como separar 'wed' até 'fri'?
weekdays[2:5]

# Quais as maneiras de selecionar 'fri' por indice?
weekdays[-1]
#ou
weekdays[4]

# Qual eh o tamanho dos dias e days_list?
len(weekdays)

# Como inverter a ordem dos dias?
weekdays.reverse()
#ou
weekdays[::-1]

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')

# Como limpar list?
list.clear()

# Como deletar list?
del(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list[-1]
list.pop()