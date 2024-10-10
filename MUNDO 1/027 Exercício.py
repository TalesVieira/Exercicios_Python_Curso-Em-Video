# Nome do vídeo: Primeiro e último nome de uma pessoa
# Este programa lê o nome completo de uma pessoa e mostra o primeiro e o último nome separadamente.

# Solicita ao usuário que insira seu nome completo, remove espaços extras no início e no fim
n = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista onde cada palavra é um elemento da lista
nome = n.split()

# Exibe uma mensagem de saudação
print('Muito prazer em te conhecer!')

# Mostra o primeiro nome, que é o primeiro elemento da lista
print('Seu primeiro nome é {}'.format(nome[0]))

# Mostra o último nome, que é o último elemento da lista, acessado pela posição -1
print('Seu último nome é {}'.format(nome[-1]))
