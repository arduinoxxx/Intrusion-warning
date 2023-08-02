from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import cv2
import numpy as np
# from telegram_utils import send_telegram
import datetime
import threading
import torch

def isInside(points, centroid):
    polygon = Polygon(points)
    centroid = Point(centroid)
    return polygon.contains(centroid)

def draw_bbox(frame, xmin, ymin, xmax, ymax, confidence, class_name):
    start_point = (xmin, ymax)
    end_point = (xmax, ymin)
    color1 = (255, 0, 0)
    color2 = (0, 255, 0)
    result = cv2.rectangle(frame, np.int32(start_point), np.int32(end_point), color1, 2)
    result = cv2.putText(frame, str(confidence), (int(np.mean([xmin, xmax])), int(ymin + 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, color2, 2)
    return result

class YOLO():
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def detect(self, frame, points):
        result = self.model(frame)
        try:
            for obj in np.array(result.xyxy[0]):
                xmin, ymin, xmax, ymax, confidence, class_name = obj
                if int(class_name) == 0:
                    frame = draw_bbox(frame, xmin, ymin, xmax, ymax, confidence, class_name)
                    centroid = (int(np.mean([xmin, xmax])), int(np.mean([ymin, ymax])))
                    cv2.circle(frame, centroid, 5, (0, 0, 255), -1)

                    if isInside(points, centroid):
                        frame = self.alert(frame)
            return frame
        except:
            pass
    
    def alert(self, img):
        cv2.putText(img, "ALARM!!!!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return img
