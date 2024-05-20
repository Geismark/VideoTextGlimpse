import cv2, os, pytube


def save_video_first_frame(video_file_name: str):
    """video_file_name must be found within /output/"""
    output_path = os.path.realpath("output")
    video_path = os.path.join(output_path, video_file_name)
    if not os.path.isfile(video_path):
        print(f"Video file does not exist: {video_path}")
        return
    video_obj = cv2.VideoCapture(video_path)
    success, image = video_obj.read()
    if success:
        file_name_no_ext = os.path.splitext(os.path.basename(video_path))[0]
        cv2.imwrite(os.path.join(output_path, f"FRAME0-{file_name_no_ext}.jpg"), image)
    else:
        print(f"Video was not read successfully.")
        return


if __name__ == "__main__":
    save_video_first_frame(
        "youtube-183741-VUxwEfx7OPQ-IT BEGINS... DEEP DIP 2 DISCOVERY - Trackmania's New Hardest Tower.mp4"
    )
