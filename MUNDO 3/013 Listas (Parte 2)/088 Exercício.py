# Nome do vídeo: Palpites para a mega sena
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e sortear números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = list()  # Lista temporária para armazenar os números de cada jogo
jogos = list()  # Lista composta que vai armazenar todos os jogos gerados

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)

# Pergunta quantos jogos o usuário deseja gerar
quant = int(input('Quantos jogos você quer que eu sorteie? '))

tot = 1  # Contador para controlar o número de jogos gerados
while tot <= quant:  # Laço para gerar a quantidade de jogos solicitada
    cont = 0  # Contador para controlar a quantidade de números no jogo atual
    while True:
        num = randint(1, 60)  # Sorteia um número entre 1 e 60
        if num not in lista:  # Verifica se o número já foi sorteado no jogo atual
            lista.append(num)  # Adiciona o número à lista se não for repetido
            cont += 1  # Incrementa o contador de números sorteados
        if cont >= 6:  # Se já tiver 6 números, para de sortear
            break
    lista.sort()  # Ordena os números do jogo para exibição organizada
    jogos.append(lista[:])  # Adiciona uma cópia da lista do jogo na lista de jogos
    lista.clear()  # Limpa a lista para o próximo jogo
    tot += 1  # Incrementa o total de jogos gerados

# Exibe os jogos sorteados
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):  # Enumera os jogos para exibir na tela
    print(f'Jogo {i+1}: {l}')  # Exibe o jogo atual
    sleep(0.2)  # Pausa de 1 segundo para simular o sorteio

# Exibe mensagem de boa sorte
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
