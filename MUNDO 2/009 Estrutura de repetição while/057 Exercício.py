# Nome do vídeo: Validação de dados
# Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peça a digitação novamente até ter um valor correto

# Solicita a entrada inicial para o sexo, e armazena apenas o primeiro caractere, removendo espaços e convertendo para maiúsculo
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

# Enquanto o valor informado não for 'M' ou 'F', continua pedindo uma nova entrada
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

# Confirmação final do sexo registrado
print('Sexo {} registrado com sucesso.'.format(sexo))
