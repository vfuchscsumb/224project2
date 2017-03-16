import numpy as np
import cv2

#create the haar cascade

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")



#read the image
img = cv2.imread("example3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#detect faces in the image
faces = face_cascade.detectMultiScale(img, 1.3, 5)


#pprint.pprint(faces)

#draw rectangles around the faces
for (counter,(x,y,w,h)) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


        cv2.putText(img, "Actor #{}".format(counter+1), (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
             0.6, (0,0, 255), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

#detect eyes in the image 
eyes = eye_cascade.detectMultiScale(roi_gray)


#pprint.pprint(eyes)

for(ex, ey, ew, eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)


smile = smile_cascade.detectMultiScale(
    roi_gray = grey[y:y+h, x:x+w]
    scaleFactor= 1,
    minNeighbors=22,
    minSize=(25, 25),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
    

# Set region of interest for smiles
for (x, y, w, h) in faces:

    print "Found", len(faces), "smiles!"
    
#draw rectangle around smiles

cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)


#print "!!!!"



cv2.imwrite('imagenew.jpg', img)
cv2.waitKey()