import os.path


def get_url_list(file_name: str):
    """'file_name' input is the name of csv file within src/data/"""
    file_path = get_data_file_path(file_name)
    with open(file_path, "r") as url_file:
        contents = url_file.read()
        url_file.close()
    url_list = url_csv_to_list(contents)
    return url_list


def get_data_file_path(file_name: str):
    path_actual = os.path.realpath(__file__)
    path_actual = path_actual.split("\\")
    path_actual[-1] = file_name
    path_actual[-2] = "data"
    path_actual = "\\".join(path_actual)
    return path_actual


def url_csv_to_list(contents: str):
    lines = contents.split("\n")
    url_list = []
    url_data = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        line = line.split(",", 1)
        url_data.append(line)
        url_list.append(line[1])
    return url_list, url_data


if __name__ == "__main__":
    print(get_url_list("Wirtual_DeepDip.csv"))
