import os
import yt_dlp

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_youtube_video(url: str, quality: str = "best") -> str:
    """
    Download a YouTube video with audio in the selected quality.

    Supported qualities:
    - best
    - 1080p
    - 720p
    - 480p
    - 360p
    """

    output_path = os.path.join(
        DOWNLOAD_DIR,
        "%(title)s.%(ext)s"
    )

    # Select video quality
    if quality == "1080p":
        format_selector = (
            "bestvideo[height<=1080]+bestaudio/"
            "best[height<=1080]"
        )

    elif quality == "720p":
        format_selector = (
            "bestvideo[height<=720]+bestaudio/"
            "best[height<=720]"
        )

    elif quality == "480p":
        format_selector = (
            "bestvideo[height<=480]+bestaudio/"
            "best[height<=480]"
        )

    elif quality == "360p":
        format_selector = (
            "bestvideo[height<=360]+bestaudio/"
            "best[height<=360]"
        )

    else:
        format_selector = "bestvideo+bestaudio/best"

    ydl_opts = {
        "format": format_selector,

        "outtmpl": output_path,

        # Merge video and audio into MP4
        "merge_output_format": "mp4",

        # Don't download playlists
        "noplaylist": True,

        # Show progress in terminal
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            # Get downloaded filename
            filename = ydl.prepare_filename(info)

            # After merging, extension becomes .mp4
            filename = os.path.splitext(filename)[0] + ".mp4"

        return filename

    except Exception as e:
        raise Exception(f"Video download failed: {str(e)}")