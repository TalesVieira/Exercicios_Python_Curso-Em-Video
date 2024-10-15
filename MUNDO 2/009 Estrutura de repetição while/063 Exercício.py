# Nome do vídeo: Sequência de fibonacci v1.0
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci

# Exibe cabeçalho para o programa
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

# Solicita ao usuário o número de termos que deseja mostrar na sequência
n = int(input('Quantos termos você quer mostrar? '))

# Define os dois primeiros termos da sequência de Fibonacci
t1 = 0
t2 = 1

# Exibe os primeiros termos formatados
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')

# Inicializa o contador a partir do terceiro termo, pois os dois primeiros já foram exibidos
cont = 3

# Usa um laço while para calcular e exibir os próximos termos até alcançar o número desejado pelo usuário
while cont <= n:
    t3 = t1 + t2  # Calcula o próximo termo da sequência somando os dois anteriores
    print(' -> {} '.format(t3), end=' ')  # Exibe o termo atual sem quebrar a linha
    
    # Atualiza os valores de t1 e t2 para os próximos cálculos
    t1 = t2
    t2 = t3
    
    # Incrementa o contador para continuar o loop até o número desejado
    cont += 1

# Exibe o término da sequência
print('FIM')
print('~' * 30)
