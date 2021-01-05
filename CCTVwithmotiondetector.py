#  1- import cv2 library by just type "pip install opencv-python" in terminal.
#  2- import playsound lib if you want to play mp3 sound "pip install playsound".
#  3- download the mp3 or wav file. wav file is more compatible with python.
#  4- if you want to play mp3 file do not import winsound, or it's upto you.

import cv2
import winsound
from playsound import playsound

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    kernel = (5, 5)
    dilated = cv2.dilate(thresh, kernel, iterations=3)
    countours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in countours:
        if cv2.contourArea(c) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        winsound.Beep(500, 300)                                 ## it's a by default system generated sound.
        #winsound.PlaySound('Police.wav', winsound.SND_ASYNC)   ## or you  can use high frequency sound..
        #playsound('HomeSound.mp3')                            ## use this code for mp3 file and comment all the winsound line.

    if cv2.waitKey(100) == ord('q'):
        break
    cv2.imshow('cam1', frame1)
