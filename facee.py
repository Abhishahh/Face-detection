import cv2
#A xml file which helps to take the data of face
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#loading the image
img = cv2.imread("robert_downey.jpg")
#converting the image into black n white
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#putting coordinates around the face
face_coordintes = face_data.detectMultiScale(gray_img)
#Loop to get all faces
for(x,y,w,h) in face_coordintes:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
#final image
cv2.imshow("robert_downey", img)
#wait unless a key pressed
cv2.waitKey()
