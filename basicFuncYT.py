import cv2
import numpy as np

img = cv2.imread('./lena.png')

kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(img, (7, 7), 0)

imgCanny = cv2.Canny(img, 150, 200)

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

imgErode = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny-Edge Img", imgCanny)
cv2.imshow(" Dilation Edge Img", imgDilation)
cv2.imshow(" Erode Edge Img", imgErode)


cv2.waitKey(0)