

import cv2
from gaze_tracking import GazeTracking
import pyautogui as pag
import os 

os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

isLeft = 0
isCenter = 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""
    
    if gaze.is_left():
        
        isLeft += 1 
        isCenter -=1
        print("Looking at Secondary")

    elif gaze.is_center():
        isCenter += 1
        isLeft -= 1
        print("Looking at MBP")
        
    
    if (isLeft > 3) :
        pag.click(x = 629, y = 947)
        isCenter = 0
        isLeft = 0
    elif (isCenter > 3) :
        pag.click(x = 2688,y=495)
        isCenter = 0
        isLeft = 0 

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
