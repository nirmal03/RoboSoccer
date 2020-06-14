# # import cv2

# # import numpy as np
# # cap = cv2.VideoCapture(1)
# # kernel = np.ones((5, 5), np.uint8)
# # while(1):
# #     # Take each frame
# #     _, frame = cap.read()
# #     # Convert BGR to HSV
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# #     # define range of blue color in HSV
# #     lower_blue = np.array([100, 100, 100])
# #     upper_blue = np.array([140, 255, 255])

# #     lower_red = np.array([0, 200, 100])
# #     upper_red = np.array([10, 255, 255])

# #     lower_green = np.array([50, 80, 100])
# #     upper_green = np.array([70, 255, 255])

# #     # Threshold the HSV image to get only blue colors
# #     b1 = cv2.inRange(hsv, lower_blue, upper_blue)
# #     # using dilation and morph open to improve recognition
# #     b2 = cv2.dilate(b1, kernel, iterations=1)
# #     b3 = cv2.morphologyEx(b2, cv2.MORPH_OPEN, kernel)

# #     r1 = cv2.inRange(hsv, lower_red, upper_red)
# #     # using dilation and morph open to improve recognition
# #     r2 = cv2.dilate(r1, kernel, iterations=1)
# #     r3 = cv2.morphologyEx(r2, cv2.MORPH_OPEN, kernel)

# #     g1 = cv2.inRange(hsv, lower_green, upper_green)
# #     # using dilation and morph open to improve recognition
# #     g2 = cv2.dilate(g1, kernel, iterations=1)
# #     g3 = cv2.morphologyEx(g2, cv2.MORPH_OPEN, kernel)

# #     # morph close didn't improve
# #    # mask3 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
# #     # Bitwise-AND mask and original image
# #     red = cv2.bitwise_and(frame, frame, mask=r3)
# #     blue = cv2.bitwise_and(frame, frame, mask=b3)
# #     green = cv2.bitwise_and(frame, frame, mask=g3)
# #     cv2.imshow('frame', frame)
# #     # cv2.imshow('mask',g2)
# #     cv2.imshow('green', green)
# #     cv2.imshow('blue', blue)
# #     cv2.imshow('red', red)
# #     img = np.uint8([[[0, 0, 0]]])
# #     (contours, hierarchy) = cv2.findContours(
# #         b3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #     for pic, contour in enumerate(contours):
# #         area = cv2.contourArea(contour)
# #         if(area > 300):
# #             x, y, w, h = cv2.boundingRect(contour)
# #             img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
# #             cv2.putText(img, "Blue color", (x, y),
# #                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
# #     (contours, hierarchy) = cv2.findContours(
# #         g3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #     for pic, contour in enumerate(contours):
# #         area = cv2.contourArea(contour)
# #         if(area > 300):
# #             x, y, w, h = cv2.boundingRect(contour)
# #             img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
# #             cv2.putText(img, "green color", (x, y),
# #                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
# #     (contours, hierarchy) = cv2.findContours(
# #         r3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #     for pic, contour in enumerate(contours):
# #         area = cv2.contourArea(contour)
# #         if(area > 300):
# #             x, y, w, h = cv2.boundingRect(contour)
# #             img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
# #             cv2.putText(img, "red color", (x, y),
# #                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
# #     cv2.imshow("Color Tracking", img)

# #     k = cv2.waitKey(5) & 0xFF
# #     if k == 27:
# #         break
# # cv2.destroyAllWindows()


# # import the necessary packages
# from collections import deque
# from imutils.video import VideoStream
# import numpy as np
# import argparse
# import cv2
# import imutils
# import time


