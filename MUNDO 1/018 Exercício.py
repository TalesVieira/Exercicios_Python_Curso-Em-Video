# Nome do vídeo: Seno, cosseno e tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importa as funções radians, sin, cos e tan da biblioteca math
from math import radians, sin, cos, tan

# Lê o ângulo em graus
ângulo = float(input('Digite o ângulo que você deseja: '))

# Calcula o seno, cosseno e tangente do ângulo, convertendo-o para radianos
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

# Exibe os resultados formatados com duas casas decimais
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
