# Nome do vídeo: Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido se o número digitado for negativo.

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))  # Solicita ao usuário o número para calcular a tabuada
    print('-' * 30)  # Imprime uma linha separadora
    if n < 0:  # Verifica se o número é negativo para interromper o programa
        break  # Sai do loop se o usuário digitar um número negativo
    for c in range(1, 11):  # Laço para gerar a tabuada de 1 a 10
        print(f'{n} X {c} = {n * c}')  # Exibe o resultado da multiplicação
    print('-' * 30)  # Imprime uma linha separadora após a tabuada
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')  # Mensagem final quando o programa for encerrado
