import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from youtube_to_mp3.gui import App

App().mainloop()