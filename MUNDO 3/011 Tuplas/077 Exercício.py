# Nome do vídeo: Contando vogais em tupla
# Crie um programa que tenha uma tupla com várias palavras, depois disso você deve mostrar para cada palavra
# quais são suas vogais, não use acentos

# Tupla com várias palavras que serão analisadas para contar as vogais
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# Loop para percorrer cada palavra na tupla 'palavras'
for p in palavras:
    # Exibe a palavra em maiúsculas (usando o método .upper()) antes de mostrar suas vogais
    print(f'\nNa palavra {p.upper()} temos ', end='')

    # Loop para percorrer cada letra da palavra
    for letra in p:
        # Verifica se a letra é uma vogal, comparando com a string 'aeiou'
        if letra.lower() in 'aeiou':
            # Exibe a vogal encontrada, mantendo na mesma linha (end='' evita a quebra de linha)
            print(letra, end=' ')
