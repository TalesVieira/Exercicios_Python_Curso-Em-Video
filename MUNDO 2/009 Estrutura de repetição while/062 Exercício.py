# Nome do vídeo: Super progressão aritmética v3.0
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos

# Exibe um título para o gerador de PA
print('Gerador de PA')
print('-=' * 10)

# Solicita ao usuário o primeiro termo da PA e a razão
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

# Define a variável 'termo' com o valor do primeiro termo e inicializa contadores
termo = primeiro
cont = 1
total = 0  # Contabiliza o total de termos exibidos
mais = 10  # Inicialmente, define para exibir 10 termos

# Laço 'while' para calcular e exibir os termos da PA, conforme o desejo do usuário
while mais != 0:
    # Incrementa o total de termos com o número atual de termos desejados
    total = total + mais

    # Exibe a quantidade atual de termos desejada
    while cont <= total:
        # Exibe o termo atual e um separador '->' sem quebrar a linha
        print('{} ->'.format(termo), end=' ')
        
        # Incrementa o termo com a razão para obter o próximo termo da PA
        termo += razão
        
        # Incrementa o contador de termos exibidos
        cont += 1
    
    # Pausa após a exibição dos termos atuais e pede ao usuário a quantidade de termos adicionais
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

# Exibe a mensagem de término e o total de termos mostrados
print('Progressão finalizada com {} termos mostrados'.format(total))
