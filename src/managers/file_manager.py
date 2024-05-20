from src.utils.file_utils import (
    get_data_file_path,
    url_csv_to_list,
    process_url_data,
)
import os


def get_url_list(file_name: str):
    """'file_name' input is the name of csv file within src/data/"""
    file_path = get_data_file_path(file_name)
    with open(file_path, "r") as url_file:
        contents = url_file.read()
        url_file.close()
    url_list, url_data = url_csv_to_list(contents)
    url_data = process_url_data(url_data)
    return url_list, url_data
