# Nome do vídeo: Criando um menu de opções 
# Faça um programa que leia dois valores e mostre na tela um menu com as opções:
# [ 1 ] SOMAR, [ 2 ] MULTIPLICAR, [ 3 ] MAIOR, [ 4 ] NOVOS NÚMEROS, [ 5 ] SAIR DO PROGRAMA

# Solicita os dois primeiros valores ao usuário
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

# Inicializa a variável opção para controlar o loop
opção = 0

# Inicia o loop enquanto a opção selecionada for diferente de 5
while opção != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    
    # Solicita ao usuário a opção desejada do menu
    opção = int(input('>>>>> Qual é a sua opção? '))

    # Verifica qual operação deve ser realizada de acordo com a opção escolhida
    if opção == 1:
        # Soma os valores e exibe o resultado
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        # Multiplica os valores e exibe o resultado
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        # Determina qual valor é maior e exibe o resultado
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        # Solicita novos valores para realizar operações
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        # Encerra o programa
        print('PROGRAMA FINALIZADO')
    else:
        # Trata caso de opção inválida
        print('Opção inválida. Tente novamente.')

print('Fim do programa. Volte sempre!')
