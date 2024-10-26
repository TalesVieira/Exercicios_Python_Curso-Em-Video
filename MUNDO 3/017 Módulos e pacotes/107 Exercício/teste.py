# Nome do vídeo: Exercitando módulos em python.
# Crie um módulo chamado moeda que tenha as funções incorporadas aumentar(), diminuir(), dorbro() e metade()
# Faça tambem um programa que importe esse módulo e use algumas dessas funções

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
   