import cv2
import numpy as np
#
sando_image = cv2.imread("sando.jpg")
cv2.imshow("foot-long", sando_image)
# 
greyed_sando = cv2.cvtColor(sando_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed", greyed_sando)
# cv2.imshow("blured", cv2.GaussianBlur(gray, (19,19), 0))
height, width, channels = sando_image.shape
# print("height:",height, " width:",width, " number of channels:",channels)
# cv2.imwrite("new_sando_image.png", sando_image)
cv2.imshow("six-inches", sando_image[0:height, 0:width//2]) #[row, col]
cv2.imshow("cascade edge", cv2.Canny(sando_image, 125, 175))

# 
# simplest: read through all pixels, otherwise: use opencv
# detect images for (greens)? then calculate the distance the sensor is from that crop line
# choose the best (closer)? crop line to move to 
#   1(simply compares distance left and right)
#   2(groups left and right crops into vertical lines using least-square fit) 
# detect and recognize (edge detection)? harvestable crops and otherwise
# when no crop (greens)? then robot can turn
field = cv2.imread("field.jpg")
cv2.imshow("f", field)
hsv = cv2.cvtColor(field, cv2.COLOR_BGR2HSV) #convert to hsv
mask = cv2.inRange(hsv, (36, 0, 0), (70, 255,255)) #search colormap range for green

cv2.imshow("greenonly", mask)
# print(mask)
imask = mask>0 #take only white pixels
green = np.zeros_like(field, np.uint8) #fill all non-green blacks
# print(green)
green[imask] = field[imask] #fill all greens
cv2.imshow("green detect", green)
#
#
cv2.waitKey(0)