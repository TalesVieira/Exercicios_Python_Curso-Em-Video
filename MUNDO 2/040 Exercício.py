# Nome do vídeo: Aquele clássico de média
# Este programa lê duas notas de um aluno, calcula a média e exibe uma mensagem final:
# - REPROVADO, se a média for abaixo de 5.0.
# - RECUPERAÇÃO, se a média for entre 5.0 e 6.9.
# - APROVADO, se a média for 7.0 ou superior.

# Lê as notas do aluno
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

# Calcula a média das notas
media = (n1 + n2) / 2

# Verifica a situação do aluno com base na média e exibe a mensagem correspondente
if media < 5:
    # Se a média for menor que 5, o aluno está reprovado
    print('A média do aluno foi {:.1f}, e ele está REPROVADO!'.format(media))
elif 5 <= media <= 6.9:
    # Se a média estiver entre 5 e 6.9, o aluno está em recuperação
    print('A média do aluno foi {:.1f}, ele está na RECUPERAÇÃO!'.format(media))
else:
    # Se a média for 7 ou superior, o aluno está aprovado
    print('A média do aluno foi {:.1f}, e ele está APROVADO!'.format(media))
