from src.utils.file_utils import get_url_list


def main(csv_file_name):
    url_list, url_data = get_url_list(csv_file_name)
    return url_list


if __name__ == "__main__":
    print(main("Wirtual_DeepDip.csv"))
