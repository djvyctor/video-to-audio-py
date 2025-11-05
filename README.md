# Video to Audio Converter

This project is a simple application that allows users to convert video files into audio files using a graphical user interface (GUI) built with CustomTkinter. The application utilizes FFmpeg for the conversion process.

## Project Structure

```
video-to-audio-py
├── src
│   ├── main.py               # Entry point of the application
│   ├── gui.py                # GUI implementation using CustomTkinter
│   ├── converters
│   │   └── video_to_audio.py # Function to convert video to audio
│   ├── services
│   │   └── ffmpeg_service.py  # Service for FFmpeg interaction
│   ├── utils
│   │   └── file_dialog.py     # Utility for opening file dialogs
│   └── assets
│       └── styles.py          # Styling constants for the GUI
├── tests
│   └── test_conversion.py      # Unit tests for conversion functionality
├── requirements.txt            # Project dependencies
├── pyproject.toml             # Project configuration
├── .gitignore                  # Files to ignore in version control
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd video-to-audio-py
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to select a video file and convert it to audio. The converted audio file will be saved in the same directory as the selected video file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.