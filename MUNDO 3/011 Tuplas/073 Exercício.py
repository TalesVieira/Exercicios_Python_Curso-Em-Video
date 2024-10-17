# Nome do vídeo: Tuplas com times de futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol na ordem de colocação.
# O programa mostra: os 5 primeiros colocados, os 4 últimos, os times em ordem alfabética, e a posição da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')  # Corrigido para exibir os últimos 4 times corretamente
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')  # Corrigido "Chapecoense" para exibir a posição corretamente
