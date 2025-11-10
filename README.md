# YouTube to MP3

Aplicação simples em Python que baixa o áudio de vídeos do YouTube e salva em formato MP3 usando yt-dlp e ffmpeg.

## Funcionalidades
- Inserir URL do vídeo e gerar MP3
- Escolher pasta de saída
- Versão CLI e GUI (Tkinter)

## Requisitos
- Python 3.10+
- ffmpeg instalado e no PATH
- pip install -r requirements.txt

## Uso GUI
python main.py

## Uso CLI
python -m youtube_to_mp3.cli "URL_DO_VIDEO" -d "C:\Destino"

## Build .exe (exemplo)
pyinstaller --onefile --noconsole -n YouTubeToMP3 main.py