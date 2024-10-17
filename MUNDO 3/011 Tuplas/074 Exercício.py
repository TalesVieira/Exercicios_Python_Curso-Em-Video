# Nome do vídeo: Maior e menor valores em tupla
# Este programa gera cinco números aleatórios, coloca-os em uma tupla e exibe a listagem dos números gerados,
# além de indicar o menor e o maior valor na tupla.

# Importando a função randint da biblioteca random para gerar números aleatórios
from random import randint

# Gerando cinco números aleatórios entre 1 e 10 e armazenando-os em uma tupla chamada 'numeros'
# As tuplas são imutáveis, o que significa que, uma vez criadas, seus valores não podem ser alterados.
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Exibindo os valores sorteados
# Usamos end=' ' para que os números sejam exibidos na mesma linha, separados por um espaço
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')  # Exibe cada número sorteado com um espaço entre eles

# Quebra de linha para separar o resultado da linha anterior
print(f'\nO maior valor sorteado foi {max(numeros)}')  # A função max() retorna o maior valor da tupla 'numeros'
print(f'O menor valor sorteado foi {min(numeros)}')    # A função min() retorna o menor valor da tupla 'numeros'
