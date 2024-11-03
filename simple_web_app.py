import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

# only if the button was pressed, then execute:
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        # cv2 uses BGR, use this to convert:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()

        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 70),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 110),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=1, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)


