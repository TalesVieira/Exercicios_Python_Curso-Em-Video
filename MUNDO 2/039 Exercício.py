# Nome do vídeo: Alistamento militar
# Este programa lê o ano de nascimento de um jovem e informa:
# - se ele ainda vai se alistar ao serviço militar,
# - se é o momento de se alistar,
# - ou se já passou do tempo para o alistamento.
# Além disso, o programa exibe o tempo que falta ou o tempo que já passou do prazo de alistamento.

# Importa o módulo 'date' para acessar o ano atual
from datetime import date

# Obtém o ano atual
atual = date.today().year

# Solicita ao usuário que insira o ano de nascimento
nasc = int(input('Ano de nascimento: '))

# Calcula a idade com base no ano atual e o ano de nascimento
idade = atual - nasc

# Exibe a idade calculada
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

# Verifica se o usuário deve se alistar agora, ainda vai se alistar ou já deveria ter se alistado
if idade == 18:
    # Se a idade é exatamente 18, é o momento de alistamento
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    # Se a idade é menor que 18, ainda faltam anos para o alistamento
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo  # Calcula o ano em que o usuário deverá se alistar
    print('Seu alistamento será em {}'.format(ano))
else:
    # Se a idade é maior que 18, o tempo de alistamento já passou
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo  # Calcula o ano em que o usuário deveria ter se alistado
    print('Seu alistamento foi em {}'.format(ano))
