# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:43:55 2021

@author: ASUS
"""
#pip install cvzone
#pip install mediapipe
#from cvzone.HandTrackingModule import HandDetector
from HandTrackingModule import HandDetector
#hg.xyz()
import cv2
import numpy as np
import time
#import autopy

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)
while True:
    success,img=cap.read()
    hands,img=detector.findHands(img)
    #hands=detector.findHands(img,draw=False)
    if hands:
        hand1=hands[0]
        lmList1=hand1["lmList"]
        bbox1=hand1["bbox"]
        centerPoint1=hand1["center"]
        handType1=hand1["type"]
        finger1=detector.fingersUp(hand1)
    
        # print(len(lmList1),lmList1)
        #print(bbox1)
        #print(centerPoint1)
        #length,info,img=detector.findDistance(lmList1[8],lmList1[12],img)#with a line drawn
        #length,info=detector.findDistance(lmList1[8],lmList1[12])#without draw line
        if len(hands)==1:
            #hand2=hands[1]
            #lmList2=hand2["lmList"]
            #bbox2=hand2["bbox"]
            #centerPoint2=hand2["center"]
            #handType2=hand2["type"]
            #finger2=detector.fingersUp(hand2)
            # print(handType1,handType2)
            length,info,img=detector.findDistance(lmList1[8],lmList1[12],img)
            #print(length)
            #print(finger1)
            if finger1==[1,1,1,1,1]:
                print("vehicle will move forward")
                cv2.putText(img, "FORWARD", (410, 50), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 3)
            elif finger1==[0,0,0,0,0]:
                print("vehicle will  move backwards")
                cv2.putText(img, "BACKWARD", (400, 50), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 3)
            elif finger1==[0,1,1,0,0] and length>80:
                print("vehicle will turn right")
                cv2.putText(img, "RIGHT", (500, 40), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 3)
            elif finger1==[0,1,1,0,0] and length<80:
                print("vehicle will turn left")
                cv2.putText(img, "LEFT", (500, 40), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
            elif finger1==[0,1,1,1,1]:
                print("vehicle will stop")
                cv2.putText(img, "STOP", (500, 40), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 3)
            else:
                print("invalid input")
            #length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
            #length,info,img=detector.findDistance(centerPoint1,centerPoint2,img)
            
    cv2.imshow("Image", img)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
