# YTDL Python

A Python-based YouTube video downloader that converts videos to MP3 audio files using `yt-dlp` and FFmpeg.

## Features

- 🎵 **Audio Extraction**: Downloads YouTube videos and converts them to MP3 format
- 📝 **Batch Processing**: Processes multiple URLs from a text file
- 🎯 **High Quality**: Downloads best available audio quality
- 🛡️ **Error Handling**: Continues processing even if individual downloads fail
- 📁 **Organized Output**: Files are saved with video titles as filenames

## Prerequisites

### 1. Python 3.13+
This project requires Python 3.13 or higher. You can download it from [python.org](https://www.python.org/downloads/).

### 2. FFmpeg
FFmpeg is required for audio conversion. Follow these steps to install and configure it:

#### Windows Installation:
1. **Download FFmpeg**:
   - Go to [FFmpeg Windows builds](https://github.com/BtbN/FFmpeg-Builds/releases)
   - Download the latest `ffmpeg-master-latest-win64-gpl.zip`

2. **Extract and Setup**:
   - Extract the ZIP file to a permanent location (e.g., `C:\ffmpeg`)
   - Copy the contents of the `bin` folder to `C:\ffmpeg\bin`

3. **Add to System PATH**:
   - Open System Properties (Win + Pause/Break)
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select "Path"
   - Click "Edit" → "New"
   - Add `C:\ffmpeg\bin` (or your chosen path)
   - Click "OK" on all dialogs

4. **Verify Installation**:
   - Open Command Prompt or PowerShell
   - Run: `ffmpeg -version`
   - You should see FFmpeg version information

### 3. UV Package Manager
This project uses [uv](https://github.com/astral-sh/uv) instead of pip for dependency management.

#### Install UV:
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv
```

## Installation

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/xposed73/YTDL-python.git
   cd ytdl
   ```

2. **Create and activate virtual environment**:
   ```bash
   uv venv
   uv sync
   ```

3. **Verify installation**:
   ```bash
   uv run main.py
   ```

## Usage

### 1. Prepare Your URLs
Edit the `urls.txt` file and add YouTube video URLs, one per line:
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
```

### 2. Run the Downloader
```bash
uv run main.py
```

The script will:
- Read URLs from `urls.txt`
- Download each video's audio
- Convert to MP3 format (192kbps quality)
- Save files in the current directory with video titles as filenames

### 3. Customize Settings (Optional)
You can modify the download options in `main.py`:

```python
options = {
    'format': 'bestaudio/best',        # Audio quality
    'outtmpl': '%(title)s.%(ext)s',    # Output filename template
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',       # Output format
        'preferredquality': '192',     # Audio quality (kbps)
    }],
    'quiet': False,                    # Show download progress
    'noplaylist': True,                # Skip playlists
}
```

## Project Structure

```
ytdl/
├── main.py           # Main download script
├── urls.txt          # List of YouTube URLs to download
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
├── README.md        # This file
└── .venv/           # Virtual environment (created by uv)
```

## Dependencies

- **yt-dlp**: YouTube video downloader (fork of youtube-dl)
- **FFmpeg**: Audio/video processing (external dependency)

## Troubleshooting

### Common Issues

1. **"FFmpeg not found" error**:
   - Ensure FFmpeg is installed and added to PATH
   - Restart your terminal after adding to PATH
   - Verify with `ffmpeg -version`

2. **"File not found: urls.txt"**:
   - Make sure `urls.txt` exists in the project directory
   - Check file permissions

3. **Download failures**:
   - Some videos may be restricted or unavailable
   - Check your internet connection
   - Verify YouTube URLs are valid

4. **UV installation issues**:
   - Try installing via pip: `pip install uv`
   - Or download from [uv releases](https://github.com/astral-sh/uv/releases)

### Getting Help

If you encounter issues:
1. Check that all prerequisites are properly installed
2. Verify FFmpeg is in your system PATH
3. Ensure you're using Python 3.13+
4. Check the error messages for specific details

## License

This project is open source. Feel free to modify and distribute.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
