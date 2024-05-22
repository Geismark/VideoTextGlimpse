import os, re
from src.utils.download_utils import get_url_duration
from src.data.crops_dict import crops_dict


def process_url_data(url_data):
    processed_data = []
    for data in url_data:
        uid, url, start, end = data
        duration = get_url_duration(url)
        if (
            not start
            or not start.isnumeric()
            or int(start) < 0
            or int(start) > duration - 1
        ):
            start = 0
        else:
            start = int(start)
        if not end or not end.isnumeric() or int(end) < 1 or int(end) > duration:
            end = duration
        else:
            end = int(end)
        if (end - start) < 0.5:
            end = int(end) + 0.5
        uid = int(uid)
        start = int(start)
        end = int(end)
        processed_data.extend([[uid, url, start, end]])
    return processed_data


def get_data_file_path(file_name: str):
    path_actual = os.path.realpath(__file__).split("\\")
    path_actual[-1] = file_name
    path_actual[-2] = "data"
    path_actual = "\\".join(path_actual)
    return path_actual


def get_output_path():
    output_path = os.path.realpath(__file__).split("\\")[:-3]
    output_path.append("output")
    output_path = "\\".join(output_path)
    return output_path


def url_csv_to_list(contents: str):
    lines = contents.split("\n")
    url_list = []
    url_data = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        line = line.split(",")
        url_data.append(line)
        url_list.append(line[1])
    return url_list, url_data


def convert_video_name_to_image_name(video_name: str):
    regex_video = re.compile(r"(?<=\d)VIDEO")
    video_name_split = regex_video.split(video_name)
    video_name_split.insert(1, "FRAME")
    image_name_wrong_ext = "".join(video_name_split)
    image_name = re.sub(".webm", ".jpg", image_name_wrong_ext)
    return image_name


def get_output_file_names(extension):
    """Current default ffmpeg outputs as .webm"""
    output_path = get_output_path()
    files = [file for file in os.listdir(output_path) if file.endswith(extension)]
    return files


def remove_files(file_paths: list):
    fail_count = 0
    for file in file_paths:
        if not os.path.isfile(file):
            print(f"Trying to remove file that doesn't exist: {file}")
            fail_count += 1
            continue
        os.remove(file)
    return fail_count


def get_crop_from_dict(csv_file_name):
    crops = crops_dict.get(csv_file_name)
    if not crops:
        crops = []
    return crops
