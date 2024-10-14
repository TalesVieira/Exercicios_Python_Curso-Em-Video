# Nome do vídeo: Tabuada v2.0
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for

num = int(input('Digite um número para ver sua tabuada: '))  # Lê um número inteiro fornecido pelo usuário e armazena na variável num

# Laço for que percorre os valores de 1 a 10, para calcular a tabuada do número escolhido
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))  # Exibe o resultado da multiplicação de 'num' por 'c' em um formato organizado
