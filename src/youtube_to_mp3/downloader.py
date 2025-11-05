import os

def download_video(video_url, output_path):
    try:
        import yt_dlp as ytdl
    except Exception:
        raise RuntimeError("yt-dlp não está instalado. Instale com: pip install yt-dlp")
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        try:
            filename = ydl.prepare_filename(info)
        except Exception:
            filename = os.path.join(output_path, f"{info.get('id')}.{info.get('ext','webm')}")
    audio_path = os.path.splitext(filename)[0] + '.mp3'
    if not os.path.exists(audio_path):
        mp3_files = sorted(
            (os.path.join(output_path, f) for f in os.listdir(output_path) if f.lower().endswith('.mp3')),
            key=os.path.getmtime,
            reverse=True
        )
        if mp3_files:
            audio_path = mp3_files[0]
        else:
            raise RuntimeError("Arquivo mp3 não encontrado após download")
    return os.path.abspath(audio_path)