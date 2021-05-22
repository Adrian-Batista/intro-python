#!/usr/bin/python3


###
# Exercicios
###

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

lista = book1.split('by')
resposta1 = "".join(lista[0:-1:])
resposta1 = resposta1.strip()
len(resposta1)

lista = book2.split('by')
resposta2 = "".join(lista[0:-1:])
resposta2 = resposta2.strip()
len(resposta2)

lista = book3.split('by')
resposta3 = "".join(lista[0:-1:])
resposta3 = resposta3.strip()
len(resposta3)


print("------------------------")
# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'


verifica = palindrome_one.replace(" ", "").lower()
verifica == verifica[::-1]

verifica = palindrome_two.replace(" ", "").lower()
verifica == verifica[::-1]

verifica = palindrome_three.replace(" ", "").lower()
verifica == verifica[::-1]

verifica = palindrome_four.replace(" ", "").lower()
verifica == verifica[::-1]