# Nome do vídeo: Somando dois números
# Crie um programa que leia dois números e mostre a soma entre eles.

# Solicita ao usuário que digite o primeiro número e converte para inteiro
n1 = int(input('Digite um valor: '))

# Solicita ao usuário que digite o segundo número e converte para inteiro
n2 = int(input('Digite outro valor: '))

# Calcula a soma dos dois números
s = n1 + n2

# Exibe o resultado da soma
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
