# Nome do vídeo: Contagem de pares
# Este programa exibe todos os números pares no intervalo entre 1 e 50.
# Utiliza um loop para percorrer apenas os números pares, economizando tempo e recursos.

# A função range() é usada para gerar uma sequência de números de 2 até 50, com passos de 2 em 2.
# Começamos em 2 e não em 1, pois sabemos que 2 é o primeiro número par nesse intervalo.
# O terceiro argumento '2' faz o loop pular de 2 em 2, o que significa que estamos gerando apenas números pares.
for n in range(2, 51, 2):
    print(n, end=' ')  # Exibe o número atual e adiciona um espaço para manter os números na mesma linha

# Após a exibição dos números pares, a mensagem 'Acabou' é exibida para indicar o fim do programa.
print('Acabou')  # Indica que a contagem terminou
