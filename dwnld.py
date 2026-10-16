import yt_dlp


def dwnld_video(master_url, output_path):
    options = {
        "outtmpl": str(output_path) + ".%(ext)s",

        "retries": 10,
        "fragment_retries": 30,

        "socket_timeout": 60,

        "continuedl": True,

        "nopart": False,

        "skip_unavailable_fragments": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([master_url])


