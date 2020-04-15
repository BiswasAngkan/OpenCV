#	Angkan Biswas
#	15.04.2020
#	Get information about the loaded image.

import cv2
import os

imgPath = '/home/dell/PythonCode/Picture/My_Desk.jpg'
img = cv2.imread(imgPath)

print('Image shape: {}'.format(img.shape))
print('Pixel Range: {} - {}'.format(img.max(), img.min()))
print('Data type: {}'.format(img.dtype))
print('Size of the image file: {} Bytes'.format(os.stat(imgPath).st_size))

cv2.imshow('Picture', img)
cv2.waitKey(0)

img = img/255
print('Pixel Range: {} - {}'.format(img.max(), img.min()))
print('Data type: {}'.format(img.dtype))

cv2.imshow('Picture', img)
cv2.waitKey(0)

