# Nome do vídeo: Lista de preços com tupla
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência, no final
# mostre uma listagem de preços, organizando os dados em forma tabular 

# Tupla contendo produtos e seus preços de forma alternada
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

# Exibe o cabeçalho da listagem com formatação centralizada
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Itera sobre a tupla usando um índice para alternar entre o nome do produto e seu preço
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        # Exibe o nome do produto alinhado à esquerda com preenchimento de pontos até 30 caracteres
        print(f'{listagem[pos]:.<30}', end='')
    else:
        # Exibe o preço do produto, alinhado à direita e formatado com 2 casas decimais
        print(f'R${listagem[pos]:>7.2f}')

# Exibe a linha final para fechamento da tabela
print('-' * 40)
