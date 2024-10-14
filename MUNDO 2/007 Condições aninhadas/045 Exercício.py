# Nome do vídeo: GAME: pedra, papel e tesoura
# Este programa permite ao jogador jogar Pedra, Papel e Tesoura contra o computador.

from random import randint

# Definindo as opções de jogadas
itens = ('Pedra', 'Papel', 'Tesoura')

# Computador escolhe aleatoriamente entre Pedra, Papel e Tesoura
computador = randint(0, 2)

# Exibe as opções para o jogador
print(''' Suas opções: 
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')

# Lê a jogada do jogador
jogador = int(input('Qual é a sua jogada? '))

# Exibe as jogadas do computador e do jogador
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

# Verifica o resultado da partida
if computador == 0:  # Computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 1:  # Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')
