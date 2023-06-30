from pytube import Playlist

p = Playlist("https://www.youtube.com/watch?v=Mroued07Z2U&list=PLAp5x8qTe85kpe81ZISZMNpQ511I2O6xg")
print(p.title)
for video in p.videos:
	audio = video.streams.filter(only_audio=True, abr="160kbps").first()
	audio.download(output_path="./musica")
