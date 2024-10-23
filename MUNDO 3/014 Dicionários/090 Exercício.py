# Nome do vídeo: Dicionário em Python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()  # Cria um dicionário para armazenar os dados do aluno

# Lê o nome e a média do aluno e armazena no dicionário
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# Verifica a situação do aluno com base na média
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

# Exibe os dados armazenados no dicionário de forma organizada
print('-=' * 30)
for k, v in aluno.items():  # Laço para exibir a chave e o valor do dicionário
    print(f' - {k} é igual a {v}')
