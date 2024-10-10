# Nome do vídeo: Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Este programa lê o nome deles e escreve o nome do escolhido.

from random import choice

# Lê o nome dos quatro alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Cria uma lista com os nomes dos alunos
lista = [n1, n2, n3, n4]

# Usa a função choice para escolher aleatoriamente um nome da lista
escolhido = choice(lista)

# Exibe o nome do aluno escolhido
print('O aluno escolhido foi {}'.format(escolhido))
