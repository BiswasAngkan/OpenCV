#	Angkan Biswas
#	03.05.2019
#	To take a video of 5 seconds using the web camera of the computer.

import cv2

camera = cv2.VideoCapture(0)			#	Get access of the web camera.
for i in range(100):				
	cameraStatus, picture = camera.read()	#	Take a picture using the camera.
	cv2.imshow('My Picture',picture)
	cv2.waitKey(50)				#	Wait for 50 milliseconds	
camera.release()				#	Release the captured camera

cv2.waitKey(0)
