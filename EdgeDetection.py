#	Angkan Biswas
#	08.05.2019
#	Detect edge using Canny algorithm.

import cv2

camera = cv2.VideoCapture(0)						#	Get access of the web camera.
_, picture = camera.read()						#	Take a picture using the camera.
camera.release()							#	Release the captured camera

lowThreshold = 40							
highThreshold = 120							#	Generaly, highThreshold = 3*lowTheshold
edge = cv2.Canny(picture, lowThreshold, highThreshold)			#	Detect edge using Canny algorithm

cv2.imshow('Edge',edge)							#	Display edge
cv2.waitKey(0)								#	Hold display window

imgFileName = '/home/dell/Example/GitHub/Picture/MyEdge.jpg'
cv2.imwrite(imgFileName, edge)						#	Save picture
