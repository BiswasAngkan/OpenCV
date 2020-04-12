# Angkan Bsiwas
# 12.04.2020
# To rotate an image


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/PythonCode/Picture/apple.jpg'		
img = cv2.imread(imgPath)					# to load an image

resizeImg = cv2.resize(img, (200,200))				# to resize the loaded image

degree = 1
for i in range(1000):
	rotateImg = imutils.rotate(resizeImg, degree)			# to rotate the resize image

	concateImg = np.concatenate((resizeImg, rotateImg), axis = 1)	# to concatenate two images	

	cv2.imshow('Picture', concateImg)				# to display concatenated images
	cv2.waitKey(5)							# to hold the display window untill any key is pressed

	degree = degree + 5
