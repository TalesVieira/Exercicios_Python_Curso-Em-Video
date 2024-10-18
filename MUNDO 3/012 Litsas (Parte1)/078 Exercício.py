# Nome do vídeo: Maior e menor valores na lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista, no final do programa mostre qual foi o maior 
# e o menor valor digitado e suas respectivas posições

# Inicializando uma lista vazia para armazenar os números digitados
listanum = []

# Variáveis para armazenar o maior e o menor valor (inicialmente zero)
mai = 0
men = 0

# Loop para ler 5 valores numéricos e adicioná-los à lista
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))  # Adiciona o valor à lista
    # Na primeira iteração, define tanto o maior quanto o menor como o primeiro valor da lista
    if c == 0:
        mai = men = listanum[c]
    else:
        # Atualiza o maior valor se o número atual for maior que o maior armazenado
        if listanum[c] > mai:
            mai = listanum[c]
        # Atualiza o menor valor se o número atual for menor que o menor armazenado
        if listanum[c] < men:
            men = listanum[c]

# Exibe a lista de valores digitados
print('-=' * 30)
print(f'Você digitou os valores {listanum}')

# Exibe o maior valor e suas respectivas posições na lista
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')  # Mostra cada posição em que o maior valor aparece

# Exibe o menor valor e suas respectivas posições na lista
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')  # Mostra cada posição em que o menor valor aparece
print()
