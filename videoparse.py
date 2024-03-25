import cv2
from datetime import datetime

source = "./testingclip.mp4"
video = cv2.VideoCapture(source)

timecode = input("Enter timestamp (HH:MM:SS.ms): ")
# timecode = "00:00:01.88"
t_timestamp = datetime.strptime(timecode, "%H:%M:%S.%f")

success, frame = video.read()

"""Save all frames from video into images"""
# counter = 1
# while success:
#     cv2.imwrite(f"./images/{counter}.jpg", frame)
#     success, frame = video.read()
#     counter += 1

"""Save frame from timecode"""
fps = video.get(cv2.CAP_PROP_FPS)
t_minutes = t_timestamp.hour*60 + t_timestamp.minute
t_seconds = (t_minutes * 60) + t_timestamp.second + (t_timestamp.microsecond/1000000)
selected_frame = int(fps*t_seconds)
video.set(cv2.CAP_PROP_POS_FRAMES, selected_frame)
success, frame = video.read()
if success:
    cv2.imwrite(f"./images/{selected_frame}_captured.jpg", frame)

