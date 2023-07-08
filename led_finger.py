import cv2
from cvzone.HandTrackingModule import HandDetector
from boltiot import Bolt
import time
import conf

mybolt=Bolt(conf.bolt_api_key,conf.device_id)

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                print("0")
                mybolt.analogWrite("0","0")
                cv2.imshow("Video",img)
            if fingerup == [0, 1, 0, 0, 0]:
                print("1")
                mybolt.analogWrite("0","51")
                cv2.imshow("Video",img)
            if fingerup == [0, 1, 1, 0, 0]:
                print("2")
                mybolt.analogWrite("0","102")
                cv2.imshow("Video",img)
            if fingerup == [0, 1, 1, 1, 0]:
                print("3")
                mybolt.analogWrite("0","153")
                cv2.imshow("Video",img)
            if fingerup == [0, 1, 1, 1, 1]:
                print("4")
                mybolt.analogWrite("0","204")
                cv2.imshow("Video",img)
            if fingerup == [1, 1, 1, 1, 1]:
                print("5")
                mybolt.analogWrite("0","255")
                cv2.imshow("Video",img)
    
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        mybolt.digitalWrite("0","LOW")
        break
    time.sleep(4)

video.release()
cv2.destroyAllWindows()