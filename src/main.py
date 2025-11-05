from tkinter import Tk
import customtkinter as ctk
from gui import VideoToAudioGUI

def main():
    root = Tk()
    app = VideoToAudioGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()