import argparse
from youtube_to_mp3.downloader import download_video
from youtube_to_mp3.converter import convert_to_mp3

def main():
    parser = argparse.ArgumentParser(description="youTube to MP3 Converter")
    parser.add_argument("url", help="The URL of the Youtube video to convert")
    parser.add_argument("-o", "--output", help="Output file name (without extension)", default="output")

    args = parser.parse_args()

    print(f"Downloading video from {args.url}...")
    video_file = download_video(args.url)

    print(f"Converting {video_file} to MP3...")
    mp3_file = convert_to_mp3(video_file, args.output)

    print(f"Conversion complete! MP3 file saved as {mp3_file}")

if __name__ == "__main__":
    main()