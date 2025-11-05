def get_video_id(url):
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    return None

def validate_url(url):
    """Validates the provided YouTube URL."""
    if "youtube.com" in url or "youtu.be" in url:
        return True
    return False

def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def create_directory(path):
    """Creates a directory if it does not exist."""
    import os
    if not os.path.exists(path):
        os.makedirs(path)