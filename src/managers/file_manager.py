from src.utils.file_utils import (
    get_data_file_path,
    url_csv_to_list,
    process_url_data,
    remove_files,
    get_output_file_names,
    get_output_path,
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


def delete_old_images():
    old_images = get_output_file_names(".jpg")
    old_image_paths = [
        os.path.join(get_output_path(), image_name) for image_name in old_images
    ]
    fail_count = remove_files(old_image_paths)
    print(f"Found {len(old_images)} images to delete. Had {fail_count} failures")
    return
