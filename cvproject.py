import numpy as np
import pprint
import cv2


#create the haar cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mouth.xml")
righteye_cascade = cv2.CascadeClassifier("haarcascade_righteye.xml")
lefteye_cascade = cv2.CascadeClassifier("haarcascade_lefteye.xml")
nose_cascade = cv2.CascadeClassifier("haarcascade_nose.xml")


def faceDetection(userImage):
    img = cv2.imread(userImage)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    #draw rectangles around the faces
    for (counter,(x,y,w,h)) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img, "Person #{}".format(counter+1), (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6, (0,0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # print "faces"
    # print str(faces[0])
    # return str(faces[0])
    if len(faces ) > 0:
        print faces
    #left eye
    lefteye = lefteye_cascade.detectMultiScale(roi_gray, 1.1, 3)
    for(ex, ey, ew, eh) in lefteye:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    #right eye
    righteye = righteye_cascade.detectMultiScale(roi_gray, 1.1, 3)
    for(ex, ey, ew, eh) in righteye:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    # print "eyes"
    # print str(eyes[0])   
    # return str(eyes[0])
    if len(righteye) > 0:
        print righteye
    if len(lefteye) > 0:
        print lefteye
    #nose   
    nose = nose_cascade.detectMultiScale(roi_gray, 1.1)
    for(ex, ey, ew, eh) in nose:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,0,0),2)
    #mouth
    mouth = mouth_cascade.detectMultiScale(roi_gray, 1.1, 3)

    for(ex, ey, ew, eh) in mouth:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (255,229,0),2)
    for (x, y, w, h) in mouth:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 158, 0), 1)
        cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 158, 0), 1)

    #smile 
    smile = smile_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for(ex, ey, ew, eh) in mouth:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (255, 40, 89),2)
    for (x, y, w, h) in smile:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 40, 89), 2)
        cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 40, 89), 2)
        break  

#pprint 
    cv2.imwrite('static/imagebrandnew.jpg', img)
        # return "done"


#read the image
# img = cv2.imread("person7.jpg")
img = cv2.imread("person7.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# newgray = cv2.equalizeHist(gray)

# print newgray

#detect faces in the image
faces = face_cascade.detectMultiScale(img, 1.1, 3)


# pprint.pprint(faces)

#draw rectangles around the faces
for (counter,(x,y,w,h)) in enumerate(faces):
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    cv2.putText(img, "Person #{}".format(counter+1), (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6, (0,0, 255), 2)
        
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
        
#detect eyes in the image

#eyes = eye_cascade.detectMultiScale(roi_gray)

#left eye in side face

lefteye = lefteye_cascade.detectMultiScale(roi_gray, 1.1, 3)

for(ex, ey, ew, eh) in lefteye:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    
    roi_gray = gray[ey:ey+eh, ex:ex+ew]
    roi_color = img[ey:ey+eh, ex:ex+ew]


#right eye in side face

righteye = righteye_cascade.detectMultiScale(roi_gray, 1.1, 3)

for(ex, ey, ew, eh) in righteye:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    
    roi_gray = gray[ey:ey+eh, ex:ex+ew]
    roi_color = img[ey:ey+eh, ex:ex+ew]


#pprint.pprint(eyes)

#for(ex, ey, ew, eh) in eyes:
#cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)

#detecting nose in side the face

nose = nose_cascade.detectMultiScale(roi_gray, 1.1)

for(ex, ey, ew, eh) in nose:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,0,0),2)
    
#detecting mouth in side face

mouth = mouth_cascade.detectMultiScale(roi_gray, 1.1, 3)

for(ex, ey, ew, eh) in mouth:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (255,229,0),2)

# Set region of interest for mouth

for (x, y, w, h) in mouth:
    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 158, 0), 1)
    cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 158, 0), 1)
    break

#pprint.pprint(mouth)
    
#detecting smile in side mouth 
smile = smile_cascade.detectMultiScale(roi_gray, 1.3, 5)

for(ex, ey, ew, eh) in mouth:
    cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (255, 40, 89),2)


# Set region of interest for smiles
    for (x, y, w, h) in smile:
        print "Found", len(smile), "smiles!"
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 40, 89), 2)
        cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 40, 89), 2)
        break


#print "!!"




cv2.imwrite('imagenew.jpg', img)
cv2.waitKey()