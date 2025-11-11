import os
import shutil
import sys

def _get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    ffmpeg_exe = os.path.join(base_path, 'bin', 'ffmpeg.exe')
    ffprobe_exe = os.path.join(base_path, 'bin', 'ffprobe.exe')
    
    if os.path.exists(ffmpeg_exe) and os.path.exists(ffprobe_exe):
        return os.path.dirname(ffmpeg_exe)
    
    if shutil.which("ffmpeg"):
        return None
    
    raise RuntimeError("ffmpeg não encontrado")

def download_video(video_url, output_path, progress_callback=None):
    try:
        import yt_dlp as ytdl
    except Exception:
        raise RuntimeError("yt-dlp não está instalado")
    
    ffmpeg_location = _get_ffmpeg_path()
    os.makedirs(output_path, exist_ok=True)
    
    def progress_hook(d):
        if progress_callback:
            if d['status'] == 'downloading':
                try:
                    total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                    downloaded = d.get('downloaded_bytes', 0)
                    if total > 0:
                        percent = (downloaded / total) * 100
                        progress_callback(percent)
                except:
                    pass
            elif d['status'] == 'finished':
                progress_callback(100)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': False,
        'noplaylist': True,
        'progress_hooks': [progress_hook],
    }
    
    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location
    
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