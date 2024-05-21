import cv2, os
from src.utils.file_utils import get_output_path


def save_video_first_frame(video_file_name: str, image_name: str, crops_info: list):
    """video_file_name must be found within /output/
    crops is list, with each element being a section of image [image_name, (%w,%w2), (%h,%h2)]
    width & height args MUST be percentage, as video resolution might change
    expect crops to have already been parsed by get_crops_info"""
    output_path = get_output_path()
    video_path = os.path.join(output_path, video_file_name)
    if not os.path.isfile(video_path):
        print(f"Video file does not exist: {video_path}")
        return
    video_obj = cv2.VideoCapture(video_path)
    success, image = video_obj.read()
    if not success:
        print(f"Video was not read successfully: {video_path}")
    height, width, _ = image.shape
    for crop in crops_info:
        image_name, h_rangep, w_rangep = crop
        image_cropped = image[
            int(height * h_rangep[0] / 100) : int(height * h_rangep[1] / 100),
            int(width * w_rangep[0] / 100) : int(width * w_rangep[1] / 100),
        ]
        cv2.imwrite(os.path.join(output_path, image_name), image_cropped)


def get_crops_to_save_info(crops, image_name, file_image_names):
    crops_info = []
    filename, extension = os.path.splitext(image_name)
    if not crops:
        crops = [["", (0, 100), (0, 100)]]
    for crop in crops:
        crop_name, h_rangep, w_rangep = crop
        crop_name_ext = f"{f'-{crop_name}' if crop_name else ''}"
        image_name_crop = f"{filename}{crop_name_ext}{extension}"
        if image_name_crop in file_image_names:
            print(f"Image file already exists: {image_name_crop}")
        else:
            crops_info.append([image_name_crop, h_rangep, w_rangep])
    return crops_info


if __name__ == "__main__":
    save_video_first_frame(
        "youtube-183741-VUxwEfx7OPQ-IT BEGINS... DEEP DIP 2 DISCOVERY - Trackmania's New Hardest Tower.mp4"
    )
