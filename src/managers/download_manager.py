from src.utils.file_utils import get_output_file_names
from src.utils.download_utils import download_video, get_url_duration

def download_urls(url_data, save_interval_seconds):
	old_downloads = get_output_file_names(".webm")
	for data in url_data:
		uid, url, start_time, end_time = data
		current_timestamp = start_time
		counter = 0
		while current_timestamp < end_time:
			file_name = f"{uid}VIDEO-{counter}-{current_timestamp}-{url.split("?v=")[-1]}"
			if "".join([file_name, ".webm"]) in old_downloads:
				print("Video download already exists: " + file_name)
			else:
				download_video(url, file_name, current_timestamp)
			current_timestamp += save_interval_seconds
			counter += 1
	return
