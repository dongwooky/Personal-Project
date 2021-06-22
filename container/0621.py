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
    _, frame_binary = cv2.threshold(frame_gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(frame_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for points in contours:
        if cv2.contourArea(points) < 1000:
            continue
        
        approx = cv2.approxPolyDP(points, cv2.arcLength(points, True) * 0.02, True)
        
        if len(approx) != 4:
            continue
        
        cv2.polylines(frame, points, True, (0, 0, 255), thickness = 3)
        
    cv2.imshow('VideoFrame', frame)
    
    if cv2.waitKey(33) == 27:
        break
    
capture.release()
cv2.destroyAllWindows()


        
    