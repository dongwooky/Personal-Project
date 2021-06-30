import cv2
import numpy as np
import sys

#컨테이너 중심점 찾기
def findCenter(approx):
    points = np.squeeze(approx)  # (4, 1, 2) ==> (4, 2)
    center_x = round(np.mean(points[:, 0])) #컨테이너 중심점 찾기 x좌표
    center_y = round(np.mean(points[:, 1])) #컨테이너 중심점 찾기 y좌표
    points_center = [center_x, center_y] #컨테이너 중심
    
    return points_center

capture = cv2.VideoCapture(1) #카메라 열기

if not capture.isOpened():
    print('Camera open failed!')
    sys.exit()

#카메라 Frame 크기 정보
'''
frameWidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frameWidth, frameHeight)
print('frmae size: {}'.format(frame_size))
'''

#카메라 Frame 크기 지정 : 카메라마다 프레임 크기가 다를 수 있다.
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#프레임 단위 작업
while True:
    ret, frame = capture.read() #프레임 읽기

    if not ret:
        print('Frame read error!')
        sys.exit()
        
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #그레이스케일로 변환
    _, frame_binary = cv2.threshold(frame_gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) #이진화 (OTSU 알고리즘 사용)
    contours, _ = cv2.findContours(frame_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for points in contours:
        if cv2.contourArea(points) < 1500:
            continue
        
        approx = cv2.approxPolyDP(points, cv2.arcLength(points, True) * 0.02, True)
        
        if not cv2.isContourConvex(approx) or len(approx) != 4:
            continue
        
        cv2.polylines(frame, [approx], True, (0, 0, 255), thickness = 3) #컨테이너 표시
        
        container_center = findCenter(approx) #컨테이너 중심점 체크
        
        print(container_center) #컨테이너 위치 확인
        
    cv2.imshow('VideoFrame', frame)
    
    if cv2.waitKey(33) == 27:
        break
    
capture.release()
cv2.destroyAllWindows()