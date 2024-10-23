# Nome do vídeo: Cadastro de jogador de futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso vai ser guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Criação do dicionário para armazenar os dados do jogador
jogador = dict()

# Criação da lista para armazenar a quantidade de gols feitos em cada partida
partidas = list()

# Solicitação do nome do jogador e armazenamento no dicionário
jogador['nome'] = str(input('Nome do jogador: '))

# Solicitação do número de partidas jogadas e armazenamento na variável 'tot'
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Laço para registrar a quantidade de gols feitos em cada partida
# O número de iterações será igual ao total de partidas jogadas
for c in range(0, tot):
    # Para cada partida, solicita o número de gols e adiciona à lista 'partidas'
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))

# Armazenamento da lista de gols no dicionário do jogador
jogador['gols'] = partidas[:]

# Cálculo e armazenamento do total de gols feitos durante o campeonato
jogador['total'] = sum(partidas)

# Exibição do dicionário com todos os dados do jogador
print('-=' * 30)
print(jogador)  # Mostra todo o dicionário com nome, gols e total

print('-=' * 30)

# Laço para exibir os dados de forma mais detalhada
# O método .items() retorna os pares de chave e valor do dicionário
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)

# Exibição da quantidade de partidas jogadas e os gols em cada uma delas
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

# Laço para exibir o número de gols em cada partida
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols')

# Exibição do total de gols feitos
print(f'Foi um total de {jogador["total"]} gols')
