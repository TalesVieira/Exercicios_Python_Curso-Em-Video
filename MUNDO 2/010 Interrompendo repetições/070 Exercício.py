# Nome do vídeo: Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. Para cada produto, o programa deverá perguntar 
# se o usuário quer continuar. No final, mostre:
# - O total gasto na compra
# - Quantos produtos custaram mais de R$1000
# - O nome do produto mais barato

total = totmil = menor = cont = 0  # Inicializa variáveis de contadores e acumuladores
barato = ''  # Variável para armazenar o nome do produto mais barato

while True:
    produto = str(input('Nome do produto: '))  # Recebe o nome do produto
    preço = float(input('Preço: R$ '))  # Recebe o preço do produto
    cont += 1  # Conta o número de produtos inseridos
    total += preço  # Acumula o total gasto na compra
    
    if preço > 1000:  # Conta quantos produtos custam mais de R$1000
        totmil += 1

    # Identifica o produto mais barato
    if cont == 1 or preço < menor:  # No primeiro produto, ou se o preço for menor que o atual menor preço
        menor = preço
        barato = produto
    
    # Pergunta se o usuário quer continuar
    resp = ' '
    while resp not in 'SN':  # Valida a resposta do usuário
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':  # Interrompe o loop se a resposta for 'N'
        break

# Exibe os resultados finais
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato}, que custa R${menor:.2f}')
