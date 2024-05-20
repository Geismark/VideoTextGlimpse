import cv2, os
from src.utils.file_utils import get_output_path


def save_video_first_frame(video_file_name: str, image_name: str):
    """video_file_name must be found within /output/"""
    output_path = get_output_path()
    video_path = os.path.join(output_path, video_file_name)
    if not os.path.isfile(video_path):
        print(f"Video file does not exist: {video_path}")
        return
    video_obj = cv2.VideoCapture(video_path)
    success, image = video_obj.read()
    if success:
        cv2.imwrite(os.path.join(output_path, image_name), image)
    else:
        print(f"Video was not read successfully.")
        return


if __name__ == "__main__":
    save_video_first_frame(
        "youtube-183741-VUxwEfx7OPQ-IT BEGINS... DEEP DIP 2 DISCOVERY - Trackmania's New Hardest Tower.mp4"
    )
