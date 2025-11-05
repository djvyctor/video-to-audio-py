import os
import shutil
from pydub import AudioSegment

def is_ffmpeg_available():
    return shutil.which("ffmpeg")

def _ensure_output_dir(path):
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)

def convert_to_mp3(input_path, output_path, bitrate="192k"):
    if not os.path.exists(input_path):
        raise FileNotFoundError(input_path)
    ffmpeg_path = is_ffmpeg_available()
    if not ffmpeg_path:
        raise RuntimeError("ffmpeg não encontrado no PATH")
    AudioSegment.converter = ffmpeg_path
    audio = AudioSegment.from_file(input_path)
    _ensure_output_dir(output_path)
    audio.export(output_path, format="mp3", bitrate=bitrate)
    return os.path.abspath(output_path)

def convert_video_to_mp3(video_file_path, output_directory, bitrate="192k"):
    if not os.path.exists(video_file_path):
        raise FileNotFoundError(video_file_path)
    os.makedirs(output_directory, exist_ok=True)
    base = os.path.splitext(os.path.basename(video_file_path))[0]
    mp3_file_path = os.path.join(output_directory, f"{base}.mp3")
    return convert_to_mp3(video_file_path, mp3_file_path, bitrate=bitrate)

def convert_multiple_videos(video_file_paths, output_directory, bitrate="192k"):
    os.makedirs(output_directory, exist_ok=True)
    converted_files = []
    for video_file_path in video_file_paths:
        converted_file = convert_video_to_mp3(video_file_path, output_directory, bitrate=bitrate)
        converted_files.append(converted_file)
    return converted_files