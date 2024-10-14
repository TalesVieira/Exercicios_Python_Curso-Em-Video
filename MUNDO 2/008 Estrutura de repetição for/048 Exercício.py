# Nome do vídeo: Soma ímpares múltiplos de três
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500

soma = 0  # Inicializa a variável para acumular a soma dos valores válidos
cont = 0  # Inicializa o contador para contar os números que atendem aos critérios

# Usa um loop para iterar pelos números ímpares de 1 a 500
for c in range(1, 501, 2):  
    if c % 3 == 0:  # Verifica se o número atual é múltiplo de 3
        soma += c  # Se for múltiplo de 3, adiciona à variável 'soma'
        cont += 1  # Incrementa o contador para cada número que atende ao critério

# Exibe o total de números que foram somados e o valor total da soma
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
