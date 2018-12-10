import numpy as np
import cv2

# 视频捕获

cap = cv2.VideoCapture(0)

while (True):
    # 一帧一帧取
    ret , frame = cap.read()

    # 取灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
