#	Angkan Biswas
#	12.05.2019
#	Display edge & grayscale picture side by side.

import cv2
import numpy as np

camera = cv2.VideoCapture(0)							#	Get access of the web camera.

lowThreshold = 40							
highThreshold = 120								#	Generaly, highThreshold = 3*lowTheshold

for i in range(100): 
	_, picture = camera.read()						#	Take a picture using the camera.
	
	picture = cv2.resize(picture,(400,300))					#	Resize image
	edge = cv2.Canny(picture, lowThreshold, highThreshold)			#	Detect edge using Canny algorithm
	grayPicture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)			#	Convert RGB to Grayscale
	concateImg = np.concatenate((grayPicture, edge),axis=1)			# 	Add two images horizontally	

	cv2.imshow('Picture+Edge',concateImg)					#	Display edge grayscale picture
	cv2.waitKey(50)								#	Hold display window

camera.release()								#	Release the captured camera
