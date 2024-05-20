def seconds_to_hour_time(seconds: int):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return hrs, mins, secs


def hour_time_to_seconds(hr: int, min: int, sec: int):
    seconds = (hr * 60 * 60) + (min * 60) + sec
    return seconds


if __name__ == "__main__":
    print(seconds_to_hour_time(26468))
