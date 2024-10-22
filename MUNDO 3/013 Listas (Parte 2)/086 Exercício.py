# Nome do vídeo: Matriz em Python
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final mostre a matriz na tela com a formatação correta

# Inicializamos a matriz 3x3 com valores 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Laço para percorrer as linhas (l) e colunas (c) da matriz
for l in range(0, 3):  # Laço que percorre as 3 linhas da matriz
    for c in range(0, 3):  # Laço que percorre as 3 colunas de cada linha
        # Preenche a matriz com os valores lidos pelo teclado
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Linha decorativa para separar a entrada de dados da exibição da matriz
print('-=' * 30)

# Laço para exibir a matriz formatada
for l in range(0, 3):  # Percorre as linhas da matriz
    for c in range(0, 3):  # Percorre as colunas de cada linha
        # Exibe cada valor da matriz, centralizado em um espaço de 5 caracteres
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()  # Quebra de linha após cada linha da matriz ser exibida
