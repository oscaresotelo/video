# from moviepy.editor import VideoFileClip

# filename = "lakonga.mp4"
# clip = VideoFileClip(filename)
# clip.audio.write_audiofile(filename[:-4] + ".mp3")
# clip.close()
from pytube import YouTube
import os

yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

audio = yt.streams.filter(only_audio = True).first()

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

base, ext = os.path.splitext("musica")
new_file = base + '.mp3'
os.rename("musica", new_file)
print(yt.title + " has been successfully downloaded in .mp3 format.")
