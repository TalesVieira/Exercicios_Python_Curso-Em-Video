# Nome do vídeo: Jogo da adivinhação v1.0
# Este programa faz o computador "pensar" em um número entre 0 e 5 e pede ao usuário para adivinhar o número.

# Importa as funções randint e sleep dos módulos random e time, respectivamente
from random import randint
from time import sleep

# Computador escolhe aleatoriamente um número entre 0 e 5
computador = randint(0, 5)

# Exibe a mensagem inicial de introdução ao jogo
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# Usuário insere sua tentativa de adivinhação
jogador = int(input('Em que número eu pensei? '))

# Mensagem de processamento com uma pausa de 3 segundos
print('PROCESSANDO...')
sleep(3)

# Verifica se o número escolhido pelo jogador é igual ao número escolhido pelo computador
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
