from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry
import tkinter as tk
from utils.file_dialog import open_file_dialog
from converters.video_to_audio import convert_video_to_audio

class VideoToAudioApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Video to Audio Converter")
        self.geometry("400x300")

        self.video_path = ""

        self.label = CTkLabel(self, text="Select a video file:")
        self.label.pack(pady=20)

        self.entry = CTkEntry(self, width=300)
        self.entry.pack(pady=10)

        self.browse_button = CTkButton(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.convert_button = CTkButton(self, text="Convert to Audio", command=self.convert_audio)
        self.convert_button.pack(pady=20)

    def browse_file(self):
        self.video_path = open_file_dialog()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.video_path)

    def convert_audio(self):
        if self.video_path:
            convert_video_to_audio(self.video_path)
            self.label.configure(text="Conversion completed!")
        else:
            self.label.configure(text="Please select a video file.")

if __name__ == "__main__":
    app = VideoToAudioApp()
    app.mainloop()