# Nome do vídeo: detector de palíndromo
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

# Lê uma frase do usuário, remove espaços em branco do início e do fim, e converte para letras maiúsculas
frase = str(input('Digite uma frase: ')).strip().upper()

# Separa as palavras da frase em uma lista
palavras = frase.split()

# Junta todas as palavras em uma única string, removendo os espaços
junto = ''.join(palavras)

# Inverte a string resultante
inverso = junto[::-1]

# Exibe a string original e sua versão invertida
print('O inverso de {} é {}'.format(junto, inverso))

# Compara a string invertida com a original (sem espaços)
if inverso == junto:  # Se forem iguais, a frase é um palíndromo
    print('Temos um palíndromo!')
else:  # Se não forem iguais, a frase não é um palíndromo
    print('A frase digitada não é um palíndromo')
