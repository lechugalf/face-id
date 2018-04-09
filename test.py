import os, fnmatch
import face_recognition as facer
import cv2

known_face_encodings = []
known_face_names = []

def set_known_faces(dirname):
    for img in fnmatch.filter(os.listdir(dirname), '*.jpg'):
        image = facer.load_image_file(dirname + img)
        known_face_encodings.append(facer.face_encodings(image)[0])
        known_face_names.append(img[:-4])

def main():
    pass

if __name__ == '__main__':
    main()

"""
def get_faces(img, model):
    faces = []
    face_locations = facer.face_locations(img, 1, model)
    for face in face_locations:
        top, right, bottom, left = face
        faces.append(img[top:bottom, left:right])
    return faces
"""