import cv2
import numpy as np
from collections import deque

# frame=[]


cap = None


# modify to get video over server-client connection
def init():
    global cap
    cap = cv2.VideoCapture(1)


def getFrame():

    global cap
    ret, frame = cap.read()

    if not ret:
        print("cant open camera")
        return None
    else:
        return frame


def end():
    global cap
    cap.release()
    cv2.destroyAllWindows()


def findByColor(hsv_low, hsv_high):
    hsv_infinum = np.array(hsv_low)

    hsv_supremum = np.array(hsv_high)

    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()

    if not ret:
        print("cant open camera")
        return None

    frame_copy = frame.copy()
    frame_ret = frame.copy()

    # Converting the frame from BGR format to HSV format, Hue Saturation Value GOOGle for more
    frame_copy = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Thresholding the frame to get our object(color) tracked
    mask = cv2.inRange(frame_copy, hsv_infinum, hsv_supremum)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cap.release()
