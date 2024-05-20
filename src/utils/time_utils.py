def seconds_to_hour_time(seconds: int):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return hrs, mins, secs


if __name__ == "__main__":
    print(seconds_to_hour_time(26468))
