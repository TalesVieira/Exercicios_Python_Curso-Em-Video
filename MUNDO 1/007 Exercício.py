# Nome do vídeo: Média Aritmética
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

# Lê a primeira nota do aluno e a armazena como um número decimal
n1 = float(input('Primeira nota do aluno: '))

# Lê a segunda nota do aluno e a armazena como um número decimal
n2 = float(input('Segunda nota do aluno: '))

# Calcula a média aritmética das duas notas
média = (n1 + n2) / 2

# Exibe a média entre as duas notas
print('A média entre {} e {} é igual a {:.2f}'.format(n1, n2, média))
