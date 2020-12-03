import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    img = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
    # Display the resulting frame
    cv.imshow('frame', img)
    key = cv.waitKey(1)
    if  key == ord('q'):
        break
    if key == ord('s'):
        cv.imwrite('teachablemachinesimage.png', img)
        print('updated')

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
