# Nome do vídeo: Análise de dados em uma tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, no final mostre
# Quantas vezes apareceu o valor 9, em que posição foi digitado o primeiro valor 3, quais foram os números pares

# Solicita que o usuário insira quatro números, cada um é adicionado à tupla `núm` em sequência
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

# Exibe todos os números que foram digitados pelo usuário
print(f'Você digitou os valores {núm}')

# Conta e exibe quantas vezes o número 9 apareceu na tupla
print(f'O valor 9 apareceu {núm.count(9)} vezes')

# Verifica se o número 3 está na tupla; se sim, exibe sua primeira posição
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

# Percorre a tupla e exibe apenas os números pares que foram digitados
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:  # Verifica se o número é par
        print(n, end=' ')  # Exibe o número par seguido de um espaço
