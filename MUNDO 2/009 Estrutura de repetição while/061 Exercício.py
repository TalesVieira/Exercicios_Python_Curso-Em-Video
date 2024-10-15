# Nome do vídeo: Progressão aritmética v2.0
# Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

# Exibe um título para o gerador de PA
print('Gerador de PA')
print('-=' * 10)

# Solicita ao usuário o primeiro termo da PA e a razão
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

# Define a variável 'termo' com o valor do primeiro termo
termo = primeiro
# Inicializa o contador para controlar o número de termos exibidos
cont = 1

# Laço 'while' para calcular e exibir os 10 primeiros termos da PA
while cont <= 10:
    # Exibe o termo atual e um separador '->' sem quebrar a linha
    print('{} ->'.format(termo), end=' ')
    
    # Incrementa o termo com o valor da razão para obter o próximo termo da PA
    termo += razão
    
    # Incrementa o contador
    cont += 1

# Exibe a mensagem de término da sequência
print('FIM')
