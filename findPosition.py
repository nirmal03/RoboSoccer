
"""
Assume video capture always working
and getPosition function work on frame
"""
import cv2
import numpy as np
from capture import init, getFrame, end


ball_hsv_infinum = np.array([100, 100, 100])
ball_hsv_supremum = np.array([140, 255, 255])
goal_hsv_infinum = np.array([0, 0, 0])
goal_hsv_supremum = np.array([10, 10, 10])


def getBallPosition():
    global ball_hsv_infinum, ball_hsv_supremum
    frame = getFrame()
    frame_copy = frame.copy()
    frame_ret = frame.copy()
    frame_copy = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    x = -1
    y = -1
    # Thresholding the frame to get our object(color) tracked
    mask = cv2.inRange(frame_copy, ball_hsv_infinum, ball_hsv_supremum)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    res = cv2.bitwise_and(frame_ret, frame_ret, mask=mask)

    #cv2.imshow('res', res)
    # The result can be improved by smoothening the frame

    mask_copy = mask.copy()
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame_ret, (int(x), int(y)),
                       int(radius), (0, 150, 255), 2)
            cv2.circle(frame_ret, center, 5, (0, 0, 255), -1)

    return (x, y)


def getGoalPosition():
    global goal_hsv_infinum, goal_hsv_supremum
    frame = getFrame()
    frame_copy = frame.copy()
    frame_ret = frame.copy()
    frame_copy = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    x = -1
    y = -1
    # Thresholding the frame to get our object(color) tracked
    mask = cv2.inRange(frame_copy, goal_hsv_infinum, goal_hsv_supremum)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    res = cv2.bitwise_and(frame_ret, frame_ret, mask=mask)

    #cv2.imshow('res', res)
    # The result can be improved by smoothening the frame

    mask_copy = mask.copy()
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame_ret, (int(x), int(y)),
                       int(radius), (0, 150, 255), 2)
            cv2.circle(frame_ret, center, 5, (0, 0, 255), -1)

    cv2.imshow("frame", frame_ret)
    while(True):
        if cv2.waitKey(1) & 0xff == 27:
            break

    return (x, y)


# modify to implement trignometry
def getAngle(obj):
    x, y = obj
    if(x == -1 or y == -1):
        return None

# modify to use focal length


def getDistance(obj):
    if(x == -1 or y == -1):
        return None
    return y


# init()
# frame = getFrame()
# cv2.imshow("frame", frame)
# while(True):
#     if cv2.waitKey(1) & 0xff == 27:
#         break
# end()


init()
x, y = getBallPosition()
end()
# if(x==None or)
print(x, y)
