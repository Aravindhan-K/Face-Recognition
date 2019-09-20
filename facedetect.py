import cv2
import face_recognition
img=cv2.imread("E:\TCS\humaAIn\Images\pic22.jpg")
face_locations=face_recognition.face_locations(img)
face_landmarks_list = face_recognition.face_landmarks(img)

print(face_locations)

#for drawing bounding boxes around faces
for i in face_locations:
    output = cv2.rectangle(img,(i[3],i[2]),(i[1],i[0]),(255,0,255),2)
    cv2.imshow("Image",output)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")