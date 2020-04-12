# Angkan Bsiwas
# 12.04.2020
# To transalate an image continuosly


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/PythonCode/Picture/apple.jpg'		
img = cv2.imread(imgPath)							# to load an image
	
resizeImg = cv2.resize(img, (200,200))						# to resize the loaded image

x = 5
y = 5
for i in range(50):
	transalateImg = imutils.translate(resizeImg, x ,y)			# to transalate the resize image

	concateImg = np.concatenate((resizeImg, transalateImg), axis = 1)	# to concatenate two images	

	cv2.imshow('Picture', concateImg)					# to display concatenated images
	cv2.waitKey(500)							# to hold the display window for 500 miliseconds

	x = x + 5
	y = y + 5
