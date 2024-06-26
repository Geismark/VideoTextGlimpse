import yt_dlp, os, pytube


def download_video(url: str, file_name, start_time, duration=0.1, verbose_bool=False):
    '''file_name does NOT include extensions
    start_time is the timestamp to start the download in seconds
    duration is duration of downloaded video, not interval of saved sections (recommend to leave this unchanged)'''
    end_time = start_time + duration
    yt_opts = {
        # using download_ranges or download_sections causes yt-dlp to go through the entire video until getting to the section you are looking for
        # "download_ranges": download_range_func(None, [(start_time, end_time)]),
        # "download_sections": "*0:21:00 - 0:21:05",
        # INSTEAD, using ffmpeg's own options to only request the video from the start time
        # https://stackoverflow.com/a/76560401
        # https://gist.github.com/space-pope/977b0d15cf01932332014194fc80c1f0
        "external_downloader": "ffmpeg",
        "external_downloader_args": {"ffmpeg_i": ["-ss", str(start_time), "-to", str(end_time)]},
        # Issue: rarely (but sometimes) overwrites previously downloaded file with same name
        # actually desired in this case - no auto-deletion yet, but added download timestamp as a fix for now (different name -> always new file)
        "outtmpl": f"{os.path.realpath("output")}/{file_name}.%(ext)s",
        # "format": "bestvideo[ext=mp4]",
        "verbose": verbose_bool,
        "force_keyframes_at_cuts": True,
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydlp:
        ydlp.download(url)
    return

def get_url_duration(url:str):
    yt = pytube.YouTube(url)
    return int(yt.length)

if __name__ == "__main__":
    start_time = 16885
    download_video("https://www.youtube.com/watch?v=VUxwEfx7OPQ", start_time)
    # yt-dlp --list-formats https://www.youtube.com/watch?v=VUxwEfx7OPQ
