# Nome do vídeo: Pintando Parede
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

# Lê a largura e a altura da parede
larg = float(input('Largura da parede (em metros): '))
alt = float(input('Altura da parede (em metros): '))

# Calcula a área da parede
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(larg, alt, área))

# Calcula a quantidade de tinta necessária
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
