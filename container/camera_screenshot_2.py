# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:10:45 2021

@author: 82106
"""

import cv2
import os
import sys

if not os.path.exists('result'):
    os.makedirs('result')

capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print('Camera open failed!')
    sys.exit()

'''
frameWidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(capture.get(cv2.CAP_PROP_FRMAE_HEIGHT))
frameSize = (frameWidth, frameHeight)
print('frame size : {}'.format(frameSize))
'''

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 1

while True:
    ret, frame = capture.read()
    
    if not ret:
        print('Frame read error!')
        sys.exit()
        
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    if key == ord('s'):
        print('Screenshot saved!')
        cv2.imwrite('result/screenshot{}.png'.format(count), frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
        count += 1
        
    elif key == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
    
        
    
    
