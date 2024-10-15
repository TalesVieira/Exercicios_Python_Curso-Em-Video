# Nome do vídeo: Maior e menor valores
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores,
# qual foi o maior e o menor número. O programa deve perguntar se o usuário quer ou não continuar a digitar valores.

resp = 'S'  # Variável de controle para a repetição, inicia com 'S' para entrar no loop
soma = quant = média = maior = menor = 0  # Inicializa variáveis para soma, quantidade, média, maior e menor

# Loop que continua enquanto o usuário quiser digitar novos números
while resp in 'Ss':
    núm = int(input('Digite um número: '))  # Solicita um número ao usuário
    soma += núm  # Soma o número atual à variável 'soma'
    quant += 1  # Incrementa a contagem de números digitados

    # Verifica se é o primeiro número inserido para inicializar maior e menor
    if quant == 1:
        maior = menor = núm  # Define o primeiro número como maior e menor
    else:
        if núm > maior:  # Atualiza o maior número se o número atual for maior que o anterior
            maior = núm
        if núm < menor:  # Atualiza o menor número se o número atual for menor que o anterior
            menor = núm

    # Pergunta ao usuário se deseja continuar e armazena a resposta na variável 'resp'
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# Calcula a média dos números digitados
média = soma / quant

# Exibe o total de números digitados, a média, o maior e o menor valor
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
