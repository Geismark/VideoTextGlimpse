import datetime
from src.utils.file_utils import get_output_file_names
from src.utils.download_utils import download_video, get_url_duration

def download_urls(url_data, save_interval_seconds):
	# check if videos have been downloaded before
	# if not, give file name, timestamps, and url
	# return successful and failed split url_data lists
	currenttime = datetime.datetime.now()
	timestring = currenttime.strftime("%H%M%S")
	old_downloads = get_output_file_names(".webm")
	for data in url_data:
		url_uid, url, start_str, end_str = data
		if start_str:
			start_time = int(start_str)
		else:
			start_time = 0
		if end_str:
			end_time = int(end_str)
		else:
			end_time = -1
		current_timestamp = start_time
		duration = get_url_duration(url)
		if end_time <= 1 or end_time > duration:
			end_time = duration
		if start_time < 0:
			start_time = 0
		elif start_time >= duration:
			start_time = duration - 1
		counter = 0
		while current_timestamp < end_time:
			file_name = f"VIDEO-{counter}-{current_timestamp}-{url.split("?v=")[-1]}"
			download_video(url, file_name, current_timestamp)
			current_timestamp += save_interval_seconds
			counter += 1
			 

	return
