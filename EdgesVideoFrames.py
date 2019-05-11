#	Angkan Biswas
#	08.05.2019
#	Detect edge of each frame using Canny algorithm.

import cv2

camera = cv2.VideoCapture(0)							#	Get access of the web camera.

for i in range(100): 
	_, picture = camera.read()						#	Take a picture using the camera.

	lowThreshold = 40							
	highThreshold = 120							#	Generaly, highThreshold = 3*lowTheshold
	edge = cv2.Canny(picture, lowThreshold, highThreshold)			#	Detect edge using Canny algorithm

	cv2.imshow('Edge',edge)							#	Display edge
	cv2.waitKey(50)								#	Hold display window

camera.release()								#	Release the captured camera
