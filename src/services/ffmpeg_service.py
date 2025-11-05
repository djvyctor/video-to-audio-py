class FFmpegService:
    def __init__(self, ffmpeg_path='ffmpeg'):
        self.ffmpeg_path = ffmpeg_path

    def convert(self, input_file, output_file):
        import subprocess

        command = [self.ffmpeg_path, '-i', input_file, output_file]
        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")
            return False