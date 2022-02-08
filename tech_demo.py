import module_manager
module_manager.review()
import cv2
import numpy as np

#set all images to variables to make them easier to access
coins = cv2.imread('coinimage.png')
circles = cv2.imread('circlespic.png')
colorcirc = cv2.imread('colorcircles.png')
beccy = cv2.imread('beccy.jpg')
beccy2 = cv2.imread('beccy2.jpg')

#averaging, low-pass filter kernel
blurbeccy = cv2.blur(beccy, (5, 5))
#can also also use mean blur
blurbeccy2 = cv2.medianBlur(beccy2,5)
blurcoins = cv2.medianBlur(coins,5)


#converts the colors in a colorful image to black and white
graycirc = cv2.cvtColor(colorcirc, cv2.COLOR_BGR2GRAY)
graybeccy = cv2.cvtColor(beccy, cv2.COLOR_BGR2GRAY)
grayblurcoins = cv2.cvtColor(blurcoins, cv2.COLOR_BGR2GRAY)

#changes the threshold of the colors for color or black and white
ret,threshcoins = cv2.threshold(grayblurcoins,235,255,cv2.THRESH_BINARY)
ret,threshbeccy = cv2.threshold(blurbeccy,100,255,cv2.THRESH_BINARY_INV)


#put citcles around coins
img = cv2.imread('coinimage.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,\
                param1=75,param2=100,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',threshbeccy)
cv2.waitKey(0)
cv2.destroyAllWindows()
