# Nome do vídeo: Catetos e hipotenusa
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Importa a função hypot da biblioteca math para calcular a hipotenusa
from math import hypot 

# Lê o comprimento do cateto oposto e do cateto adjacente
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# Calcula a hipotenusa usando a função hypot
hi = hypot(co, ca)

# Exibe o comprimento da hipotenusa com duas casas decimais
print('A hipotenusa vai medir {:.2f}'.format(hi))
