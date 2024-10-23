# Nome do vídeo: Unindo dicionários e listas
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, o programa deve mostrar:
# 1) Quantas pessoas foram cadastradas
# 2) A média de idade
# 3) Uma lista com todas as mulheres cadastradas
# 4) Uma lista de pessoas com idade acima da média

galera = list()  # Lista para armazenar o dicionário de cada pessoa
pessoa = dict()  # Dicionário para armazenar os dados de cada pessoa
soma = 0         # Variável para somar as idades e calcular a média posteriormente

# Laço principal para o cadastro de várias pessoas
while True:
    pessoa.clear()  # Limpa o dicionário para evitar duplicação de dados de pessoas anteriores
    
    # Solicita o nome da pessoa e armazena no dicionário
    pessoa['nome'] = str(input('Nome: '))
    
    # Solicita o sexo da pessoa e valida a entrada para garantir que seja apenas 'M' ou 'F'
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]  # Converte a entrada para maiúscula e pega a primeira letra
        if pessoa['sexo'] in 'MF':  # Verifica se o sexo é válido
            break  # Se válido, sai do laço de validação
        print('ERRO! Por favor, digite apenas M ou F.')  # Exibe mensagem de erro caso a entrada seja inválida
    
    # Solicita a idade da pessoa e armazena no dicionário
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']  # Soma a idade da pessoa à variável 'soma' para calcular a média depois

    # Adiciona uma cópia do dicionário 'pessoa' à lista 'galera'
    galera.append(pessoa.copy())  # Necessário usar o método .copy() para evitar ligação entre os dicionários

    # Pergunta ao usuário se deseja continuar o cadastro e valida a resposta
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':  # Verifica se a resposta é válida (S ou N)
            break  # Sai do laço de validação se a resposta for válida
        print('ERRO! Responda apenas S ou N.')  # Exibe mensagem de erro caso a entrada seja inválida
    
    # Se o usuário responder 'N', o programa encerra o laço de cadastro
    if resp == 'N':
        break

# Exibe a quantidade total de pessoas cadastradas
print('-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

# Calcula e exibe a média de idade de todas as pessoas cadastradas
média = soma / len(galera)
print(f'A média de idade é de {média:.2f} anos.')

# Exibe a lista de todas as mulheres cadastradas
print('C) As mulheres cadastradas foram ', end='')
for p in galera:  # Percorre a lista de dicionários
    if p['sexo'] == 'F':  # Verifica se a pessoa é do sexo feminino
        print(f'{p["nome"]} ', end='')  # Exibe o nome das mulheres

print()

# Exibe a lista de pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:  # Percorre a lista de dicionários
    if p['idade'] >= média:  # Verifica se a idade da pessoa é maior ou igual à média
        print(' ', end='')
        for k, v in p.items():  # Para cada pessoa, exibe as informações detalhadas (nome, sexo e idade)
            print(f'{k} = {v}; ', end='')  # Exibe as chaves e valores do dicionário
        print()  # Pula uma linha ao final da exibição de cada pessoa

print('<< ENCERRADO >>')  # Mensagem final indicando o fim do programa
