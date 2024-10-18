# Nome do vídeo: Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados. Ao final, mostre o conteúdo das 3 listas geradas.

# Inicializando as três listas: 'num' para todos os números, 'pares' para os números pares, e 'ímpares' para os ímpares.
num = list()
pares = list()
ímpares = list()

# Loop principal para inserção de valores
while True:
    # Adiciona o valor digitado pelo usuário à lista 'num'
    num.append(int(input('Digite um número: ')))
    
    # Pergunta ao usuário se deseja continuar inserindo valores
    resp = str(input('Quer continuar? [S/N] '))
    
    # Se o usuário responder 'N' ou 'n', o loop é interrompido
    if resp in 'Nn':
        break

# Loop para classificar os números como pares ou ímpares
for i, v in enumerate(num):
    # Se o número for par, ele é adicionado à lista 'pares'
    if v % 2 == 0:
        pares.append(v)
    # Se o número for ímpar, ele é adicionado à lista 'ímpares'
    elif v % 2 == 1:
        ímpares.append(v)

# Exibindo uma linha de separação visual
print('-=' * 30)

# Exibindo o conteúdo das três listas
print(f'A lista completa é: {num}')  # Exibe todos os números digitados
print(f'A lista de pares é: {pares}')  # Exibe apenas os números pares
print(f'A lista de ímpares é: {ímpares}')  # Exibe apenas os números ímpares
