# Nome do vídeo: Analisador de textos
# Este programa lê o nome completo de uma pessoa e exibe:
# 1. O nome em maiúsculas e minúsculas.
# 2. A quantidade total de letras, sem contar os espaços.
# 3. A quantidade de letras no primeiro nome.

# Lê o nome completo da pessoa e remove espaços extras nas extremidades
nome = str(input('Digite seu nome completo: ')).strip()

# Exibe uma mensagem de análise
print('Analisando seu nome...')

# Exibe o nome em letras maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# Exibe o nome em letras minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Calcula e exibe o total de letras, desconsiderando os espaços
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

# Divide o nome em partes para acessar o primeiro nome
separa = nome.split()

# Exibe o primeiro nome e a quantidade de letras que ele possui
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
