# Nome do vídeo: Jogo do par ou ímpar
# Faça um programa que jogue par ou ímpar com o computador, o jogo só será interrompido quando o jogador PERDER mostrando no final
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0  # Variável para contar o número de vitórias consecutivas
while True:
    jogador = int(input('Diga um valor: '))  # Jogador escolhe um número
    computador = randint(0, 10)  # Computador escolhe um número aleatório entre 0 e 10
    total = jogador + computador  # Soma dos valores do jogador e do computador
    tipo = ' '
    while tipo not in 'PI':  # Validação da escolha de Par ou Ímpar pelo jogador
        tipo = str(input('Par ou Ímpar [P/I] ')).strip().upper()[0]
    
    # Exibe os valores e o resultado da soma
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    
    # Verifica o resultado do jogo
    if tipo == 'P':
        if total % 2 == 0:  # Jogador vence se escolheu "Par" e o total é par
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu')
            break  # Sai do loop se o jogador perdeu
    elif tipo == 'I':
        if total % 2 == 1:  # Jogador vence se escolheu "Ímpar" e o total é ímpar
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break  # Sai do loop se o jogador perdeu
    print('Vamos jogar novamente...')  # Mensagem de continuação do jogo

# Mensagem final exibindo o número de vitórias consecutivas do jogador
print(f'GAME OVER! Você venceu {v} vezes.')
