from datetime import datetime
import yt_dlp, os, pytube


def download_video(url: str, start_time, duration=0.5):
    currenttime = datetime.now()
    timestring = currenttime.strftime("%H%M%S")
    end_time = start_time + duration
    yt_opts = {
        # using the built in download_range_func causes yt-dlp to go through the entire video until getting to the section you are looking for
        # "download_ranges": download_range_func(None, [(start_time, end_time)]),
        # INSTEAD, using ffmpeg's own options to only request the video from the start time
        # https://stackoverflow.com/a/76560401
        "external_downloader": "ffmpeg",
        "external_downloader_args": {"ffmpeg_i": ["-ss", str(start_time), "-to", str(end_time)]},
        # Issue: rarely (but sometimes) overwrites previously downloaded file with same name
        # actually desired in this case - no auto-deletion yet, but added download timestamp as a fix for now (different name -> always new file)
        "outtmpl": f"{os.path.realpath("output")}/%(extractor)s-{timestring}-%(id)s-%(title)s.%(ext)s",
        # "format": "bestvideo[ext=mp4]",
        "verbose": True,
        "force_keyframes_at_cuts": True,
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydlp:
        ydlp.download(url)
    return

def get_url_duration(url:str):
    yt = pytube.Youtube(url)
    return yt.length

if __name__ == "__main__":
    start_time = 180000
    download_video("https://www.youtube.com/watch?v=VUxwEfx7OPQ", start_time)
    # yt-dlp --list-formats https://www.youtube.com/watch?v=VUxwEfx7OPQ
