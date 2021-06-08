import cv2
img = cv2.imread('./lambo.png')

print(img.shape)


imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCrop = img[0:200, 200:500]
print(imgCrop.shape)


cv2.imshow("Orignal", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Crop", imgCrop)

cv2.waitKey(0)