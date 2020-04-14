# Angkan Bsiwas
# 14.04.2020
# To concatenate a translated image & rotated image side by side 


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/Downloads/Football.png'		
img = cv2.imread(imgPath)							# to load an image

resizeImg = cv2.resize(img, (200,200))						# to resize the loaded image

degree = 10
x = 2
y = 2

for i in range(100):
	rotateImg = imutils.rotate(resizeImg, degree)				# to rotate the resized image
	translateImg = imutils.translate(resizeImg, x , y)			# to translate the resize image
	concateImg = np.concatenate((translateImg, rotateImg), axis = 1)	# to concatenate two images
	cv2.imshow('Picture', concateImg)					# to display images
	cv2.waitKey(100)							# to hold the display window 100 miliseconds
	
	degree = degree + 5
	x = x + 5
	y = y + 5
		
