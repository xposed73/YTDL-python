import yt_dlp

def app(file_path):
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            print(f"Downloading: {url}")
            try:
                ydl.download([url])
            except Exception as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    app('urls.txt')
