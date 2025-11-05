def convert_video_to_audio(video_file_path, audio_format='mp3'):
    import os
    import subprocess

    # Define the output audio file path
    base = os.path.splitext(video_file_path)[0]
    audio_file_path = f"{base}.{audio_format}"

    # Command to convert video to audio using ffmpeg
    command = ['ffmpeg', '-i', video_file_path, audio_file_path]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        return audio_file_path
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while converting video to audio: {e}")
        return None