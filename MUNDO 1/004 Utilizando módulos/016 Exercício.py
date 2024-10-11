# Nome do vídeo: Quebrando um número
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: digite um número: 6.127
# O número 6.127 tem a parte inteira 6

# Importa a função trunc da biblioteca math para obter a parte inteira do número
from math import trunc

# Lê o número real fornecido pelo usuário
num = float(input('Digite um valor: '))

# Exibe a parte inteira do número usando a função trunc
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
