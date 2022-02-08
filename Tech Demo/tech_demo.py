# import module_manager
# module_manager.review()
#import argparse
import numpy as np
import cv2



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


















'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
 
    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

 #################
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
'''