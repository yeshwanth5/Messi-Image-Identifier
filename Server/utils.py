import tensorflow as tf
import numpy as np
import cv2
import os

class utils:

    def __init__(self):
        current_directory = os.getcwd()
        dir = os.path.join(current_directory,'Server/Artifacts')
        self.model = tf.keras.models.load_model(os.path.join(dir,'MessiIdentifierModel.h5'))

    def validate(self, image):
        current_directory = os.getcwd()
        dir = os.path.join(current_directory,'Server/Artifacts')
        face_cascade = cv2.CascadeClassifier(os.path.join(dir,'haarcascade_frontalface_default.xml'))
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        messi_present = []
        if faces is None:
            return False
        for face_indices in faces:
            (x,y,w,h) = face_indices
            face = image[y:y+h,x:x+w]
            face = cv2.resize(face,(100,100))
            face = face/255
            face = np.expand_dims(face,axis=0)
            messi_present.append(round(self.model.predict(face)[0][0]))
        return any(messi_present)