# Nome do vídeo: Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista, no final mostre:
# Quantas pessoas foram cadastradas, uma listagem das pessoas mais pesadas, uma listagem com as pessoas mais leves

# 'temp' é a lista temporária usada para armazenar os dados de uma pessoa (nome e peso)
# 'princ' é a lista principal que armazenará todas as pessoas
temp = []
princ = []
mai = men = 0  # Variáveis que armazenarão o maior e o menor peso

# Loop principal para cadastrar várias pessoas
while True:
    temp.append(str(input('Nome: ')))  # Adiciona o nome à lista temporária
    temp.append(float(input('Peso: ')))  # Adiciona o peso à lista temporária

    # Se for a primeira pessoa cadastrada, inicializa 'mai' e 'men' com o peso dessa pessoa
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        # Verifica se o peso atual é maior que o maior peso registrado
        if temp[1] > mai:
            mai = temp[1]
        # Verifica se o peso atual é menor que o menor peso registrado
        if temp[1] < men:
            men = temp[1]

    # Adiciona uma cópia da lista temporária à lista principal e limpa a lista temporária para o próximo cadastro
    princ.append(temp[:])  # Cria uma cópia de 'temp' e armazena em 'princ'
    temp.clear()  # Limpa a lista temporária para o próximo cadastro

    # Pergunta ao usuário se ele quer continuar cadastrando
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break  # Sai do loop se o usuário digitar 'N'

# Exibe quantas pessoas foram cadastradas
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')

# Exibe o maior peso e as pessoas que possuem esse peso
print(f'O maior peso foi de {mai}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()

# Exibe o menor peso e as pessoas que possuem esse peso
print(f'O menor peso foi de {men}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
