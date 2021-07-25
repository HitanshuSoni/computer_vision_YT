import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

BG_COLOR = (192, 192, 192) #gray
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))

with mp_selfie_segmentation.SelfieSegmentation(model_selection = 1) as selfie_segmentation:
    '''bg_image = None'''
    '''bg_image_org = cv2.imread('./pika.jpg')
    bg_image = cv2.resize(bg_image_org, (width, height))'''
    
    while cap.isOpened():
        success, image = cap.read()

        bg_image = cv2.GaussianBlur(image, (55, 55), 0)

        if not success:
            print("No Camera")

            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        image.flags.writeable = False
        results = selfie_segmentation.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        condition = np.stack((results.segmentation_mask,) *3 , axis=-1) > 0.1

        if bg_image is None:
            bg_image = np.zeros(image.shape, dtype = np.uint8)
            bg_image[:] = BG_COLOR
        
        output_image = np.where(condition, image, bg_image)

        cv2.imshow("Virtual Background", output_image)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
