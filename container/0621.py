import cv2
import numpy as np
import sys

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('Camera open failed!')
    sys.exit()
    
while True:
    ret, frame = capture.read()
    
    if not ret:
        print('Frame read error!')
        sys.exit()
        
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame_binary = cv2.threshold(frame_gray, 0, 255, cv2.THRESH_BINARY|cv2.TRHESH_OTSU)
    contours, _ = cv2.findcontours()