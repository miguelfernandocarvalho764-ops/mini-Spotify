import pygame
from tkinter import *

# =========================
# INICIALIZA O PYGAME
# =========================

pygame.init()
pygame.mixer.init()

# =========================
# PLAYLIST
# =========================

playlist = [
    'audios_mp3/musica1.mp3',
    'audios_mp3/musica2.mp3'
]

# CONTROLA A MÚSICA ATUAL
indice = 0

# =========================
# FUNÇÃO PLAY
# =========================

def tocar_musica():

    global indice

    musica = playlist[indice]

    display_musica.config(text=f'Tocando: {musica}')

    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    

# =========================
# FUNÇÃO PAUSE
# =========================

def pausar_musica():

    pygame.mixer.music.pause()

# =========================
# FUNÇÃO CONTINUE
# =========================

def continuar_musica():

    pygame.mixer.music.unpause()

# =========================
# FUNÇÃO NEXT
# =========================

def proxima_musica():

    global indice

    indice += 1

    # VOLTA PARA PRIMEIRA
    if indice >= len(playlist):
        indice = 0

    tocar_musica()

# =========================
# FUNÇÃO BACK
# =========================

def voltar_musica():

    global indice

    indice -= 1

    # VOLTA PARA ÚLTIMA
    if indice < 0:
        indice = len(playlist) - 1

    tocar_musica()

# =========================
# FUNÇÃO VOLUME
# =========================

def alterar_volume(valor):

    volume = int(valor) / 100

    pygame.mixer.music.set_volume(volume)

# =========================
# CRIA JANELA
# =========================

janela = Tk()

janela.title('Meu Player MP3')

# AUMENTEI A JANELA
janela.geometry('400x350')

# =========================
# CRIAR DISPLAY
# =========================

display_musica = Label(
    janela,
    text='Nenhuma música tocando',
    font=('Arial', 14)
)

display_musica.pack(pady=20)

# =========================
# BOTÃO PLAY
# =========================

botao_play = Button(
    janela,
    text='PLAY',
    width=8,
    command=tocar_musica
)

botao_play.pack(side=LEFT, padx=8)

# =========================
# BOTÃO PAUSE
# =========================

botao_pause = Button(
    janela,
    text='PAUSE',
    width=8,
    command=pausar_musica
)

botao_pause.pack(side=LEFT, padx=8)

# =========================
# BOTÃO CONTINUE
# =========================

botao_continue = Button(
    janela,
    text='CONTINUE',
    width=8,
    command=continuar_musica
)

botao_continue.pack(side=LEFT, padx=8)

# =========================
# BOTÃO NEXT
# =========================

botao_next = Button(
    janela,
    text='NEXT',
    width=8,
    command=proxima_musica
)

botao_next.pack(side=LEFT, padx=8)

# =========================
# BOTÃO BACK
# =========================

botao_back = Button(
    janela,
    text='BACK',
    width=8,
    command=voltar_musica
)

botao_back.pack(side=LEFT, padx=8)

# =========================
# TEXTO VOLUME
# =========================

texto_volume = Label(
    janela,
    text='VOLUME'
)

texto_volume.pack(pady=5)

# =========================
# BARRA DE VOLUME
# =========================

controle_volume = Scale(
    janela,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    length=250,
    command=alterar_volume
)

controle_volume.pack(pady=10)

# COMEÇA COM VOLUME MÁXIMO
controle_volume.set(100)



# =========================
# MAINLOOP
# =========================

janela.mainloop()