# Nome do vídeo: Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares
# se o valor digitado for ímpar desconsidere-o

soma = 0  # Inicializa a variável 'soma' para acumular a soma dos números pares
cont = 0  # Inicializa a variável 'cont' para contar quantos números pares foram digitados

# Laço for para receber seis números inteiros do usuário
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))  # Lê um número inteiro e o atribui à variável 'num'
    if num % 2 == 0:  # Verifica se o número é par (divisível por 2)
        soma += num  # Se for par, adiciona o valor de 'num' à variável 'soma'
        cont += 1  # Incrementa o contador de números pares

# Exibe a quantidade de números pares informados e a soma desses valores
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
