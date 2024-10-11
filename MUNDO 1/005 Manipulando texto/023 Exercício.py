# Nome do vídeo: Separando dígitos de um número
# Este programa lê um número de 0 a 9999 e exibe os dígitos separados em unidade, dezena, centena e milhar.

# Lê um número inteiro entre 0 e 9999 fornecido pelo usuário
num = int(input('Informe um número: '))

# Calcula o dígito da unidade
u = num // 1 % 10

# Calcula o dígito da dezena
d = num // 10 % 10

# Calcula o dígito da centena
c = num // 100 % 10

# Calcula o dígito do milhar
m = num // 1000 % 10

# Exibe o número analisado
print('Analisando o número {}'.format(num))

# Exibe cada dígito separadamente
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
