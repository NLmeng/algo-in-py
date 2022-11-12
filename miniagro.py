import cv2
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

# b,g,r = cv2.split(sando_image)
# cv2.imshow("Blue",cv2.Canny(b, 125, 175))
# cv2.imshow("Green",g)
# cv2.imshow("Red",r)
# 
cv2.waitKey(0)