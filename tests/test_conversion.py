import unittest
from src.converters.video_to_audio import convert_video_to_audio

class TestVideoToAudioConversion(unittest.TestCase):

    def test_conversion_valid_file(self):
        video_file = "path/to/valid/video.mp4"
        audio_file = convert_video_to_audio(video_file)
        self.assertTrue(audio_file.endswith('.mp3'))  # Assuming the output format is mp3

    def test_conversion_invalid_file(self):
        video_file = "path/to/invalid/video.mp4"
        with self.assertRaises(FileNotFoundError):
            convert_video_to_audio(video_file)

    def test_conversion_empty_file(self):
        video_file = ""
        with self.assertRaises(ValueError):
            convert_video_to_audio(video_file)

if __name__ == '__main__':
    unittest.main()