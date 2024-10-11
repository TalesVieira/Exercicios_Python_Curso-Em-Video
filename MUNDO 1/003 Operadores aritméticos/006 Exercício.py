# Nome do vídeo: Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Lê um número inteiro do usuário e armazena na variável 'n'
n = int(input('Digite um número: '))

# Calcula o dobro de 'n'
d = n * 2

# Calcula o triplo de 'n'
t = n * 3

# Calcula a raiz quadrada de 'n'
r = n ** (1/2)

# Exibe o dobro, triplo e raiz quadrada do número
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
