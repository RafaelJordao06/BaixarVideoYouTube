from pytube import YouTube
link = input('Entre com o link: ')
yt = YouTube(link)

#Obtendo a maior resolução possível
ys = yt.streams.get_highest_resolution()
print("Baixando.....")
ys.download()
print('Baixado com sucesso! :)')