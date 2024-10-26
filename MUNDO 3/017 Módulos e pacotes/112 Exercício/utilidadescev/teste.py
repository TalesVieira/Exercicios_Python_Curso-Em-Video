# Nome do vídeo: Entrada de dados monetários
# Dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado, crie uma função chamada leiaDinheito
# que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários

from utilidadescev import moeda, dado

p = dado.LeiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)


