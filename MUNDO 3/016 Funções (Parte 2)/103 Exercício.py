# Nome do vídeo: Ficha do jogador
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deve ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    """
    -> Exibe a ficha de um jogador com nome e número de gols.
    :param jog: Nome do jogador (opcional).
    :param gol: Número de gols marcados pelo jogador (opcional).
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

# Programa principal
n = str(input("Nome do jogador: "))  # Recebe o nome do jogador
g = str(input("Número de gols: "))  # Recebe o número de gols como string

# Verifica se o valor inserido em 'g' é numérico
if g.isnumeric():
    g = int(g)  # Converte para inteiro se for numérico
else:
    g = 0  # Define como 0 se o valor não for um número

# Verifica se o nome do jogador foi informado ou se está vazio
if n.strip() == '':
    ficha(gol=g)  # Chama a função com o número de gols, mas sem o nome do jogador
else:
    ficha(n, g)  # Chama a função com o nome e o número de gols
