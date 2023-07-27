from pytube import YouTube

url1 = "https://youtu.be/3KdlW1Rf9cE"
url="https://youtu.be/svj-Z0CYTHI"

yt=YouTube(url)
yt1 = YouTube(url1)

# Show video title and thumbnail URL
print(yt.title)
print(yt.thumbnail_url)

#for video
yt=yt.streams.get_lowest_resolution()
yt.download()

#For audio
audio= yt1.streams.filter(only_audio=True)
aud=list(enumerate(audio))
for i in aud:
    print(i)
print()
strm=int(input("Enter : "))
audio[strm].download()
print("Successfully downloaded both audio and video")

