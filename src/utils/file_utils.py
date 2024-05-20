import os, pathlib


def get_url_list(file_name: str):
    """'file_name' input is the name of csv file within src/data/"""
    file_path = get_data_file_path(file_name)
    with open(file_path, "r") as url_file:
        contents = url_file.read()
        url_file.close()
    url_list, url_data = url_csv_to_list(contents)
    return url_list, url_data


def get_data_file_path(file_name: str):
    path_actual = os.path.realpath(__file__).split("\\")
    path_actual[-1] = file_name
    path_actual[-2] = "data"
    path_actual = os.path.join(*path_actual)
    return path_actual


def get_output_path():
    output_path = os.path.realpath(__file__).split("\\")[:-3]
    output_path.append("output")
    output_path = os.path.join(*output_path)
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


def get_output_file_names(extension):
    """Current default ffmpeg outputs as .webm"""
    output_path = get_output_path()
    files = [file for file in os.listdir(output_path) if file.endswith(extension)]
    return files


if __name__ == "__main__":
    print(get_url_list("Wirtual_DeepDip.csv"))
    print(get_output_path())
