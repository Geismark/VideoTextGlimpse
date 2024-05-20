from src.managers.file_manager import get_url_list
from src.managers.download_manager import download_urls
from src.managers.image_manager import save_first_frames

DOWNLOAD_INTERVAL_SECONDS = 600


def main(csv_file_name, download_videos=True, convert_to_images=True):
    _, url_data = get_url_list(csv_file_name)
    if download_videos:
        download_urls(url_data, DOWNLOAD_INTERVAL_SECONDS)
    if convert_to_images:
        save_first_frames()


if __name__ == "__main__":
    print(main("Wirtual_DeepDip.csv"))
