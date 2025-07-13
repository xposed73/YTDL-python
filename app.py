import yt_dlp
import os

def app(file_path):
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    # Create downloads directory if it doesn't exist
    downloads_dir = "downloads"
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
        print(f"Created downloads directory: {downloads_dir}")

    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),  # Save in downloads folder
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True,
    }

    print(f"Current working directory: {os.getcwd()}")
    print(f"Files will be saved to: {os.path.abspath(downloads_dir)}")
    
    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            print(f"Downloading: {url}")
            try:
                ydl.download([url])
                print(f"Download completed for: {url}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")
    
    # List all files in downloads directory after download
    print(f"\nFiles in {downloads_dir} directory after download:")
    if os.path.exists(downloads_dir):
        for file in os.listdir(downloads_dir):
            if file.endswith('.mp3') or file.endswith('.webm') or file.endswith('.m4a'):
                print(f"  {file}")
    else:
        print(f"  {downloads_dir} directory not found")

if __name__ == "__main__":
    app('urls.txt')
