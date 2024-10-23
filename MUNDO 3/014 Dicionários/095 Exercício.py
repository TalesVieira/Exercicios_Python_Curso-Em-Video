# Nome do vídeo: Aprimorando os dicionários
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador

time = list()  # Lista que irá armazenar todos os jogadores
jogador = dict()  # Dicionário que armazenará os dados individuais de cada jogador
partidas = list()  # Lista que armazenará a quantidade de gols por partida para cada jogador

while True:  
    jogador.clear()  # Limpa os dados do jogador anterior para registrar um novo jogador
    jogador['nome'] = str(input('Nome do jogador: '))  # Solicita o nome do jogador
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # Solicita o número de partidas jogadas
    partidas.clear()  # Limpa a lista de partidas para o próximo jogador
    for c in range(0, tot):  
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))  # Adiciona a quantidade de gols para cada partida jogada
    jogador['gols'] = partidas[:]  # Armazena a lista de gols no dicionário do jogador
    jogador['total'] = sum(partidas)  # Calcula e armazena o total de gols feitos no campeonato
    time.append(jogador.copy())  # Adiciona os dados do jogador ao time (lista de jogadores)
    
    while True:  
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]  # Pergunta se o usuário deseja continuar
        if resp in 'SN':  
            break  # Sai do loop se a resposta for válida
        print('ERRO! Responda apenas S ou N.')  # Exibe mensagem de erro se a resposta for inválida
    
    if resp == 'N':  
        break  # Sai do loop principal se o usuário não quiser continuar

# Exibição dos dados cadastrados
print('-=' * 30)  
print('cod ', end=' ')  
for i in jogador.keys():  
    print(f'{i:<15}', end='')  # Cabeçalho mostrando as chaves do dicionário (nome, gols, total)
print()
for k, v in enumerate(time):  
    print(f'{k:<3}', end='')  # Exibe o índice do jogador (código)
    for d in v.values():  
        print(f'{str(d):<15}', end='')  # Exibe os valores do jogador (nome, gols e total)
print('-' * 40)  

# Sistema de busca de dados detalhados por jogador
while True:  
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))  
    if busca == 999:  
        break  # Encerra o programa se o usuário digitar 999
    if busca >= len(time):  
        print(f'ERRO! Não existe jogador com código {busca}!')  # Mensagem de erro caso o código não exista
    else:  
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')  # Exibe os dados detalhados do jogador
        for i, g in enumerate(time[busca]['gols']):  
            print(f'  No jogo {i+1} fez {g} gols.')  # Exibe o número de gols feitos em cada partida
print('<< VOLTE SEMPRE >>')  # Mensagem de finalização do programa
