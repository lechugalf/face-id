import face_recognition as facer
import sys, os, fnmatch
import cv2

known_face_encodings = []
known_face_names = []

#load images and their names from a directory
def set_known_faces(dirname):
    for img in fnmatch.filter(os.listdir(dirname), '*.jpg'):
        image = facer.load_image_file(dirname + img)
        known_face_encodings.append(facer.face_encodings(image)[0])
        known_face_names.append(img[:-4])

def main():

    #load and encoding known faces
    set_known_faces(sys.argv[2])

    #load imagen to identify their faces
    test_img = facer.load_image_file(sys.argv[1])

    #find all faces in the test image and encoding them
    faces = facer.face_locations(test_img)
    encod_faces = facer.face_encodings(test_img, faces)

    #compare each of located image to identify with known faces
    for (top, right, bottom, left), encod_face in zip(faces, encod_faces):

        #compare located face with known faces
        matches = facer.compare_faces(known_face_encodings, encod_face)

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

    #exit window
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()