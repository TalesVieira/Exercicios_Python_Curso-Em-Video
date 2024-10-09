# Nome do vídeo: Dissecado uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Lê um valor do teclado e armazena na variável 'a'
a = input('Digite algo: ')

# Exibe o tipo primitivo do valor digitado
print('O tipo primitivo desse valor é', type(a))

# Verifica se o valor só contém espaços
print('Só tem espaços?', a.isspace())

# Verifica se o valor é um número
print('É um número?', a.isnumeric())

# Verifica se o valor é alfabético
print('É alfabético?', a.isalpha())

# Verifica se o valor é alfanumérico
print('É alfanumérico?', a.isalnum())

# Verifica se o valor está em maiúsculas
print('Está em maiúsculas?', a.isupper())

# Verifica se o valor está em minúsculas
print('Está em minúsculas?', a.islower())

# Verifica se o valor está capitalizado (primeira letra maiúscula)
print('Está capitalizada?', a.istitle())
