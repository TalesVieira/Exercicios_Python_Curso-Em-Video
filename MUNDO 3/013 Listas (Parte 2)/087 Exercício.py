# Nome do vídeo: Mais sobre matriz em Python
# Aprimore o desafio anterior mostrando no final:
# - A soma de todos os valores pares digitados
# - A soma dos valores da terceira coluna
# - O maior valor da segunda linha

# Inicializamos a matriz 3x3 com valores 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0  # Variável para somar os valores pares
scol = 0  # Variável para somar os valores da terceira coluna
mai = 0   # Variável para armazenar o maior valor da segunda linha

# Preenchemos a matriz com valores fornecidos pelo usuário
for l in range(0, 3):  # Laço para percorrer as linhas
    for c in range(0, 3):  # Laço para percorrer as colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Exibição da matriz formatada
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        # Exibe cada valor da matriz centralizado
        print(f'[{matriz[l][c]:^5}]', end=' ')
        # Verifica se o valor é par e soma
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()  # Quebra de linha após cada linha da matriz ser exibida

print('-=' * 30)
# Exibe a soma dos valores pares
print(f'A soma dos valores pares é {spar}.')

# Soma dos valores da terceira coluna (coluna índice 2)
for l in range(0, 3):
    scol += matriz[l][2]
# Exibe a soma dos valores da terceira coluna
print(f'A soma dos valores da terceira coluna é {scol}.')

# Maior valor da segunda linha (linha índice 1)
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]  # Inicializa o maior valor com o primeiro elemento da segunda linha
    elif matriz[1][c] > mai:
        mai = matriz[1][c]  # Atualiza o maior valor se encontrar um valor maior

# Exibe o maior valor da segunda linha
print(f'O maior valor da segunda linha é {mai}.')
