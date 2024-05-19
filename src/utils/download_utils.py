from datetime import datetime
import yt_dlp, os
from yt_dlp.utils import download_range_func


def download_video(url: str, start_time=5, end_time=10):
    currenttime = datetime.now()
    timestring = currenttime.strftime("%H%M%S")
    yt_opts = {
        # Issue: RARELY (but sometimes) overwrites previously downloaded file with same name
        # actually desired in this case - no auto-deletion yet, but added download timestamp as a fix for now (different name -> always new file)
        "download_ranges": download_range_func(None, [(start_time, end_time)]),
        "format": "best[ext=mp4]",
        "verbose": True,
        "force_keyframes_at_cuts": True,
        "outtmpl": f"{os.path.realpath("output")}/%(extractor)s-{timestring}-%(id)s-%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydlp:
        ydlp.download(url)
    return


start_time = 2
end_time = 7
download_video("https://www.youtube.com/watch?v=VUxwEfx7OPQ", start_time=1810, end_time=1810.1)
# yt-dlp --list-formats https://www.youtube.com/watch?v=VUxwEfx7OPQ
# print(os.path.realpath("output"))
