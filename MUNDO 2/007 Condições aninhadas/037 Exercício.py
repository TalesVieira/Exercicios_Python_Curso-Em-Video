# Nome do vídeo: Conversor de bases numéricas
# Este programa converte um número inteiro para uma base numérica escolhida pelo usuário:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# Solicita um número inteiro do usuário
num = int(input('Digite um número inteiro: '))

# Apresenta as opções de conversão
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')

# Solicita ao usuário que escolha uma base de conversão
opção = int(input('Sua opção: '))

# Condicional para verificar a escolha e realizar a conversão para a base selecionada
if opção == 1:
    # Converte o número para binário e remove o prefixo '0b' do resultado
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    # Converte o número para octal e remove o prefixo '0o' do resultado
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    # Converte o número para hexadecimal e remove o prefixo '0x' do resultado
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    # Informa ao usuário caso a opção seja inválida
    print('Opção inválida. Tente novamente')
