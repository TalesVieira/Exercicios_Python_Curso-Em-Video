# Nome do vídeo: Índice de massa corporal
# Este programa calcula o Índice de Massa Corporal (IMC) de uma pessoa e determina sua faixa de peso.

# Lê o peso e a altura da pessoa
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

# Calcula o IMC utilizando a fórmula
imc = peso / (altura ** 2)

# Exibe o valor do IMC com uma casa decimal
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

# Verifica em qual faixa de peso o IMC se enquadra e exibe o status correspondente
if imc < 18.5:
    # Abaixo do peso
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    # Peso ideal
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    # Sobrepeso
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    # Obesidade
    print('Você está em OBESIDADE!')
else:
    # Obesidade mórbida
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
