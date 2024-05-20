import re
from src.utils.file_utils import get_output_file_names, convert_video_name_to_image_name
from src.utils.image_utils import save_video_first_frame


# get all file names
# get altered file name for image
# save first frame of each video
def save_first_frames():
    video_names = get_output_file_names(".webm")
    image_names = get_output_file_names(".jpg")
    for video_name in video_names:
        image_name = convert_video_name_to_image_name(video_name)
        if image_name in image_names:
            print("Frame image already exists")
        else:
            save_video_first_frame(video_name)
    return
