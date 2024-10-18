# Nome do vídeo: Extraindo dados de uma lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# 1. Quantos números foram digitados.
# 2. A lista de valores ordenada de forma decrescente.
# 3. Se o valor 5 foi digitado e está ou não na lista.

# Inicializando a lista vazia para armazenar os valores digitados
valores = []

# Loop principal para inserção de valores
while True:
    # Adiciona o valor digitado pelo usuário à lista
    valores.append(int(input('Digite um valor: ')))
    
    # Pergunta ao usuário se deseja continuar inserindo valores
    resp = str(input('Quer continuar? [S/N] '))
    
    # Se o usuário responder 'N' ou 'n', o loop é interrompido
    if resp in 'Nn':
        break

# Exibindo uma linha de separação visual
print('-=' * 30)

# Exibindo a quantidade de elementos que foram digitados
print(f'Você digitou {len(valores)} elementos.')

# Ordenando a lista em ordem decrescente
valores.sort(reverse=True)

# Exibindo os valores da lista em ordem decrescente
print(f'Os valores em ordem decrescente são: {valores}')

# Verificando se o valor 5 está presente na lista
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
