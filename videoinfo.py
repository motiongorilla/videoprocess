import cv2

video = cv2.VideoCapture("./testingclip.mp4")

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)
framenum = video.get(cv2.CAP_PROP_FRAME_COUNT)

bitrate = video.get(cv2.CAP_PROP_BITRATE)
duration = framenum/fps

print(f'''
      Width: {width}
      Height: {height}
      Frames per second: {fps}
      Duration: {duration}
      Bitrate: {bitrate}''')
