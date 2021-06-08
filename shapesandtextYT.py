import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (512, 512), (0, 0, 255), 3)
cv2.line(img, (512, 0), (0, 512), (0, 0, 255), 3)

#cv2.rectangle(img, (0 ,0), (256, 256), (0 ,255, 0), cv2.FILLED)
cv2.rectangle(img, (0 ,0), (256, 256), (0 ,255, 0), 3)

cv2.circle(img, (256 ,256), 100, (0, 255 ,255), 3)

cv2.putText(img, "How are you Earth??", (100 ,30), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 150), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)