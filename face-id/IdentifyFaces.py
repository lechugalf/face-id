import face_recognition as facer
import cv2

#load and encoding image of Victor face
img1 = facer.load_image_file('images/faces/Victor.jpg')
img1_encod = facer.face_encodings(img1)[0]

#load and encoding imgae of Julio face
img2 = facer.load_image_file('images/faces/Julio.jpg')
img2_encod = facer.face_encodings(img2)[0]

known_face_encodings = [
    img1_encod,
    img2_encod
]

known_face_names = [
    "Victor Alfonso",
    "Julio Profe"
]

#load imagen to identify their faces
test_img = facer.load_image_file('images/test1.jpg')

#find all faces in the test image and encoding them
faces = facer.face_locations(test_img)
encod_faces = facer.face_encodings(test_img, faces)

#compare each of located image to identify with known faces
for (top, right, bottom, left), encod_face in zip(faces, encod_faces):

    #compare located face with known faces
    matches = facer.compare_faces(known_face_encodings, encod_face)
    print matches

    #get index of identify faces
    if True in matches:
        foundindex = matches.index(True)
        name = known_face_names[foundindex]
    else:
        name = "Unknown"

    #draw a box in the located faces with their identified name
    cv2.rectangle(test_img, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.rectangle(test_img, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
    cv2.putText(test_img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255, 255, 255), 1)

#show the results
cv2.imshow("Face ID", test_img)

cv2.waitKey(0) 
cv2.destroyWindow()