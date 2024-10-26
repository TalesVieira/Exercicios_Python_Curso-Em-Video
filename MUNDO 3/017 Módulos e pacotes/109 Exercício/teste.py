# Nome do vídeo: Formatando moedas em python
# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais
# informando se o valor retornado por elas vai ou não ser formatado pela função moeda()

import moeda

# Solicita ao usuário que informe o preço, armazenando o valor na variável 'p'
p = float(input('Digite o preço: R$'))

# Exibe a metade do valor informado, formatada como moeda
# Chama a função metade passando True para formatar o resultado
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')

# Exibe o dobro do valor informado, formatada como moeda
# Corrige a chamada da função dobro para passar True para formatação
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')

# Exibe o valor com um aumento de 10%, formatado como moeda
# Corrige a chamada da função aumentar para passar True para formatação
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')

# Exibe o valor reduzido em 13%, formatado como moeda
# Corrige a chamada da função diminuir para passar True para formatação
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
