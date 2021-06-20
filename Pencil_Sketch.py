import cv2
img = cv2.imread('./hitanshu.jpeg')
img = cv2.resize(img, (900, 800))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(gray)
#cv2.imshow("Gray", gray)
#cv2.imshow("inv", img_invert)
gblur_img = cv2.GaussianBlur(img_invert, (23, 23), sigmaX = 0, sigmaY=0)
#cv2.imshow("Blur", gblur_img)
dodge_img = cv2.divide(gray, 255-gblur_img, scale=256)

cv2.imshow("Dodge", dodge_img)

cv2.imwrite('./hitanshuSKT.jpg', dodge_img)
cv2.waitKey(0)