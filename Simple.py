import numpy as np
import cv2 as cv

global cap 

def Init():
    global cap
    cap = cv.VideoCapture(0)
    ret, frame = cap.read()
    return  ret #cap.isOpened()

def snap():
    global cap
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        return False

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    return True

def close():
    global cap
    cap.release()
    cv.destroyAllWindows()
    return True
