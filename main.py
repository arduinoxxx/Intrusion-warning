import cv2
import numpy as np
from imutils.video import VideoStream
import torch
from YOLO_detect import YOLO

# List points of polygon
points = []

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(img=frame, 
                           center=(point[0], point[1]), 
                           radius=5, 
                           color=(0,0,255))
    frame = cv2.polylines(frame, [np.int32(points)], False, (255, 0, 0), 2)
    return frame

# Camera
video = VideoStream(src=0).start()
frame = video.read()
height, width, channels = frame.shape

# Model
model = YOLO()
detect  = False

while True:
    # Read frame
    frame = video.read()
    frame = cv2.flip(frame, 1)

    # Draw polygon
    frame = draw_polygon(frame, points)

    # If you dont't want to draw polygon, you can set points
    # detect = True
    # points = [(0, 0), (0, width), (-height, width), (-height, 0)]

    # Detect decision
    if detect:
        try:
            frame = model.detect(frame, points)
        except:
            pass

    key = cv2.waitKey(1)
    if key == ord('q'): # Quit
        break
    elif key == ord('d'): # Close polygon
        points.append(points[0])
        detect = True

    # Show frame
    cv2.imshow('Intrusion Warning', frame)
    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

video.stop()
cv2.destroyAllWindows()