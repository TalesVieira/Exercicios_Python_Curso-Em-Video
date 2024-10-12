# Nome do vídeo: Gerenciador de pagamentos
# Este programa calcula o valor a ser pago por um produto, considerando o preço normal e a condição de pagamento.

print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$ '))

# Exibe as opções de pagamento
print(''' FORMAS DE PAGAMENTO 
      [ 1 ] À vista dinheiro/cheque
      [ 2 ] À vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

# Calcula o total com base na opção escolhida
if opção == 1:
    # À vista dinheiro/cheque: 10% de desconto
    total = preço - (preço * 10 / 100)
elif opção == 2:
    # À vista no cartão: 5% de desconto
    total = preço - (preço * 5 / 100)
elif opção == 3:
    # Em até 2x no cartão: preço normal
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    # 3x ou mais no cartão: 20% de juros
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    # Opção inválida
    print('Opção inválida de pagamento, tente novamente.')
    total = preço  # Define total como o preço original, caso a opção seja inválida

# Exibe o valor final da compra
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
