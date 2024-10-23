# Nome do vídeo: Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente além da idade com quantos anos a pessoa vai se aposentar.

from datetime import datetime  # Importa a biblioteca necessária para trabalhar com datas

# Criação do dicionário que armazenará os dados do trabalhador
# O dicionário "dados" conterá o nome, idade, CTPS (Carteira de Trabalho), e se aplicável, o ano de contratação, salário e aposentadoria.
dados = dict()

# Entrada de dados:
# Solicita o nome do trabalhador e o armazena no dicionário na chave 'nome'.
dados['nome'] = str(input('Nome: '))

# Solicita o ano de nascimento do trabalhador e calcula a idade com base no ano atual.
nasc = int(input('Ano de nascimento: '))
# A idade é calculada pela subtração do ano atual com o ano de nascimento e armazenada na chave 'idade'.
dados['idade'] = datetime.now().year - nasc

# Solicita o número da Carteira de Trabalho (CTPS). Se o valor for 0, indica que a pessoa não possui carteira de trabalho.
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

# Verificação se a CTPS é diferente de 0, ou seja, se o trabalhador possui carteira de trabalho.
if dados['ctps'] != 0:
    # Se o trabalhador tiver carteira de trabalho, são solicitados mais informações:
    
    # Solicita o ano de contratação do trabalhador e armazena na chave 'contratação'.
    dados['contratação'] = int(input('Ano de contratação: '))
    
    # Solicita o salário do trabalhador e armazena na chave 'salário'.
    dados['salário'] = float(input('Salário: R$'))

    # Cálculo da aposentadoria:
    # O cálculo considera que o trabalhador precisa de 35 anos de trabalho para se aposentar.
    # A idade de aposentadoria é calculada somando a idade atual com o número de anos restantes para completar 35 anos de trabalho.
    # Isso é feito pela fórmula: idade + (ano de contratação + 35 - ano atual).
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

# Exibição dos dados cadastrados:
# O laço "for" percorre o dicionário "dados" para exibir cada chave (nome, idade, CTPS, etc.) e seu respectivo valor (conteúdo).
print('-=' * 30)
for k, v in dados.items():
    # Para cada par chave-valor no dicionário, imprime a chave (ex: 'nome') e o valor associado (ex: 'João').
    print(f' - {k} tem o valor {v}')
