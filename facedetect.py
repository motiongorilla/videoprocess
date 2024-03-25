import cv2
from pathlib import Path

face_cascade = cv2.CascadeClassifier("../imgtrans/haarcascade_frontalface_default.xml")
red = (0, 255, 0)

# Read video file
video = cv2.VideoCapture("./testingclip.mp4")
# Read webcam
# video = cv2.VideoCapture(0)

frame_exist, frame_data = video.read()

height = frame_data.shape[0]
width = frame_data.shape[1]
codec = cv2.VideoWriter_fourcc(*'DIVX')
fps = video.get(cv2.CAP_PROP_FPS)
output = cv2.VideoWriter("./detected.avi", codec, fps, (width, height))

count = 0
while frame_exist:
    frame = frame_data
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    for (x,y,w,h) in faces:
        start = (x, y)
        end = (x+w, y+h)
        cv2.rectangle(frame, start, end, color=red, thickness=10)

    output.write(frame)
    frame_exist, frame_data = video.read()
    print(count)
    count += 1

output.release()
