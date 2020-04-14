# Angkan Bsiwas
# 14.04.2020
# To rotate an image clockwise & anti-clockwise & display side by side 


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/Downloads/Football.png'		
img = cv2.imread(imgPath)							# to load an image

resizeImg = cv2.resize(img, (200,200))						# to resize the loaded image

degree1 = 0
degree2 = 360
for i in range(100):
	rotateImg1 = imutils.rotate(resizeImg, degree1)				# to rotate the resized image clockwise
	rotateImg2 = imutils.rotate(resizeImg, degree2)				# to rotate the resized image anti-clockwise
	concateImg = np.concatenate((rotateImg1, rotateImg2), axis = 1)		# to concatenate two images
	cv2.imshow('Picture', concateImg)					# to display images
	cv2.waitKey(100)							# to hold the display window 100 miliseconds
	
	degree1 = degree1 + 5
	degree2 = degree2 - 5
		
