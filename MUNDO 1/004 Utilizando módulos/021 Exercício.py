# Nome do vídeo: Tocando um MP3
# Este programa reproduz um arquivo de áudio MP3.

import pygame

# Inicializa o mixer e o módulo de reprodução de áudio
pygame.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('ex01.mp3')

# Inicia a reprodução do áudio
pygame.mixer.music.play()

# Aguarda o evento para que o programa não feche enquanto o áudio é reproduzido
pygame.event.wait()
