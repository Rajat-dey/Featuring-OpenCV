import cv2
import numpy as np
import matplotlib.pyplot as plt
#                                   0
img = cv2.imread('desk.jpg',cv2.IMREAD_GRAYSCALE)

#IMREAD_COLOR = 1
#IMREAD_UNCHANGED=2

#we can put binary code inplace of IMREAD for calling the fun

cv2.imshow('image', img)  #imshow fun popup a screen display to show the image with two urguments where 1st is the name of the screen
cv2.waitKey(0) #it is used to show tje display untill the key is pressed

cv2.destroyAllWindows() #it is called to destroy the screen after pressing the key


#we can also display image in matplotlib


'''plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([80,100],[50,140], 'c', linewidth=6)
plt.show()'''

cv2.imwrite('deskgray.png',img)




