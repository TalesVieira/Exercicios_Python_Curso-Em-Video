# Nome do vídeo: Jogo de Dados em Python
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário e, no final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# Gera os resultados dos 4 jogadores, cada um tirando um número entre 1 e 6
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

# Exibe os resultados sorteados
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

# Ordena os jogadores pelo valor do dado em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Exibe o ranking dos jogadores
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)  # Corrige o erro de digitação no "sleep"
