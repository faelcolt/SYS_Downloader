from pytube import Youtube, Playlist
from time import sleep
import os


def pasta_download():
    caminho = f"{os.getenv('USER PROFILE)}\\ Downloads"
    print(caminho)
    
    return caminho

caminho = pasta_download()

def download_unico():
    link = input('Coloque o Link do vídeo do Youtube: ')
    yt = Youtube(link)
    sleep(2)
    tipo = input('Você quer vídeo ou áudio? V ou A: ').lower()
    if tipo == 'v':
        stream = yt.streams.get_by_itag(22)
        print('Fazendo o download...')
        sleep(2)
        stream.download(caminho)
        print('Download concluído...')
        sleep(2)
    
    else:
        stream = yt.streams.get_by_itag(140)
        print('Fazendo download...')
        sleep(2)
        stream.download(caminho)
        print('Download concluído...')
        sleep(2)

def download_playlist():
    playlist = input('Cole o link da PLAYLIST: ')
    sleep(3)
    pl = Playlist(playlist)
    for videos in pl.videos:
        print(f'Baixando: "{video.title}"')
        video.streams.get_by_itag(140).download()
        
print('Bem vindo ao programa!')
print('Ele foi construído para baixar vídeos, músicas ou playlists inteiras do Youtube.')
print(f'Seus downloads ficarão salvos em {caminho}.')


contador = 0

while contador == 0:
    escolha = input('Você quer baixar um vídeo ou uma playlist?: V ou P ').lower()
    
    if escolha == 'v':
        download_unico()
    elif escolha == 'p':
        download_playlist()
    contador += 1
        