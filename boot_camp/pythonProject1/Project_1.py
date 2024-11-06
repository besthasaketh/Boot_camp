from PIL import ImageTk,Image
import cv2
inputimage=cv2.imread('IMG_20231222_121112.jpg')
blue,green,red=cv2.split(inputimage)
img=cv2.merge((red,green,blue))
im=Image.fromarray(img)
image1=im.resize((240,240))
image1=ImageTk.PhotoImage(image1)
gray_img=cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
for (x, y, w, h) in faces_rect:
    outputimage=cv2.rectangle(inputimage, (x, y), (x + w, y + h), (0, 350, 0), 10)