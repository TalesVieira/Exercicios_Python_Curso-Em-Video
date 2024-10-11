# Nome do vídeo: Par ou ímpar
# Este programa lê um número inteiro e determina se ele é PAR ou ÍMPAR.

# Lê um número inteiro inserido pelo usuário
número = int(input('Me diga um número qualquer: '))

# Calcula o resto da divisão do número por 2
resultado = número % 2

# Verifica se o resto é igual a zero, o que significa que o número é par
if resultado == 0:
    # Se o resto for zero, o número é par
    print('O número {} é PAR'.format(número))
else:
    # Se o resto não for zero, o número é ímpar
    print('O número {} é ÍMPAR'.format(número))
