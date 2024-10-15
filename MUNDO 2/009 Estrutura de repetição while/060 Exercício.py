# Nome do vídeo: Cálculo do fatorial
# Faça um programa que leia um número qualquer e mostre seu fatorial

# Solicita um número do usuário para calcular o fatorial
n = int(input('Digite um número para calcular seu fatorial: '))

# Inicializa as variáveis: 'c' como contador decrescente e 'f' como o valor do fatorial
c = n 
f = 1 

# Inicia a saída visual do cálculo do fatorial
print('Calculando {}!'.format(n), end=' ')

# Loop para calcular o fatorial, multiplicando os números de 'n' até 1
while c > 0:
    print('{}'.format(c), end=' ')
    # Imprime 'x' como multiplicação ou '=' para o resultado final
    print('x' if c > 1 else '= ', end='')
    
    # Multiplica o valor atual de 'f' pelo contador 'c' e decrementa 'c'
    f *= c
    c -= 1

# Exibe o resultado do fatorial
print('{}'.format(f))
