# Importa o módulo moeda, que contém as funções de manipulação e formatação de valores monetários
import moeda

# Solicita ao usuário que informe o preço, armazenando o valor na variável 'p'
p = float(input('Digite o preço: R$'))

# Exibe a metade do valor informado, formatada como moeda
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')

# Exibe o dobro do valor informado, formatada como moeda
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')

# Exibe o valor com um aumento de 10%, formatado como moeda
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
