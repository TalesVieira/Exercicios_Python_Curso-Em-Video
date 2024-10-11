# Nome do vídeo: Maior e menor valores
# Este programa lê três números e determina qual é o maior e qual é o menor entre eles.

# Entrada de dados: Solicita ao usuário três valores inteiros
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Inicializa a variável 'menor' com o valor de 'a' para comparação
menor = a
# Verifica se 'b' é menor que 'a' e 'c'; se for, 'menor' recebe o valor de 'b'
if b < a and b < c:
    menor = b
# Verifica se 'c' é menor que 'a' e 'b'; se for, 'menor' recebe o valor de 'c'
if c < b and c < a:
    menor = c

# Inicializa a variável 'maior' com o valor de 'a' para comparação
maior = a
# Verifica se 'b' é maior que 'a' e 'c'; se for, 'maior' recebe o valor de 'b'
if b > a and b > c:
    maior = b
# Verifica se 'c' é maior que 'a' e 'b'; se for, 'maior' recebe o valor de 'c'
if c > b and c > a:
    maior = c

# Saída de dados: Exibe o maior e o menor valor dentre os três valores inseridos
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
