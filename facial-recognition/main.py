from PIL import Image, ImageDraw
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

    #load faces and names from a folder
    set_known_faces('images/faces/')

    #load imagen to identify their faces
    image = facer.load_image_file('images/test1.jpg')

    #locate faces on image and encode them
    faces = facer.face_locations(image)
    encodig_faces = facer.face_encodings(image, faces)

    #use ImageDraw to draw the match faces in the image
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)

    #compare each of locate images
    for encod_face in encodig_faces:
        matches = facer.compare_faces(known_face_encodings, encod_face)
        print matches
        

        if True in matches:
            index = matches.index(True)
            top, right, bottom, left = faces[index+1]
            name = known_face_names[index]

            #draw rectangle on locatefaces
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            #draw label names
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    del draw

    image.show()






    #cv2.imshow("input1", found_faces[2])
    #cv2.imshow("input2", found_faces[4])
    #cv2.waitKey(0)
    #img_pil = Image.fromarray(found_faces[0])
    #img_pil.show()
    

if __name__ == '__main__':
    main()

def get_faces(img, model):
    faces = []
    face_locations = facer.face_locations(img, 1, model)
    for face in face_locations:
        top, right, bottom, left = face
        faces.append(img[top:bottom, left:right])
    return faces