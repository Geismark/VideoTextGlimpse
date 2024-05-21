from src.managers.file_manager import get_url_list, delete_old_images
from src.managers.download_manager import download_urls
from src.managers.image_manager import save_first_frames

DOWNLOAD_INTERVAL_SECONDS = 60


def main(
    csv_file_name,
    download_videos=True,
    convert_to_images=True,
    delete_old_images_bool=True,
):
    _, url_data = get_url_list(csv_file_name)
    if download_videos:
        download_urls(url_data, DOWNLOAD_INTERVAL_SECONDS)
    if delete_old_images_bool:
        delete_old_images()
    if convert_to_images:
        if csv_file_name == "Wirtual_DeepDip.csv":
            # crops = ["name of the crop", (ymin, ymax), (xmin, xmax)]
            crops = [["Falls", (50, 56), (85, 100)], ["Time", (37, 48), (75, 100)]]
        else:
            crops = []
        save_first_frames(crops)


if __name__ == "__main__":
    print(main("Wirtual_DeepDip.csv"))
