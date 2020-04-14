# Angkan Bsiwas
# 14.04.2020
# To translate an image after rotation


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/PythonCode/Picture/apple.jpg'		
img = cv2.imread(imgPath)							# to load an image

resizeImg = cv2.resize(img, (200,200))						# to resize the loaded image

degree = 10
x = 2
y = 2

for i in range(100):
	rotateImg = imutils.rotate(resizeImg, degree)				# to rotate the resized image
	translateImg = imutils.translate(rotateImg, x , y)			# to translate the rotated image

	cv2.imshow('Picture', translateImg)					# to display images
	cv2.waitKey(100)							# to hold the display window 100 miliseconds
	
	degree = degree + 5
	x = x + 5
	y = y + 5
		
