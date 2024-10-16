# Nome do vídeo: Simulador de caixa eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico, 
# perguntando ao usuário qual será o valor a ser sacado e informando 
# quantas cédulas de cada valor serão entregues.

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))  # Cabeçalho do banco
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))  # Solicita o valor a ser sacado
total = valor  # Inicializa o total com o valor solicitado
céd = 50  # Inicializa a cédula de maior valor
totcéd = 0  # Contador de cédulas

while True:
    if total >= céd:  # Verifica se o total ainda é maior ou igual à cédula atual
        total -= céd  # Subtrai o valor da cédula do total
        totcéd += 1  # Incrementa o contador de cédulas
    else:  # Se não houver mais dinheiro suficiente para a cédula atual
        if totcéd > 0:  # Se alguma cédula foi contabilizada
            print(f'Total de {totcéd} cédulas de R${céd}')  # Mostra a quantidade de cédulas
        # Atualiza o valor da cédula para a próxima menor
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0  # Reinicia o contador de cédulas
        if total == 0:  # Se o total chega a zero, encerra o loop
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')  # Mensagem de despedida
