# Angkan Bsiwas
# 12.04.2020
# To translate an image


import cv2
import imutils
import numpy as np


imgPath = '/home/dell/PythonCode/Picture/apple.jpg'		
img = cv2.imread(imgPath)						# to load an image

resizeImg = cv2.resize(img, (200,200))					# to resize the loaded image

x = 2
y = 2
translateImg = imutils.translate(resizeImg, x , y)			# to translate the resized image

concateImg = np.concatenate((resizeImg, translateImg), axis = 1)	# to concatenate two images	

cv2.imshow('Picture', concateImg)					# to display concatenated images
cv2.waitKey(0)								# to hold the display window untill any key is pressed
