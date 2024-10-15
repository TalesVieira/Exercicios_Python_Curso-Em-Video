# Nome do vídeo: Tratando valores v1.0
# Crie um programa que leia vários números inteiros digitados pelo teclado, o programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

núm = cont = soma = 0  # Inicializa as variáveis de controle para número, contador e soma

# Solicita o primeiro número ao usuário
núm = int(input('Digite um número [999 para parar]: '))

# Loop que continua até o usuário digitar 999
while núm != 999:
    soma += núm  # Adiciona o número à soma acumulada
    cont += 1  # Incrementa o contador de números digitados
    # Solicita o próximo número ao usuário
    núm = int(input('Digite um número [999 para parar]: '))

# Exibe o total de números digitados e a soma total (desconsiderando o flag 999)
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
