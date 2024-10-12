# Nome do vídeo: Classificando atletas
# Este programa lê o ano de nascimento de um atleta e determina sua categoria de natação:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

# Obtém o ano atual
atual = date.today().year

# Lê o ano de nascimento do atleta
nascimento = int(input('Ano de nascimento: '))

# Calcula a idade do atleta
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))

# Determina e exibe a categoria do atleta com base na idade
if idade <= 9:
    # Categoria para atletas com até 9 anos
    print('Classificação: MIRIM')
elif idade <= 14:
    # Categoria para atletas com até 14 anos
    print('Classificação: INFANTIL')
elif idade <= 19:
    # Categoria para atletas com até 19 anos
    print('Classificação: JUNIOR')
elif idade <= 25:
    # Categoria para atletas com até 25 anos
    print('Classificação: SÊNIOR')
else:
    # Categoria para atletas acima de 25 anos
    print('Classificação: MASTER')
