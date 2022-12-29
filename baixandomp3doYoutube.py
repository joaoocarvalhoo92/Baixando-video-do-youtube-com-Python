from pytube import YouTube
import moviepy.editor as mp
import re
import os

# --Cole o link do video e o local de armazenamento do download
link = input("Cole o link para download aqui : ")
path = input("Cole o local de armazenamento do download : ")
yt = YouTube(link)

# começa o download

print("Baixando...")

ys = yt.streams.filter(only_audio=True).first().download(path)
print("Downloado feito com sucesso !")

#convertendo em mp3
for file in os.listdir(path):
    if re.search('mp4',file):
        mp4_path = os.path.join(path,file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Feito com sucesso !")