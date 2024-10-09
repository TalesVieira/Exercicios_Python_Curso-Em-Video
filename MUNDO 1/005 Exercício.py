# Nome do vídeo: Antecessor e Sucessor
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Lê um número inteiro do usuário e armazena na variável 'n'
n = int(input('Digite um número: '))

# Calcula o antecessor subtraindo 1
a = n - 1 

# Calcula o sucessor somando 1
s = n + 1

# Exibe o número digitado, seu antecessor e seu sucessor
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
