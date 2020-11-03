import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

def Init():
    return  cap.isOpened()

def snap():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        return False

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    return True

def close():
    cap.release()
    cv.destroyAllWindows()
    return True


print(Init())
for i in range(100):
    print(snap())
close()
