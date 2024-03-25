import cv2
import matplotlib.pyplot as plt

camin = input("webcam in: ")
stream = cv2.VideoCapture(int(camin))

while True:
    stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    ret,frame = stream.read()
    if not ret:
        print("Can't read frame")
        break
    cv2.imshow('webcam', frame)
    # plt.imshow(frame)
    # plt.show()
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
