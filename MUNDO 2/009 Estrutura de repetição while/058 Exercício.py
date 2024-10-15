# Nome do vídeo: Jogo da adivinhação v2.0
# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10,
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint  # Importa a função randint para gerar números aleatórios

# O computador escolhe um número aleatório entre 0 e 10
computador = randint(0, 10)

# Exibe uma mensagem inicial ao jogador
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

# Define as variáveis iniciais: `acertou` como False para iniciar o loop e `palpites` para contar as tentativas
acertou = False
palpites = 0

# Inicia o loop enquanto o jogador não acertar o número
while not acertou:
    jogador = int(input('Qual é seu palpite? '))  # Recebe o palpite do jogador
    palpites += 1  # Incrementa o número de tentativas

    # Verifica se o palpite está correto
    if jogador == computador:
        acertou = True  # Define `acertou` como True para encerrar o loop
    else:
        # Fornece uma dica dependendo se o palpite é menor ou maior que o número do computador
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

# Exibe uma mensagem final com o número total de palpites até o jogador acertar
print('Acertou com {} palpites. Parabéns!'.format(palpites))
