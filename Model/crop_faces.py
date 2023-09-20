import cv2
import os

dir = 'Images/0_Others'
out = 'Images/0_CroppedOtherFaces'
image_files = [f for f in os.listdir(dir)]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
for image_file in image_files:
    image_path = os.path.join(dir, image_file)
    image = cv2.imread(image_path)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    try:
        (x,y,w,h) = faces[0]
        face = image[y:y+h,x:x+w]
        output = os.path.join(out, image_file)
        face = cv2.resize(face,(100,100))
        cv2.imwrite(output,face)
    except:
        pass