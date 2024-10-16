# Nome do vídeo: Vários números com flag
# Crie um programa que leia vários números pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

soma = cont = 0  # Inicializa as variáveis para a soma dos números e a contagem

# Inicia um loop infinito para leitura dos números
while True:
    num = int(input('Digite um valor (999 para parar): '))  # Solicita um número ao usuário

    # Verifica se o número é o flag de parada
    if num == 999:
        break  # Sai do loop se o usuário digitar 999

    cont += 1  # Incrementa o contador para cada número digitado
    soma += num  # Adiciona o número digitado à soma total

# Exibe a quantidade de números digitados e a soma total
print(f'A soma dos {cont} valores foi {soma}')
