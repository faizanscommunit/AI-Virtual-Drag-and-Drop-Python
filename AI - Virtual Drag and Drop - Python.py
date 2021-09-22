#**** ---- Note --- ****#
# AI Virtual Drag and Drop - Python
# By Faizanscommunit
# MIT Licensed

#**** --- Source Code --- ****#

import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
cx, cy, w, h = 100, 100, 200,200
while True:
    success, img = cap.read()
    img = cv2.flip(img, 0)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    if lmList:
        cursor = lmList[8]
        if cx-w//2 < cursor[1] < cx+w//2 and cy-h//2 < cursor[2] < cy+h//2:
            colorR = 0, 255, 0
            cx, cy = cursor[1], cursor[2]
        else:
            colorR = (255, 0, 255)
    cv2.rectangle(img, (cx-w//2, cy-h//2),
                  (cx+w//2, cy+h//2), colorR, cv2.FILLED)
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break

#**** --- Social Links --- ****#
#  Github: https://github.com/faizanscommunit
#  Fiverr: https://fvrr.co/3iZIX0L
#  Website: https://faizanscommunit.pythonanywhere.com/
#  Instagram: https://www.instagram.com/faizanscommunit/
