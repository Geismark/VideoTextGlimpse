import re
from src.utils.file_utils import get_output_file_names, convert_video_name_to_image_name
from src.utils.image_utils import save_video_first_frame, get_crops_to_save_info


# get all file names
# get altered file name for image
# save first frame of each video
def save_first_frames(crops=None):
    video_names = get_output_file_names(".webm")
    file_image_names = get_output_file_names(".jpg")
    for video_name in video_names:
        image_name = convert_video_name_to_image_name(video_name)
        crops_to_save_info = get_crops_to_save_info(crops, image_name, file_image_names)
        print(f"2{crops=}\n\t{crops_to_save_info=}\n\t{image_name=}\n\t{video_name=}")
        save_video_first_frame(video_name, image_name, crops_to_save_info)
    return
