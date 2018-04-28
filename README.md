# Face ID
Identify faces from a picture or webcam video using the [face recognition](https://github.com/ageitgey/face_recognition) module in python


## Getting Started
IdentifyFaces.py compares found faces on an image with faces previously stored in a directory

### Prerequisites
IdentifyFaces.py uses Python 2.7 and the packages below

* face_recognition 1.2
* opencv-python 3.4

You can install this packages using pip
```bash
sudo pip install face_recognition
sudo pip install opencv-python
```
visit https://github.com/ageitgey/face_recognition for more information about install face recognition module.

### Installing
1. Clone this repository into a directory of your choice.
```bash
git clone https://github.com/lechugalf/face-id.git
```
If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

```bash
cd face-id
```
#### Run IdentifyFaces.py
In order to select the images with which you will work create a folder with all images of recognized faces, name the images as you want to show them in the result. run IdentifyFaces.py through the terminal and pass the image to identify as the first argument and the directory of you recognized faces as the second argument.

```bash
cd IdentifyFaces
python IdentifyFaces.py image-to-identify directory-of-known-recognized-faces
```

##### Run Test
You can test how works running IdentifyFaces.py as follow

```bash
python IdentifyFaces.py test1.jpg faces/
```

#### Run IdentifyFacesWebcam.py
You have pass as the first argument the folder with de images of the faces to recognize in the webcam
```bash
cd IdentifyFacesWebcam
python IdentifyFacesWebcam.py directory-of-known-recognized-faces
```

##### Run Test
You can test how works running IdentifyFacesWebcam.py as follow

```bash
python IdentifyFacesWebcam.py faces/
```

## Authors

* **Alfonso Lechuga** - *Initial work* - [lechugalf](https://github.com/lechugalf)
* Visit [face recognition](https://github.com/ageitgey/face_recognition)  to know more about the creators for face recognition module

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
