# Nome do vídeo: Comparando números
# Este programa lê dois números inteiros e compara-os, exibindo uma mensagem que indica:
# - se o primeiro valor é maior,
# - se o segundo valor é maior,
# - ou se ambos são iguais.

# Solicita ao usuário que insira o primeiro número inteiro
n1 = int(input('Primeiro valor: '))

# Solicita ao usuário que insira o segundo número inteiro
n2 = int(input('Segundo valor: '))

# Compara os valores e exibe a mensagem apropriada
if n1 > n2:
    # Informa que o primeiro valor é maior que o segundo
    print('O primeiro valor é maior')
elif n2 > n1:
    # Informa que o segundo valor é maior que o primeiro
    print('O segundo valor é maior')
else:
    # Informa que ambos os valores são iguais
    print('Os dois valores são IGUAIS')
