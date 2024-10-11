# Nome do vídeo: Primeira e última ocorrência de uma string.
# Este programa analisa a ocorrência da letra "A" em uma frase fornecida pelo usuário.

# Solicita que o usuário insira uma frase, converte para maiúsculas e remove espaços extras no início e no final
frase = str(input('Digite uma frase: ')).upper().strip()

# Conta quantas vezes a letra 'A' aparece na frase
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

# Encontra a posição da primeira ocorrência da letra 'A' (soma 1 para dar a posição considerando o início em 1)
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))

# Encontra a posição da última ocorrência da letra 'A' (soma 1 para a posição correta)
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))
