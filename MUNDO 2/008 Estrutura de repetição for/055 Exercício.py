# Nome do vídeo: Maior e menor na sequência
# Faça um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior e o menor peso lidos.

# Inicializa as variáveis para armazenar o maior e menor peso
maior = 0
menor = 0

# Laço para repetir a leitura de peso 5 vezes
for p in range(1, 6):
    # Lê o peso da pessoa atual
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    
    # Para a primeira pessoa, define o maior e menor peso com o valor lido
    if p == 1:
        maior = peso
        menor = peso
    else:
        # Atualiza o maior peso se o peso atual for maior que o armazenado
        if peso > maior:
            maior = peso
        
        # Atualiza o menor peso se o peso atual for menor que o armazenado
        if peso < menor:
            menor = peso

# Exibe o maior peso lido
print('O maior peso lido foi de {:.2f}kg'.format(maior))

# Exibe o menor peso lido
print('O menor peso lido foi de {:.2f}kg'.format(menor))
