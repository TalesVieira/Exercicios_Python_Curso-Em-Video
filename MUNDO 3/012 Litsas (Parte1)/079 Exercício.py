# Nome do vídeo: Valores únicos em uma lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já 
# exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores digitados em ordem crescente.

# Inicializando uma lista vazia para armazenar os números
números = list()

# Loop principal para a inserção dos valores
while True:
    n = int(input('Digite um valor: '))  # Solicita ao usuário que digite um número
    
    # Verifica se o número já está na lista
    if n not in números:
        números.append(n)  # Adiciona o número à lista se ele ainda não existir
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')  # Informa que o número já está na lista

    # Pergunta ao usuário se deseja continuar inserindo valores
    r = str(input('Quer continuar? [S/N] '))
    
    # Se a resposta for "N" ou "n", o loop é interrompido
    if r in 'Nn':
        break

# Exibe uma linha de separação
print('-=' * 30)

# Ordena a lista em ordem crescente
números.sort()

# Exibe os valores únicos digitados, já ordenados
print(f'Você digitou os valores {números}')
