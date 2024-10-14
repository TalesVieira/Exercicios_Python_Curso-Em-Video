# Nome do vídeo: Números primos
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# Lê um número inteiro fornecido pelo usuário
núm = int(input('Digite um número: '))

# Inicializa a variável tot para contar quantas vezes o número é divisível
tot = 0

# Laço for para verificar todos os números de 1 até o número fornecido
for c in range(1, núm + 1):
    if núm % c == 0:  # Verifica se 'c' é um divisor do número
        print('\033[33m', end='')  # Muda a cor do texto para amarelo para divisores
        tot += 1  # Incrementa o contador de divisores
    else:
        print('\033[31m', end='')  # Muda a cor do texto para vermelho para não divisores
    print('{}'.format(c), end=' ')  # Exibe o número atual do loop

# Reseta a cor do texto para o padrão
print('\n\033[mO número {}, foi divisível {} vezes'.format(núm, tot))

# Verifica se o número é primo com base no contador de divisores
if tot == 2:  # Um número é primo se for divisível apenas por 1 e ele mesmo
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
