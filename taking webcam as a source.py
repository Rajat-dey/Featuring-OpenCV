import cv2
import numpy as np

cap=cv2.VideoCapture(0) #videocapture is used to take webcm as output


#for creating a video as a output file

fourcc= cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 340)) #20 refers to the frame per seconds

while True:
    ret, frame= cap.read() #ret=return, frame of every video of input webcam to read
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #for creating another frame with gray color
    
    out.write(frame)
    cv2.imshow('videoframe',frame)
    cv2.imshow('grayframe',gray)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):   #0xFF == ord('q') is used shut down the window with pressing of q 
        break
    
cap.release()
out.release() #it should be called after cap.ralease to get the video
cv2.destroyAllWindows()