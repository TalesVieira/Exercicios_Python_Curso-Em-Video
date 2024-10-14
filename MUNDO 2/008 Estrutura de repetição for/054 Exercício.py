# Nome do vídeo: Grupo da maioridade
# Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

from datetime import date  # Importa o módulo date da biblioteca datetime para trabalhar com datas

# Obtém o ano atual
atual = date.today().year

# Inicializa contadores para maiores e menores de idade
totmaior = 0 
totmenor = 0

# Laço que itera 7 vezes, uma para cada pessoa
for pess in range(1, 8):
    # Lê o ano de nascimento da pessoa
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))

    # Calcula a idade da pessoa
    idade = atual - nasc

    # Verifica se a pessoa é maior ou menor de idade
    if idade >= 21:  # Se a idade é maior ou igual a 21
        totmaior += 1  # Incrementa o contador de maiores de idade
    else:
        totmenor += 1  # Incrementa o contador de menores de idade

# Exibe o total de pessoas maiores de idade
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))

# Exibe o total de pessoas menores de idade
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
