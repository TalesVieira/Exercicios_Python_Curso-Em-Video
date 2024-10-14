# Nome do vídeo: Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

# Inicializa variáveis para somar as idades, armazenar a idade e o nome do homem mais velho e contar mulheres com menos de 20 anos
somaidade = 0 
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# Loop para coletar informações de 4 pessoas
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()  # Lê o nome e remove espaços em branco
    idade = int(input('Idade: '))  # Lê a idade da pessoa
    sexo = str(input('Sexo [M/F]: ')).strip()  # Lê o sexo e remove espaços em branco

    # Acumula a idade para calcular a média
    somaidade += idade

    # Verifica se a pessoa é a primeira ou o homem mais velho
    if sexo in 'Mm' and (p == 1 or idade > maioridadehomem):
        maioridadehomem = idade  # Atualiza a idade do homem mais velho
        nomevelho = nome  # Atualiza o nome do homem mais velho

    # Conta quantas mulheres têm menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

# Calcula a média de idade do grupo
mediaidade = somaidade / 4

# Exibe os resultados
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo, são {} mulheres com menos de 20 anos'.format(totmulher20))