# greenLower = (29, 86, 6)
# greenUpper = (64, 255, 255)
# # initialize the list of tracked points, the frame counter,
# # and the coordinate deltas
# pts = deque()
# counter = 0
# (dX, dY) = (0, 0)
# direction = ""
# # if a video path was not supplied, grab the reference
# # to the webcam
# # if not args.get("video", False):
# # 	vs = VideoStream(src=0).start()
# # # otherwise, grab a reference to the video file
# # else:
# # 	vs = cv2.VideoCapture(args["video"])
# # allow the camera or video file to warm up
# vs = cv2.VideoCapture(1)
# time.sleep(2.0)
# while True:
#     # grab the current frame
#     frame = vs.read()
#     # handle the frame from VideoCapture or VideoStream
#     # frame = frame[1] if args.get("video", False) else frame
#     # if we are viewing a video and we did not grab a frame,
#     # then we have reached the end of the video
#     if frame is None:
#         break
#     # resize the frame, blur it, and convert it to the HSV
#     # color space
#     # frame = imutils.resize(frame, width=600)
#     blurred = cv2.GaussianBlur(frame, (11, 11), 0)
#     hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
#     # construct a mask for the color "green", then perform
#     # a series of dilations and erosions to remove any small
#     # blobs left in the mask
#     mask = cv2.inRange(hsv, greenLower, greenUpper)
#     mask = cv2.erode(mask, None, iterations=2)
#     mask = cv2.dilate(mask, None, iterations=2)
#     # find contours in the mask and initialize the current
#     # (x, y) center of the ball
#     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
#                             cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     center = None
#     if len(cnts) > 0:
#         # find the largest contour in the mask, then use
#         # it to compute the minimum enclosing circle and
#         # centroid
#         c = max(cnts, key=cv2.contourArea)
#         ((x, y), radius) = cv2.minEnclosingCircle(c)
#         M = cv2.moments(c)
#         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#         # only proceed if the radius meets a minimum size
#         if radius > 10:
#             # draw the circle and centroid on the frame,
#             # then update the list of tracked points
#             cv2.circle(frame, (int(x), int(y)), int(radius),
#                        (0, 255, 255), 2)
#             cv2.circle(frame, center, 5, (0, 0, 255), -1)
#             pts.appendleft(center)
#     for i in np.arange(1, len(pts)):
#         # if either of the tracked points are None, ignore
#         # them
#         if pts[i - 1] is None or pts[i] is None:
#             continue
#         # check to see if enough points have been accumulated in
#         # the buffer
#         if counter >= 10 and i == 1 and pts[-10] is not None:
#             # compute the difference between the x and y
#             # coordinates and re-initialize the direction
#             # text variables
#             dX = pts[-10][0] - pts[i][0]
#             dY = pts[-10][1] - pts[i][1]
#             (dirX, dirY) = ("", "")
#             # ensure there is significant movement in the
#             # x-direction
#             if np.abs(dX) > 20:
#                 dirX = "East" if np.sign(dX) == 1 else "West"
#             # ensure there is significant movement in the
#             # y-direction
#             if np.abs(dY) > 20:
#                 dirY = "North" if np.sign(dY) == 1 else "South"
#             # handle when both directions are non-empty
#             if dirX != "" and dirY != "":
#                 direction = "{}-{}".format(dirY, dirX)
#             # otherwise, only one direction is non-empty
#             else:
#                 direction = dirX if dirX != "" else dirY

#             thickness = int(np.sqrt(32 / float(i + 1)) * 2.5)
#             cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
#     # show the movement deltas and the direction of movement on
#     # the frame
#     cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.65, (0, 0, 255), 3)
#     cv2.putText(frame, "dx: {}, dy: {}".format(dX, dY),
#                 (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.35, (0, 0, 255), 1)
#     # show the frame to our screen and increment the frame counter
#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1) & 0xFF
#     counter += 1
#     # if the 'q' key is pressed, stop the loop
#     if key == ord("q"):
#         break

# vs.release()
# # close all windows
# cv2.destroyAllWindows()


import cv2
import numpy as np

from collections import deque

pts = deque()
cap = cv2.VideoCapture(1)

# Info : ZOOM in the frame to get the RGB value of the corresponding pixel

# The range of color for the object to be detected in HSV
# hsv_supremum = np.array([172, 221, 255])
# hsv_infinum = np.array([150, 40, 130])
# hsv_infinum = np.array([100, 100, 100])
# hsv_supremum = np.array([140, 255, 255])
hsv_infinum = np.array([0, 0, 0])
hsv_supremum = np.array([50, 50, 50])


def operate(frame):
    frame_copy = frame.copy()
    frame_ret = frame.copy()

    # Converting the frame from BGR format to HSV format, Hue Saturation Value GOOGle for more
    frame_copy = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Thresholding the frame to get our object(color) tracked
    mask = cv2.inRange(frame_copy, hsv_infinum, hsv_supremum)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cv2.imshow('mask', mask)

    # Obtaining the binary Image for the corresponding mask
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

    pts.appendleft(center)
    # print(pts[0])

    for i in range(1, len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue
        thickness = 6
        cv2.line(frame_ret, pts[i-1], pts[i], (0, 0, 255), thickness)

    return frame_ret


while True:
    # Let's capture/read the frames for the video
    ret, frame = cap.read()

    if not ret:
        print("cant open camera")
        break

    # This frame captured is flipped, Lets's get the mirror effect
    frame = cv2.flip(frame, 1)

    # Any operations on the frame captured will be processed in the operate(frame) method
    final_frame = operate(frame)

    # Showing the captured frame
    cv2.imshow('garrix', frame)
    cv2.imshow('martin', final_frame)

    # Continuous, Large amount of frames produce a video
    # waitkey(value), value is the ammount of millisecs a frame must be displayed
    # 0xff represents the ASCII value for the key, 27 is for ESC
    # waitKey is necessary to show a frame
    if cv2.waitKey(1) & 0xff == 27:
        break


cap.release()
cv2.destroyAllWindows()
