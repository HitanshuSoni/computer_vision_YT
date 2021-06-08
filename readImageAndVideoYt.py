import cv2
'''
img = cv2.imread('./lena.png')

cv2.imshow("image", img)

cv2.waitKey(0)'''

'''cap = cv2.VideoCapture('./test_video.mp4')

while True:
    success, img = cap.read()
    cv2.imshow("I'm a Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break