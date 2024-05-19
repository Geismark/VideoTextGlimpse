from src.utils.file_utils import get_url_list


def main(csv_file_name):
    urls = get_url_list(csv_file_name)
    return urls


if __name__ == "__main__":
    print(main("Wirtual_DeepDip.csv"))
