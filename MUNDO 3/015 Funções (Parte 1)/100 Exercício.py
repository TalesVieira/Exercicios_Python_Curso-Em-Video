# Nome do vídeo: Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista.
# A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint  # Importa a função randint para gerar números aleatórios
from time import sleep  # Importa a função sleep para criar pausas entre as operações

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    # Sorteia 5 números aleatórios de 1 a 10 e adiciona à lista
    for cont in range(0, 5):
        n = randint(1, 10)  # Gera um número aleatório entre 1 e 10
        lista.append(n)  # Adiciona o número à lista
        print(f'{n}', end=' ', flush=True)  # Exibe o número sorteado com uma pequena pausa
        sleep(0.3)  # Pausa de 0.3 segundos entre os números
    print('PRONTO!')

def somaPar(lista):
    soma = 0  # Inicializa a soma dos valores pares
    # Itera sobre os valores da lista e soma apenas os números pares
    for valor in lista:
        if valor % 2 == 0:  # Verifica se o número é par
            soma += valor  # Adiciona o número par à soma
    # Exibe a soma dos valores pares
    print(f'Somando os valores pares de {lista}, temos {soma}')

# Cria uma lista vazia para armazenar os números sorteados
números = list()
# Chama a função sorteia() para preencher a lista com 5 números aleatórios
sorteia(números)
# Chama a função somaPar() para calcular e exibir a soma dos números pares da lista
somaPar(números)
