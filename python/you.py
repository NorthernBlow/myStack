import yt_dlp as youtube_dl

def download_video(url):
    ydl_opts={}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url='https://youtu.be/LAvaaQO2L_o?si=8Fqz_OlOZdmR-3Nl'

download_video(video_url)
