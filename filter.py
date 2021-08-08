import cv2
import numpy as np
from PIL import Image
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import streamlit as st
st.title('Thug Life Filter')

class VideoTransformer(VideoTransformerBase):
    def transform(self, image):
        image = image.to_ndarray(format="bgr24")
        maskPath = 'mask.png'

        harcasPath = 'haarcascade_frontalface_default.xml'

        faceCascade = cv2.CascadeClassifier(harcasPath)

        mask = Image.open(maskPath)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 2.1)
        background = Image.fromarray(image)

        for (x, y, w, h) in faces:
            resized_mask = mask.resize((w, h), Image.ANTIALIAS)

            offset = (x, y)
            background.paste(resized_mask, offset, mask=resized_mask)
    
        thug_filter = np.asarray(background)      
        return thug_filter

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

