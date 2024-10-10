# Nome do vídeo: Sorteando uma ordem na lista
# Este programa sorteia a ordem de apresentação de trabalhos dos alunos.
from random import shuffle

# Lê o nome dos quatro alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Cria uma lista com os nomes dos alunos
lista = [n1, n2, n3, n4]

# Usa a função shuffle para embaralhar a lista
shuffle(lista)

# Exibe a ordem de apresentação dos alunos
print('A ordem de apresentação será:')
print(lista)
