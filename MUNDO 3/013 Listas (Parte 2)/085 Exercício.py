# Nome do vídeo: Listas com pares e ímpares
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
# Separados os valores pares e ímpares, no final mostre os valores pares e ímpares em ordem crescente

# 'núm' é uma lista composta de duas sublistas:
# - A primeira sublista (núm[0]) armazenará os valores pares
# - A segunda sublista (núm[1]) armazenará os valores ímpares
núm = [[], []]
valor = 0  # Variável que armazenará o valor digitado temporariamente

# Loop para ler sete valores numéricos
for c in range(1, 8):  # O range vai de 1 a 7, pois o usuário deve digitar sete valores
    valor = int(input(f'Digite o {c}º valor: '))  # Solicita ao usuário que insira um valor

    # Se o valor for par, ele é adicionado à primeira sublista (pares)
    if valor % 2 == 0:
        núm[0].append(valor)  # Adiciona o valor à sublista de pares
    # Se o valor for ímpar, ele é adicionado à segunda sublista (ímpares)
    else:
        núm[1].append(valor)  # Adiciona o valor à sublista de ímpares

# Exibe a separação dos pares e ímpares e os organiza em ordem crescente
print('-=' * 30)  # Linha decorativa para separar a saída visualmente

# Ordena a sublista de pares em ordem crescente
núm[0].sort()

# Ordena a sublista de ímpares em ordem crescente
núm[1].sort()

# Exibe os valores pares
print(f'Os valores pares digitados foram: {núm[0]}')

# Exibe os valores ímpares
print(f'Os valores ímpares digitados foram: {núm[1]}')
