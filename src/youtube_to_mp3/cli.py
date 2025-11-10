import argparse
from youtube_to_mp3.downloader import download_video
import os

def main():
    parser = argparse.ArgumentParser(description="YouTube to MP3")
    parser.add_argument("url", help="URL do vídeo")
    parser.add_argument("-d", "--dir", help="Pasta de saída", default=os.path.join(os.path.expanduser("~"), "Downloads"))
    args = parser.parse_args()
    print("Baixando e convertendo...")
    mp3_path = download_video(args.url, args.dir)
    print(f"Concluído: {mp3_path}")

if __name__ == "__main__":
    main()