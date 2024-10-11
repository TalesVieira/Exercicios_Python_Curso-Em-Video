# Nome do vídeo: Ano bissexto
# Este programa determina se um ano é bissexto, considerando a regra de divisibilidade.

from datetime import date  # Importa a função date da biblioteca datetime para trabalhar com datas

# Solicita ao usuário o ano que deseja verificar, com a opção de colocar "0" para analisar o ano atual
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

# Verifica se o valor inserido é "0". Se for, o programa usa o ano atual
if ano == 0:
    ano = date.today().year  # Atribui o ano atual à variável ano

# Determina se o ano é bissexto usando as regras de divisibilidade:
# - O ano é bissexto se for divisível por 4 e não divisível por 100, exceto quando também for divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))  # Exibe que o ano é bissexto
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))  # Exibe que o ano não é bissexto
